from pydantic import BaseModel, Field


class ClassificationRequest(BaseModel):
    message: str


class ClassificationResult(BaseModel):
    category: str = Field(description="The category of the customer message")
    reason: str = Field(
        description="A short explanation for why the message belongs to this category"
    )
