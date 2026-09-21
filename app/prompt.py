from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

example_prompt = PromptTemplate.from_template(
    """
    Message: {message}
    Category: {category}
    """
)

examples = [
    {
        "message": "My order arrived damaged.",
        "category": "Complaint",
    },
    {
        "message": "When will my order arrive?",
        "category": "Query",
    },
    {
        "message": "The delivery was really fast.",
        "category": "Feedback",
    },
    {
        "message": "Please change my delivery address.",
        "category": "Request",
    },
]

classification_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="""
You are a customer support message classifier.

Classify the message into exactly one of these categories:
- Complaint
- Query
- Feedback
- Request""",
    suffix="""

Now classify this message:

Message: {message}

Return only the category.
    """,
    input_variables=["message"],
)
