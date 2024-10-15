# Resources

### 1. API Reference:

| API Endpoint | Description |
| --- | --- |
|[/info](https://learn.microsoft.com/en-us/azure/ai-studio/reference/reference-model-inference-info) | Returns the information about the model deployed under the endpoint.|
| [/embeddings](https://learn.microsoft.com/en-us/azure/ai-studio/reference/reference-model-inference-embeddings) | Creates an embedding vector representing the input text. |
| [/completions](https://learn.microsoft.com/en-us/azure/ai-studio/reference/reference-model-inference-completions)| Creates a completion for the provided prompt and parameters (think request-response) |
| [/chat/completions](https://learn.microsoft.com/en-us/azure/ai-studio/reference/reference-model-inference-chat-completions)| Creates a model response for the given chat **conversation**. (think multi-turn with history) |
| [/images/embeddings](https://learn.microsoft.com/en-us/azure/ai-studio/reference/reference-model-inference-images-embeddings)|Creates an embedding vector representing the input image and text pair. |
|||


### 2. Documentation

!!! tip "The inference API is currently supported with SDKs for Python, JavaScript, C# and REST API calls."

1. [Azure AI Model Inference API](https://learn.microsoft.com/en-us/azure/ai-studio/reference/reference-model-inference-api?tabs=python) - Main documentation page for the API



### 3. Code Samples

!!! info "Samples can be used with _Serverless API_ and _Managed Compute_ model deployments. All samples use Python and depend on the `azure-ai-inference` library, with the async samples also requiring the `aiohttp` library."

1. [17 Samples](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-inference/samples/README.md#chat-completions) using sync client with chat completions endpoint
1. [4 Samples](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-inference/samples/README.md#text-embeddings) using sync client with embeddings endpoint
1. [6 Samples](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-inference/samples/README.md#chat-completions-1) using async client with chat completions endpoint
1. [1 Samples](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-inference/samples/README.md#text-embeddings-1)  using async client with embeddings endpoint
