import os
import sys

from dotenv import load_dotenv

from google import genai
from google.genai import types



def main():
	load_dotenv()

	args = sys.argv[1:]

	if not args:
		print("No prompt given in the CLI. Please provide a prompt.\nUsage: python main.py <prompt here>")
		sys.exit(1)


	api_key = os.environ.get("GEMINI_API_KEY")
	client = genai.Client(api_key=api_key)
	model = "gemini-2.0-flash-001"
	user_prompt = args[0]

	messages = [
		types.Content(role="user", parts=[types.Part(text=user_prompt)]),
	]

	response = client.models.generate_content(
	    model=model, contents=messages
	)
	print(response.text)

	if "--verbose" in args:
		prompt_token_count = response.usage_metadata.prompt_token_count
		candidates_token_count = response.usage_metadata.candidates_token_count
		print("User prompt:", user_prompt)
		print("Prompt tokens:", prompt_token_count)
		print("Response tokens:", candidates_token_count)


if __name__ == '__main__':
	main()
