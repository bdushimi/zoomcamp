from elastic_client import search

def search_with_filters(query_text, course=None, section=None, size=3):
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
    
    # Add section filter if specified
    if section:
        must_conditions.append({
            "term": {
                "section": section
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
    
    response = search(index_name, search_query)
    
    # Print results
    print(f"\nFound {response['hits']['total']['value']} matches:")
    for hit in response['hits']['hits']:
        print(f"\nScore: {hit['_score']}")
        print(f"Course: {hit['_source'].get('course', 'N/A')}")
        print(f"Section: {hit['_source'].get('section', 'N/A')}")
        print(f"Question: {hit['_source'].get('question', 'N/A')}")
        print(f"Text: {hit['_source'].get('text', 'N/A')}")
    
    return response

if __name__ == "__main__":
    # Example 1: Search with course filter
    print("\n=== Example 1: Search in machine-learning-zoomcamp ===")
    search_with_filters(
        query_text="How do copy a file to a Docker container?",
        course="machine-learning-zoomcamp"
    )
    
    # Example 2: Search with section filter
    print("\n=== Example 2: Search in specific section ===")
    search_with_filters(
        query_text="How do copy a file to a Docker container?",
        section="Docker"
    )
    
    # Example 3: Search with both filters
    print("\n=== Example 3: Search with both filters ===")
    search_with_filters(
        query_text="How do copy a file to a Docker container?",
        course="machine-learning-zoomcamp",
        section="Docker"
    ) 