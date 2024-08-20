from openai import AzureOpenAI
from .prompts import Lib_prompt


client = AzureOpenAI(api_key="******",
	api_version="**********",
	azure_endpoint="***********")

def send_to_open_ai(prompt):
	try:
		message = [{"role": "user", "content": prompt}]
		print(message)
		complition = (client.chat.completions.create(model="gpt-35-turbo-16k",
			messages=message, temperature=0, max_tokens=2000, top_p=0.5, frequency_penalty=0,
			presence_penalty=0
			))
		return complition.choices[0].message.content
	except Exception as e:
		print(str(e))
		print("unable to connect openAI service please check connection details.")
		return ""