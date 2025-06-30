import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from sys import argv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
user_prompt = argv[1]
verbose = len(argv) > 2 and argv[2].lower() == "--verbose"

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

prompt_token_count = response.usage_metadata.prompt_token_count
candidates_token_count = response.usage_metadata.candidates_token_count
response_text = response.text

if verbose:
    print(f"\nUser prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {candidates_token_count}\n")
print(response_text)
