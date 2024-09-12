import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# For Serverless API or Managed Endpoint
# client = ChatCompletionsClient(
#    endpoint=os.environ["AZUREAI_ENDPOINT_URL"],
#    credential=AzureKeyCredential(os.environ["AZUREAI_ENDPOINT_KEY"]),
#)

# For GitHub Models
# https://github.com/marketplace/models
github_token=os.environ["GITHUB_TOKEN"]
client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(github_token),
    model="mistral-large" # Update as needed. Alternatively, you can include this is the `complete` call.
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="How many languages are in the world?"),
    ]
)

print(response.choices[0].message.content)