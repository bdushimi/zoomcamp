from elastic_client import search

def search_documents(query_text):
    index_name = "faq"
    search_query = {
        "query": {
            "multi_match": {
                "query": query_text,
                "fields": ["question^4", "text"],
                "type": "best_fields"
            }
        }
    }
    
    response = search(index_name, search_query)
    
    # Print results
    print(f"\nFound {response['hits']['total']['value']} matches:")
    for hit in response['hits']['hits']:
        print(f"\nScore: {hit['_score']}")
        print(f"Course: {hit['_source'].get('course', 'N/A')}")
        print(f"Question: {hit['_source'].get('question', 'N/A')}")
        print(f"Text: {hit['_source'].get('text', 'N/A')}")
        if 'section' in hit['_source']:
            print(f"Section: {hit['_source']['section']}")

if __name__ == "__main__":
    query = "How do execute a command on a Kubernetes pod?"
    search_documents(query) 