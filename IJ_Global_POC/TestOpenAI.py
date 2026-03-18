from openai import AzureOpenAI
import json

# load prompt config
with open("config/prompt.json") as f:
    prompt_config = json.load(f)

task = prompt_config["prompt"]["task"]
instructions = prompt_config["prompt"]["instructions"]
parameters = prompt_config["prompt"]["parameters"]

# dummy text for testing
text = """
Twin Hills Wind Farm project has been proposed in Western Australia near Eneabba.
The project will involve the construction of up to 110 wind turbines and renewable energy infrastructure.
The project developer is Twin Hills Wind Farm Pty Ltd.
The current project status is Referral Decision - Open for Public Comment.
"""

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

Extract these parameters:
{parameters}

Text:
{text}
"""
        }
    ]
)

print(response.choices[0].message.content)