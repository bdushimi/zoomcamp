from get_faq_data import get_faq_documents
from index_data import index_documents

if __name__ == "__main__":
    # Get and index documents
    documents = get_faq_documents()
    index_documents(documents) 