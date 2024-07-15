# Welcome Learners!

## 1. Motivation
Building generative AI applications involves working with a wide range of language models from diverse providers.

 - Language models can be large (LLM) or small (SLM) in terms of model size and complexity.
 - Models can be proprietary (e.g., GPT-4 from OpenAI) or open-source (e.g., GPT-2 from HuggingFace).
 - Models can differ in their capabilities (text generation, embedding) and API features (config parameters, system prompt, stop words etc.)

This creates a challenge for AI application developers when interacting with these models - particularly when they want to evaluate diverse models, or switch to a different model later.

## 2. Introduction 
The [Azure AI Model Inference API](https://learn.microsoft.com/azure/machine-learning/reference-model-inference-api) tries addresses this challenge by providing a **unified API** that abstracts the differences between the various models into common API calls for convenience - while providing _extensibility_ to support model-specific features.

Developers can now focus on building their applications for a _specific capability_ without worrying about how that capability is implemented in a specific model instance.


## 3. Learning Objectives

In this workshop, we'll explore the Azure AI Model Inference API from core concepts to applied usage with various models and inference tasks. 

By the end of the workshop you should be able to:

1. Describe the Azure AI Inference API capabilities
1. Describe the benefits of using the unified API
1. Configure your application to use the unified API
1. Use Inference API with diverse deployed models
1. Ensure responsible AI with content safety tooling 

## 4. Pre-Requisites

- Python 3.8 or higher
- Azure Subscription
- Model Deployments (Azure AI Studio)
- Authentication Credentials

Model deployments will have default _key, endpoint, region_ properties.

- Use endpoint for initializing the inference API library.
- Use key to create a traditional authentication credential if preferred.
- Alternatively, use Microsoft Entra ID (32-character string) for a secure managed identity solution.


Check out the [samples README](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-inference/README.md#prerequisites) for updated requirements.



## 5. Supported Models

Currently, we can deploy models in the Azure AI platform in one of two ways:

 - **Managed Compute Endpoints** - using Models as a Platform (MaaP) with subscription based pricing for [_managed inference_](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2) capability.
 - **Serveless API Endpoints** - using Models As a Service (MaaS) with token-based billing for [_pay as you go_](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-serverless?view=azureml-api-2&tabs=azure-studio) inference capability.
 
Currently [only a subset of these models are available](https://learn.microsoft.com/en-us/azure/machine-learning/reference-model-inference-api?view=azureml-api-2&tabs=python#availability) for use with the Azure AI Inference API.

| Azure Inference API | Managed | Serverless |
|:---|:---|:---|
| Cohere Embed V3 family | - | ✅|
| Cohere Command R  family| - | ✅|
| Meta LLama 2 chat family|  - | ✅|
| Meta Llama 3 instruct family |  ✅ | ✅|
| Phi-3 family |  ✅ | ✅|
| Mistral-Small | - | ✅|
| Mistral-Large |  - | ✅|
| Mixtral family |  ✅ | ✅|
| | |


## 6. Related Resources

1. Docs - [Azure AI Model Inference API](https://learn.microsoft.com/azure/machine-learning/reference-model-inference-api) 
1. Docs - [Azure AI Inference Library (Python)](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-inference-readme) 
1. Docs - [AI Model Inferene Package (Python)](https://learn.microsoft.com/python/api/azure-ai-inference/azure.ai.inference) 
1. Repo - [Azure AI Inference Samples (Python)](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples) 
1. Docs - [Deploy models .. with Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/concepts/deployments-overview)
- Video - [Accelerate your AI Journey with Azure AI Model Catalog](https://build.microsoft.com/en-US/sessions/6809f536-19ee-4b8d-aa06-dfde657c6b90?source=sessions)
- Slides - [Accelerate your AI Journey with Azure AI Model Catalog](https://medius.microsoft.com/video/asset/PPT/c8af97e4-0dc5-4eee-b2fe-1f15be58bab7)

## 7. Get Started

You are hopefully viewing this page in the preview editor or browser. To get started, just move to the next section of this guide as seen in the sidebar.
