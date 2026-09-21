from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import classification_prompt


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)

message = "The order was so amazing. I loved it."

prompt = classification_prompt.invoke({"message": message})

response = llm.invoke(prompt)

print(response.content)