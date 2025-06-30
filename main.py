import os
from dotenv import load_dotenv
from google import genai
from sys import argv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=argv[1],
)

response_text = response.text
print(response_text)

prompt_token_count = response.usage_metadata.prompt_token_count
candidates_token_count = response.usage_metadata.candidates_token_count

print(f"Prompt tokens: {prompt_token_count}")
print(f"Response tokens: {candidates_token_count}")
