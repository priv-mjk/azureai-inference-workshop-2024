# 2. Setup

!!! tip "Dev Containers - Configuration As Code"

    This repository is configured with a dev container that sets up all dependencies **for the Python Inference SDK**. Simply fork the repo, launch Codespaces and start exploring. To set up your dev environment manually, or with a different language SDK, [follow these instructions](https://learn.microsoft.com/en-us/azure/machine-learning/reference-model-inference-api?view=azureml-api-2&tabs=python#inference-sdk-support). The Azure AI Model Inference API supports Python, JavaScript, C# and REST API calls.

## 1. Deploy a Model

Deploy a **supported** model from the Azure AI Model Catalog, to Azure AI Studio. This can be a Serverless API or Managed Compute deployment option.

> 🌟 | MODEL CATALOG DEMO

## 2. Setup Dev Env

You will need the deployment details of your model above.

```bash
# Install package if needed
pip install azure-ai-inference

# Set these environment variables in terminal
export AZUREAI_ENDPOINT_URL="your-endpoint-url"
export AZUREAI_ENDPOINT_KEY="your-endpoint-key"

```

**Alternatively** you can set them via an `.env` file:

```bash
# Copy the sample .env and populate values
cp .env.sample .env

# Set those env vars in your terminal
set +a; source .env; set -a
```

## 3. Run the Sample Code

This code is in the `src/demo/first-prompt.py` file in this repo. 

```python
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

client = ChatCompletionsClient(
    endpoint=os.environ["AZUREAI_ENDPOINT_URL"],
    credential=AzureKeyCredential(os.environ["AZUREAI_ENDPOINT_KEY"]),
)
response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="How many languages are in the world?"),
    ]
)

print(response.choices[0].message.content)

```

Open 3 terminals. In each, set the default variables to a different model. Run the code to see the difference.

```bash
python src/demo/first-prompt.py
```

Note the differences in quality, length and other characteristics of the responses.

## 4. Try Richer Samples

The Azure SDK For Python has an [extensive number of samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples) that you can use, to get a sense of the different API capabilities.

Let's try a few of them here (and get a sense of how you can setup to run others in the same sandbox).

| Sample | Description |
| --- | --- |
| 01_chat_completions.py | One chat completion operation using a synchronous client. |
| 02_chat_completions_streaming.py | One chat completion operation using a synchronous client and streaming response. |
| 03_chat_completions_model.py | Chat completions with additional model-specific parameters. |

## 5. Try GitHub Models

1. [Authenticate with GitHub Token](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference#create-and-authenticate-a-client-directly-using-api-key-or-github-token) in Azure Inference API client.
2. [Try GitHub MarketPlace](https://github.com/marketplace/models) with Playground or SDK
3. [Use Prompty With Serverless](https://github.com/microsoft/prompty/tree/33201d8af11b8d595a3380e268a08f9ffb87ebe5/runtime/prompty/tests/prompts) for prompt engineering

## 6. Try Prompty Assets

Let's try a Serverless Prompty