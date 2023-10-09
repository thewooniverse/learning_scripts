from dotenv import load_dotenv
import os
import openai



load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
print(openai_api_key)


