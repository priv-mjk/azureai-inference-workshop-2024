# Introduction

!!! tip "Azure AI Model Inference API - 5 Resources To Start With"
    
    1. [Browse the Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/reference-model-inference-api?)
    1. [Explore the Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples)
    1. Sep 2024: [#RAGHack - Pick the Right Model For The Right Job](https://developer.microsoft.com/reactor/events/23433/)
    1. Aug 2024: [What's New with Azure AI Model Inference API](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/expanding-the-azure-ai-model-inference-api-integrating-azure-ai/ba-p/4212883)
    1. May 2024: [Accelerate your AI Journey with Azure AI Model Catalog](https://build.microsoft.com/en-US/sessions/6809f536-19ee-4b8d-aa06-dfde657c6b90?source=sessions)


## 1. What is this API?

!!! example "[From the Docs](https://learn.microsoft.com/en-us/azure/machine-learning/reference-model-inference-api?view=azureml-api-2&tabs=python)"
    The Azure AI Model Inference is an API that exposes a common set of capabilities for foundational models and that can be used by developers to consume predictions _from a diverse set of models in a uniform and consistent way_. Developers can talk with different models deployed in Azure AI Studio without changing their underlying code!

Another way to think about it is that it is a _model wrapper_ that abstracts frequently-used model capabilities into a **common API** that applications can interact with, for a consistent developer experience, independent of the specific model implementing them.

- It **throws exceptions** cleanly if the underlying model lacks a specific API feature.
- It **supports extensibility** by "passing through" custom parameters for model-unique features.

This allows us to _explore model choice_ with the same codebase, simply by swapping the model deployment details in the configuration or environment - without changing the application code. We can also _compare models_ side-by-side, by running the same code in different terminals, to contrast quality of responses or performance of execution.


## 2. Why should we use it?

Building generative AI applications requires rapid prototyping and ideation, with the ability to make decisions like _model selection_, _model configuration_, _prompt template design_ and _orchestration framework_ in a flexible way. The API provides an abstraction layer between application code and model invocation interface, allowing us to evolve each side independently. This lets us do the following:

1. **Rapid Ideation** - Quickly prototype against the API, then explore diverse models for best fit.
1. **Design Flexibility** - Build for common capabilities, and extend to custom features if present.
1. **Deploy Flexibility** - Works with Managed Compute and Serverless API model deployments.
1. **Ecosystem Expansion** - Growing partner list e.g, GitHub Marketplace Models, LlamaIndex.
1. **Prompty Enabled** - Prompt asset & runtime for rapid prototyping, works out-of-the-box.

## 3. Where could we use it?

Use it in any situation where you think **model choice matters**. For instance, _"you have a specific cost or performance target and want to see if an alternative model offers better trade-offs"_. The API lets you swap in alternative models without changing the application code, and compare the results side-by-side to make effective decisions. For example,

1. **Performance optimization** - swap downstream "bottleneck" models for faster ones.
1. **Cost optimization** - scale down to cheaper models when justified (e.g., traffic lulls)
1. **Multi-model composition** - use different API endpoints for orchestrated flows (agentic, RAG)

## 4. How would we use it?

The [current version](https://learn.microsoft.com/en-us/azure/machine-learning/reference-model-inference-info?view=azureml-api-2) of the Azure AI Model Inference API supports the following endpoints, reflecting the types of inference tasks exposed using a common API. See these in action in the _Quickstart_ section of this lab.

1. **Get Info** - about underlying model
1. **Text Embeddings** - generate vectors from text
1. **Image Embeddings** - generate vectors from images and text
1. **Text Completion** - single turn model response (for prompt)
1. **Chat Completion** - multi-turn model response (for conversation)

The [API samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples) showcase both _sync client_ and _async client_ usage patterns.

---

[**Next**](./1-setup.md) - Setup Environment