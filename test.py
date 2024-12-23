# test_ollama.py

from langchain_ollama import OllamaLLM  # Updated import as per deprecation warning

# Initialize the local Ollama model
llm = OllamaLLM(
    base_url="http://localhost:11434",  # Ollama local server URL
    model="llama3.2:1b",  # Specify the model
    verbose=True  # Enable verbose logging
)

def test_ollama(prompt):
    """
    Test function to send a prompt to the Ollama model and print the response.
    """
    try:
        print(f"Sending prompt: {prompt}")
        response = llm.invoke(prompt)  # Updated to use `invoke` method
        print("Response:")
        print(response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Test prompt
    test_prompt = "What are the key features of AI models like GPT?"
    test_ollama(test_prompt)
