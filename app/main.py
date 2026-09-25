from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import classification_prompt
from schemas import ClassificationResult

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)

structuredllm = llm.with_structured_output(ClassificationResult)

chain = classification_prompt | structuredllm

response = chain.invoke({"message": "My order is super delayed."})

print(response)
print(response.category + "\n")
print(response.reason)
