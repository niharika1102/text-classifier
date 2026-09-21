from langchain_core.prompts import PromptTemplate

classification_prompt = PromptTemplate.from_template(
    """
    You are a customer support agent. 

    Classify the messages into exactly one of these categories:
    - Complaint
    - Query
    - Feedback
    - Request

    Message: 
    {message}
    """
)