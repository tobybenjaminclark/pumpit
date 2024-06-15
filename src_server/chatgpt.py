import os
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

model = OpenAI(model_name="gpt-3.5-turbo-instruct")

context = "Please reply a very, very short concise reply. You are 'HEAT GEEK' an AI assistant in a HEAT PUMP system planning app. To clear the users current design embed CLEAR_DESIGN in your response."

def generate_response(prompt):
  """Takes a prompt and provides the ChatGPT response.

  Args:
      prompt (String): The string that will be passes as the ChatGPT prompt

  Returns:
      String: The response to the given prompt
  """
  response = model.invoke(context + prompt)
  return response