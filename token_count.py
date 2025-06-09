import tiktoken
from build_prompt import build_prompt, search_documents, build_context

def count_tokens(text):
    # Get the encoding for GPT-4
    encoding = tiktoken.encoding_for_model("gpt-4")
    
    # Encode the text and count tokens
    tokens = encoding.encode(text)
    token_count = len(tokens)
    
    # Print the results
    print(f"Text: {text}")
    print(f"Number of tokens: {token_count}")
    print("\nToken breakdown:")
    for token in tokens:
        print(f"Token {token}: {encoding.decode_single_token_bytes(token)}")
    
    return token_count

if __name__ == "__main__":
    # Search for relevant documents
    response = search_documents(
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
    
    # Count tokens in the generated prompt
    count_tokens(prompt) 