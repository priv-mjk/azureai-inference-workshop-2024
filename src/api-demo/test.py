import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

# Retrieve the endpoint and key from environment variables
endpoint = os.environ["AZUREAI_ENDPOINT_URL"]
key = os.environ["AZUREAI_ENDPOINT_KEY"]

# Initialize the client
client = ChatCompletionsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Test the connection with a simple request
response = client.complete(
    model="gpt-4o-mini",  # Replace with your model name
    messages=[{"role": "user", "content": "Hello, Azure AI!"}]  # Add the messages argument
)

print(response)