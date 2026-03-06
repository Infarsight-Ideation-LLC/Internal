import json
from openai import AzureOpenAI

def extract_project_details(text):

    # load prompt config
    with open("config/prompt.json", "r") as f:
        prompt_config = json.load(f)

    task = prompt_config["prompt"]["task"]
    instructions = prompt_config["prompt"]["instructions"]
    parameters = prompt_config["prompt"]["parameters"]
    output_format = prompt_config["prompt"]["output_format"]

    client = AzureOpenAI(
        api_key="4Ng4vnx2KNiWNF9PTdG79Df5kWcV3S9Ci62WQvdwh1Dpr4FphNFQJQQJ99CAACHYHv6XJ3w3AAAAACOG2jHs",
        api_version="2025-01-01-preview",
        azure_endpoint="https://rs-ai-internal-projects-poc-dev.cognitiveservices.azure.com"
    )

    response = client.chat.completions.create(
        model="IFS_Internal_POC_Dev",
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

    return response.choices[0].message.content