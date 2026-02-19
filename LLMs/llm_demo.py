from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# This is the demo model which doesn't run. We have to pay to access the model.
llm = OpenAI(model="gpt-model")

result = llm.invoke("What is langchain ?")
print(result)