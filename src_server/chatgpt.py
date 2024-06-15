import os
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

model = OpenAI(model_name="gpt-3.5-turbo-instruct")

def generate_response(prompt):
  """Takes a prompt and provides the ChatGPT response.

  Args:
      prompt (String): The string that will be passes as the ChatGPT prompt

  Returns:
      String: The response to the given prompt
  """
  response = model.invoke(prompt + ". Please reply a very, very short concise reply.")
  return response