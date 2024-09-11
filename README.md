# Azure AI Inference API Workshop

This repository contains the materials for running a beginner-friendly workshop on the Azure AI Inference API. It is designed to be self-paced and contains links to documentation and code samples for hands-on exploration of the topic.

## 1. Model Choice Matters

Building generative AI applications requires developers to have a good understanding of the diverse models and capabilities available to them, and tools and techniques that can help them choose the right model for their application requirements. But developers face three key challenges when making model choices:

1. **Discovery** - How can they _find_ suitable models for their cost (budget), category (task) or capability (features) requirements.
1. **Evaluation** - How can they _assess_ models to find the best fit for those requirements among the suitable choices?
1. **Iteration** - How can they _swap_ models later to adapt to changing needs or new capabilities, without significant rework?

The Azure AI Platform addressess these with three key features:
 - **[Azure AI Model Catalog](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)** - to facilitate discovery.
 - **[Azure AI Model Benchmarks](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/model-benchmarks)** - to compare model choices.
 - **[Azure AI Inference API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python)** - to abstract code complexity.

**👩🏽‍💻 `DEMO`** | Explore Azure AI Studio As Guest. 

## 2. Common API for Code-First Development

Building generative AI applications requires interacting with foundational models - and orchestrating multi-model workflows - to execute complex tasks. Modern LLM Ops involves a 3-phase app lifecycle:

 - **ideation** - where we build a proof of concept
 - **augmentation** - where we evaluate & iterate for response quality
 - **operationalization** - where we deploy & monitor for real-world use

Building custom applications requires a **code-first** approach where we can tailor all elements of this lifecycle - from prompt to production. 

The **model choice** challenge developers now face comes in the form of diverse APIs and SDKs that they will need to learn, implement, and debug, to work with these models. And, the challenge increases with each iteration if they need to swap models or experiment with new capabilities.

The **common API** approach tackles complexity by _abstracting_ "core" operations into a base interface and _adapting_ it to the custom API by:

 - implementing common features where possible
 - throwing controlled exceptions where not possible
 - extending with extra parameters to support custom features

## 3. Azure AI Inference API

The [Azure AI Model Inference API](https://learn.microsoft.com/azure/machine-learning/reference-model-inference-api) provides this common API for a growing subset of foundation models provided in the Azure AI Model catalog.
- The API is implemented in multiple languages (Python, C#, JS)
- It works with both managed and serverless model deployments
- It works with GitHub Marketplace Models & LlamaIndex (local)

Getting started with the API involves these steps:

1. **Discovery** - Azure AI Model Catalog, GitHub Marketplace, LlamaIndex
1. **Deployment** - get hosted or local endpoint (and API key) for model
1. **Development** - install the Azure AI Inference API library and use it
1. **Iteration** - evaluate & swap models  with minimal code changes

## 4. Learning Objectives

The objectives of this workshop are to help you get familiar with the Azure AI Model Inference API capabilities and usage with hands-on exercises. By the end of this workshop, you should be able to:
 - Describe the Azure AI Inference API
 - Discover & deploy models in Azure AI Studio
 - Discover & deploy models in GitHub Marketplace
 - Use deployed models with the Azure AI Inference API
 - Swap deployed models with minimal code changes
 - Handle exceptions (when models don't support a feature)
 - Explore extensions (when models offer extra parameters)
 - Explore usage with diverse inference tasks (categories)
 - Explore usage with diverse model providers (collections)
 - Explore usage with managed and serverless deployments
 - Explore support for responsible AI with content safety tooling
 - Explore usage for rapid prototyping with observability (Prompty)
 - Explore usage with locally hosted models (using LLamaIndex)

## 5. Pre-Requisites

- Python 3.8 or higher
- Azure Account (with subscription or PAYG billing)
- GitHub Account (with access to Codespaces, Marketplace)
- Familiarity with Visual Studio Code, Python
- Model Deployments (Azure, GitHub or LlamaIndex)


## 6. Quick Start

1. Fork this repo and launch in Codespaces
1. Run `mkdocs serve` to view workshop guide
1. Follow the guide to complete the exercises


## 7. Related Resources

1. Docs - [Azure AI Model Inference API](https://learn.microsoft.com/azure/machine-learning/reference-model-inference-api) 
1. Docs - [Azure AI Inference Library (Python)](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-inference-readme) 
1. Docs - [AI Model Inferene Package (Python)](https://learn.microsoft.com/python/api/azure-ai-inference/azure.ai.inference) 
1. Repo - [Azure AI Inference Samples (Python)](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples) 
1. Docs - [Deploy models .. with Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/concepts/deployments-overview)
- Video - [Accelerate your AI Journey with Azure AI Model Catalog](https://build.microsoft.com/en-US/sessions/6809f536-19ee-4b8d-aa06-dfde657c6b90?source=sessions)
- Slides - [Accelerate your AI Journey with Azure AI Model Catalog](https://medius.microsoft.com/video/asset/PPT/c8af97e4-0dc5-4eee-b2fe-1f15be58bab7)

## 8. FAQ & Troubleshooting
TBD