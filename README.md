# LLM Course FAQ System

This project implements a FAQ system using Elasticsearch and OpenAI's GPT models. It demonstrates various concepts related to LLM applications, including document search, prompt engineering, and token counting.

## Prerequisites

- Python 3.x
- Elasticsearch running locally (default: http://localhost:9200)
- Required Python packages:
  ```bash
  pip install elasticsearch tiktoken
  ```

## Project Structure

### Core Files

1. `elastic_client.py`
   - Handles connection to Elasticsearch
   - Provides search functionality
   - Usage: Import and use the `search` function to query Elasticsearch

2. `query_filtering.py`
   - Implements search with filters (course and section)
   - Demonstrates how to build complex Elasticsearch queries
   - Usage:
     ```python
     from query_filtering import search_with_filters
     
     # Search with course filter
     results = search_with_filters(
         query_text="your question",
         course="machine-learning-zoomcamp"
     )
     
     # Search with section filter
     results = search_with_filters(
         query_text="your question",
         section="Docker"
     )
     ```

3. `build_prompt.py`
   - Builds context-aware prompts for LLM
   - Combines search results with user questions
   - Usage:
     ```python
     from build_prompt import build_prompt, search_documents, build_context
     
     # Search and build prompt
     response = search_documents(query_text="your question")
     context = build_context(response)
     prompt = build_prompt(question="your question", context=context)
     ```

4. `token_count.py`
   - Demonstrates token counting using tiktoken
   - Shows how to analyze token usage in prompts
   - Usage:
     ```python
     python token_count.py
     ```

## Example Questions and Answers

### Q6: Tokens
To answer the question about token counting:
1. Run `token_count.py` to see how many tokens are in the generated prompt
2. The script will show:
   - The full prompt text
   - Total number of tokens
   - Token-by-token breakdown

### Other Questions
For other questions in the course, you can:
1. Use `query_filtering.py` to search the FAQ database
2. Use `build_prompt.py` to generate context-aware prompts
3. Use `token_count.py` to analyze token usage

## Running the Code

1. Ensure Elasticsearch is running locally
2. Install required packages
3. Run individual scripts as needed:
   ```bash
   python query_filtering.py  # Test search with filters
   python build_prompt.py     # Test prompt generation
   python token_count.py      # Test token counting
   ```

## Notes

- The system uses Elasticsearch for document search
- Prompts are built using a template that includes context from search results
- Token counting is done using tiktoken for GPT-4
- The system supports filtering by course and section 