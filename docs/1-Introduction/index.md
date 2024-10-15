# About

The [Azure AI Model Inference API](https://learn.microsoft.com/en-us/azure/machine-learning/reference-model-inference-api?view=azureml-api-2&tabs=python)  enables developers to make better **model choices** by simplifying the process by which their applications interact with the model APIs.

!!! tip "Read the Documentation"
    
    1. [Azure AI Model Inference API documentation](https://learn.microsoft.com/en-us/azure/machine-learning/reference-model-inference-api?)
    1. [Azure AI Model Inference API Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples)
    1. [Reference API Documentation](https://aka.ms/azsdk/azure-ai-inference/python/reference)
    1. [Blog Post: What's New in Aug 2024](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/expanding-the-azure-ai-model-inference-api-integrating-azure-ai/ba-p/4212883)


## 1️⃣ | What is it?

1. Think of it as a **model wrapper** that abstracts common capabilities of models into a **single API** that applications interact with for a consistent developer experience.
1. The wrapper **adapts** the incoming calls to the custom API for the specific models being used, hiding the differences and complexity from the developer.
1. This allows developers to **swap models** with minimal changes required to application code - enabling model choice for cost and performance optimization.

## 2️⃣ | Why use it?

1. **Rapid Prototyping for Ideation**. Build your prototype quickly against the API, then try it with diverse models for best fit.
1. **Increase Design Flexibility**. Take advantage of API extensibility to start with common capabilities, then add custom features.
1. **Increase Deployment Flexibility** Benefit from API support for both managed compute and serverless API deployments.
1. **Growing Ecosystem Support** Works with new GitHub Marketplace Models (cloud) and LlamaIndex models (local) for flexibility.

## 3️⃣ | Where to use it?

1. **Performance optimization** - for downstream "bottleneck" models.
1. **Cost optimization** - scale down to cheaper models when justified.
1. **Multi-model composition** - chain interactions or orcherstate flows.

## 4️⃣ | How to use it

1. **Get Info** - about underlying model
1. **Text Embeddings** - generate vectors from text
1. **Image Embeddings** - generate vectors from images and text
1. **Text Completion** - single turn model response (for prompt)
1. **Chat Completion** - multi-turn model response (for conversation)


## 5️⃣ | Handling Diversity

The model ecosystem is large and diverse, and evolving rapidly. The wrapped model may **NOT** map exactly onto the common API capabilities - it may lack some features and it may bring other unique ones to the table. The API is designed to handle thi with:

1. **Exceptions** - The API will raise a meaningful exception if the underlying model does not support a specific API feature.
1. **Extensions** - The API has an `extras` field that allows developers to pass through custom parameters to handle model-unique features.