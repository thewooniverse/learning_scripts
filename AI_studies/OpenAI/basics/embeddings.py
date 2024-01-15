# import modules
from dotenv import load_dotenv
import os
import json
from openai import OpenAI
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4, width=80, depth=2)

# env variables, constants and API keys
load_dotenv()
openai_api_key=os.getenv('OPENAI_API_KEY', 'YourAPIKey_BACKUP')
serpapi_api_key=os.getenv("SERPAPI_API_KEY", "YourAPIKey_Backup")
# print(serpapi_api_key) # check
# print(openai_api_key)

client = OpenAI()



response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-ada-002"
)

print(response.data[0].embedding)
""" Example Response ---
{
  "data": [
    {
      "embedding": [
        -0.006929283495992422,
        -0.005336422007530928,
        ...
        -4.547132266452536e-05,
        -0.024047505110502243
      ],
      "index": 0,
      "object": "embedding"
    }
  ],
  "model": "text-embedding-ada-002",
  "object": "list",
  "usage": {
    "prompt_tokens": 5,
    "total_tokens": 5
  }
}
"""


