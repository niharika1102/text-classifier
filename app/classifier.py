from collections import Counter

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from app.prompt import classification_prompt
from app.schemas import ClassificationResult

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.7)

structuredllm = llm.with_structured_output(ClassificationResult)

chain = classification_prompt | structuredllm


def classify(message: str):
    return chain.invoke({"message": message})


def classify_with_self_consistency(message: str, attempts: int = 2):
    results = []

    for _ in range(attempts):
        result = classify(message)
        results.append(result)

    categories = [result.category for result in results]

    majority_category = Counter(categories).most_common(1)[0][0]

    return majority_category, results
