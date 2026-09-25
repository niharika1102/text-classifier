from fastapi import FastAPI

from app.classifier import classify_with_self_consistency
from app.schemas import ClassificationRequest

app = FastAPI()


@app.post("/classify")
def classify_message(request: ClassificationRequest):

    category, results = classify_with_self_consistency(request.message)

    return {"category": category, "results": results}
