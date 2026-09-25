# AI Text Classifier & Explainer

A small AI application that classifies customer support messages using
few-shot prompting, structured LLM output, and self-consistency.

## What this project demonstrates

- Few-shot prompting
- In-context learning
- Structured output with Pydantic
- LangChain LCEL
- Gemini LLM integration
- Self-consistency
- FastAPI
- Request/response validation with Pydantic

## Architecture

```text
Client
  ↓
FastAPI
  ↓
Pydantic Request Validation
  ↓
Few-Shot Prompt
  ↓
LangChain
  ↓
Gemini
  ↓
Structured Pydantic Output
  ↓
Self-Consistency
  ↓
Majority Vote
  ↓
API Response