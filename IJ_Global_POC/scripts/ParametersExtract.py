import json
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

def extract_project_details(text):

    # load prompt config
    with open("config/prompt.json", "r") as f:
        prompt_config = json.load(f)

    task = prompt_config["prompt"]["task"]
    instructions = prompt_config["prompt"]["instructions"]
    parameters = prompt_config["prompt"]["parameters"]
    output_format = prompt_config["prompt"]["output_format"]

    # Create Azure OpenAI client using ENV variables
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {
                "role": "user",
                "content": f"""
{task}

{instructions}

Parameters to extract:
{parameters}

Expected JSON format:
{output_format}

Text:
{text}
"""
            }
        ]
    )

    # Log token usage
    if hasattr(response, "usage"):
        print("Prompt Tokens:", response.usage.prompt_tokens)
        print("Completion Tokens:", response.usage.completion_tokens)
        print("Total Tokens:", response.usage.total_tokens)

    return response.choices[0].message.content