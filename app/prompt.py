from langchain_core.prompts import PromptTemplate

classification_prompt = PromptTemplate.from_template(
    """
You are a customer support message classifier.

Classify the message into exactly one of these categories:
- Complaint
- Query
- Feedback
- Request

Examples:

Message: My order arrived damaged.
Category: Complaint

Message: When will my order arrive?
Category: Query

Message: The delivery was really fast.
Category: Feedback

Message: Please change my delivery address.
Category: Request

Now classify this message:

Message: {message}

Return only the category.
    """
)
