from elastic_client import create_index, index_document

def index_documents(documents):
    # Create index with mappings
    index_name = "faq"
    mappings = {
        "mappings": {
            "properties": {
                "course": {"type": "keyword"},
                "question": {"type": "text"},
                "answer": {"type": "text"}
            }
        }
    }

    # Create the index
    create_index(index_name, mappings)

    # Index the documents
    for doc in documents:
        index_document(index_name, doc)

    print(f"Indexed {len(documents)} documents") 