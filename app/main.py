from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import classification_prompt


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)

message = "My order is very delayed."

prompt = classification_prompt.invoke({"message": message})

response = llm.invoke(prompt)

print(response.content)