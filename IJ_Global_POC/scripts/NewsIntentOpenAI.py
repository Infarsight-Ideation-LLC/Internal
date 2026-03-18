import json
from openai import AzureOpenAI


def detect_news_intent(text):

    # relevance json load
    with open("config/relevantnews.json") as f:
        relevance = json.load(f)

    phrases = relevance["relevanceFilters"]["phrases"]
    keywords = relevance["relevanceFilters"]["keywords"]

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
Analyse the following project/news text.

{text}

Determine the intent of the news using these phrases or keywords. Donot provide any explanation.

Phrases:
{phrases}

Keywords:
{keywords}

Return:
1. Detected Intent

"""
            }
        ]
    )

    return response.choices[0].message.content