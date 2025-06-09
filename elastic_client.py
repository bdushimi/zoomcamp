from elasticsearch import Elasticsearch
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a single Elasticsearch client instance with minimal configuration
try:
    es = Elasticsearch(
        "http://localhost:9200",
        verify_certs=False,
        headers={"Accept": "application/vnd.elasticsearch+json; compatible-with=8"}
    )
    # Test the connection
    info = es.info()
    logger.info(f"Successfully connected to Elasticsearch version {info['version']['number']}")
except Exception as e:
    logger.error(f"Error connecting to Elasticsearch: {str(e)}")
    raise

def get_client():
    """Returns the Elasticsearch client instance"""
    return es

def create_index(index_name, mappings):
    """Creates an index with the given mappings"""
    try:
        # First check if we can connect
        es.info()
        
        # Then try to create the index
        if es.indices.exists(index=index_name):
            logger.info(f"Deleting existing index: {index_name}")
            es.indices.delete(index=index_name)
        
        logger.info(f"Creating index: {index_name}")
        es.indices.create(index=index_name, body=mappings)
        logger.info("Index created successfully")
    except Exception as e:
        logger.error(f"Error creating index: {str(e)}")
        raise

def index_document(index_name, document):
    """Indexes a single document"""
    try:
        es.index(index=index_name, document=document)
    except Exception as e:
        logger.error(f"Error indexing document: {str(e)}")
        raise

def search(index_name, query):
    """Performs a search query"""
    try:
        return es.search(index=index_name, body=query)
    except Exception as e:
        logger.error(f"Error performing search: {str(e)}")
        raise 