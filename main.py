import os
import sys
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


if __name__ == '__main__':
	if len(sys.argv) > 1:
		client = genai.Client(api_key=api_key)
		model = "gemini-2.0-flash-001"
		contents = sys.argv[1]

		response = client.models.generate_content(
		    model=model, contents=contents
		)
		print(response.text)

		prompt_token_count = response.usage_metadata.prompt_token_count
		candidates_token_count = response.usage_metadata.candidates_token_count
		print("Prompt tokens:", prompt_token_count)
		print("Response tokens:", candidates_token_count)
	else:
		print("No prompt given in the CLI. Please provide a prompt. Example: python main.py <prompt here>")
		exit(1)
