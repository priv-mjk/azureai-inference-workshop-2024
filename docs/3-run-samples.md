# Run Sample Scripts

To run these scripts, make sure you set the following environment variables in your VS Code terminal - with the values for the deployed model endpoint (URL) and key (API key).

```bash
export AZURE_AI_CHAT_ENDPOINT=
export AZURE_AI_CHAT_KEY=
```

**Attribution** | All these script examples were copied from the [official samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples) repository, and adapted for use with a workshop format.

---


### Chat completions

|**File Name**|**Description**|
|----------------|-------------|
|[Chat Completion](./../src/01_chat_completions.py) | One chat completion operation using a synchronous client and streaming response. | 
|[Streaming Chat Completion](./../src/02_chat_completions_streaming.py) |One chat completion operation using a synchronous client and streaming response. |
| [Chat Completion with Model Extras](./../src/03_chat_completions_model_extras.py)| Chat completions with additional model-specific parameters. (e.g., "Safe prompt" for Mistral |
| | |

### Text embeddings

|**File Name**|**Description**|
|:---|:---|
| [](./../src) | | 
| | |

<!--
### Image embeddings

|**File Name**|**Description**|
|----------------|-------------|
|[sample_image_embeddings_async.py](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-inference/samples/async_samples/sample_image_embeddings_async.py) | One image embeddings operation, on two input images, using an asynchronous client. |
-->
