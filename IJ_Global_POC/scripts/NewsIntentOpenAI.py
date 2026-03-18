import json
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

def detect_news_intent(text):

    # relevance json load
    with open("config/relevantnews.json") as f:
        relevance = json.load(f)

    phrases = relevance["relevanceFilters"]["phrases"]
    keywords = relevance["relevanceFilters"]["keywords"]

    # Azure OpenAI client using ENV
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
Analyse the following project/news text.

{text}

Determine the intent of the news using these phrases or keywords.
Do not provide any explanation.

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