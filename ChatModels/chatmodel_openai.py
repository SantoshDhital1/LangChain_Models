from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
# This is the demo model which doesn't run. We have to pay to access the model.
# This is the closed source model.
chatmodel = ChatOpenAI(model='gpt-4', temperature=0.5, max_completion_tokens=50)

result = chatmodel.invoke("What is langchain?")
print(result)