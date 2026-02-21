from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# This is the demo model which doesn't run. We have to pay to access the model.
# This is the closed source model.
model = ChatGoogleGenerativeAI(model = 'gemini-2.5')

result = model.invoke("What is large language model ?")
print(result.content)

