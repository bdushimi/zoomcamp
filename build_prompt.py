from elastic_client import search
from query_filtering import search_with_filters

def search_documents(query_text, course=None, size=3):
    index_name = "faq"
    
    # Build the bool query
    must_conditions = [
        {
            "multi_match": {
                "query": query_text,
                "fields": ["question^4", "text"],
                "type": "best_fields"
            }
        }
    ]
    
    # Add course filter if specified
    if course:
        must_conditions.append({
            "term": {
                "course": course
            }
        })
    
    search_query = {
        "query": {
            "bool": {
                "must": must_conditions
            }
        },
        "size": size
    }
    
    return search(index_name, search_query)

def build_context(response):
    context_entries = []
    for hit in response['hits']['hits']:
        context_entry = f"""Q: {hit['_source'].get('question', 'N/A')}
A: {hit['_source'].get('text', 'N/A')}"""
        context_entries.append(context_entry)
    
    return "\n\n".join(context_entries)

def build_prompt(question, context):
    return f"""You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}"""

if __name__ == "__main__":
    # Search for relevant documents using query_filtering logic
    response = search_with_filters(
        query_text="How do copy a file to a Docker container?",
        course="machine-learning-zoomcamp"
    )
    
    # Build context from search results
    context = build_context(response)
    
    # Build the final prompt
    prompt = build_prompt(
        question="How do I execute a command in a running docker container?",
        context=context
    )
    
    print("\n=== Generated Prompt ===")
    print(prompt)
    print(f"\nPrompt length: {len(prompt)} characters") 