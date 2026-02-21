from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

# This is the demo model which doesn't run. We have to pay to access the model.
# This is the closed source model.
model = ChatAnthropic(model = "claude-sonnet-4.5-20241118")

result = model.invoke("Who is the current prime minister of nepal?")
print(result.content)