from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import classification_prompt

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)

chain = classification_prompt | llm

response = chain.invoke({"message": "My order is super delayed."})

print(response.content)
