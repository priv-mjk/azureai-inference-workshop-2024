# 2. Deploy Models For Usage

To try the Azure AI Inference API, we first need to deploy **relevant models** to Azure so we can interact with them. Currently, the API is available for use with [the following models](https://learn.microsoft.com/en-us/azure/machine-learning/reference-model-inference-api?view=azureml-api-2&tabs=python#availability) - where the list is defined in two categories:
 - Deploy to [Serverless API endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-serverless?view=azureml-api-2) - pay as you go.
 - Deploy to [Managed Compute endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2) - subscription needed.

## 2.1 Deployment Guides

There are multiple guides for deployment:
- [Deploy to Managed endpoint](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2&tabs=cli) - from Azure ML Studio or SDK
- [Deploy to Serverless endpoint](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-serverless?view=azureml-api-2&tabs=azure-studio) - from Azure ML Studio, CLI or SDK
- [Deploy with Azure AI Studio](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-open) - serverless or managed, with code

## 2.2 Supported Models

Deploying a model to either a serverless API endpoint or a managed compute endpoint **using code**, requires us to know the _Model ID_. You can find this using one of the following guides based on the type of deployment as linked below:
 - [Get the Model ID for Serverless Endpoint deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-open#get-the-model-id) 
 - [Get the Model ID for Managed Compute Endpoint deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-open#get-the-model-id-1) 

For now, the Azure AI Inference API supports **only a subset of these model/type combinations**. The [documentation](https://learn.microsoft.com/en-us/azure/machine-learning/reference-model-inference-api?view=azureml-api-2&tabs=python#availability) provides direct links to the relevant docs for deployment:
- Cohere Embed V3 - [Serverless EP](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-cohere-embed?view=azureml-api-2) 
- Cohere Command R - [Serverless EP](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-cohere-command?view=azureml-api-2) 
- Meta Llama 2 chat - [Serverless EP](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-llama?view=azureml-api-2) 
- Meta Llama 3 instruct - [Serverless EP](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-llama?view=azureml-api-2) - [Managed EP](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-llama?view=azureml-api-2)
- Mistral-Small - [Serverless EP](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-mistral?view=azureml-api-2) 
- Mistral-Large - [Serverless EP](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-mistral?view=azureml-api-2)
- Phi-3 - [Serverless EP](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2) - [Managed EP](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2)
- Mixtral - Managed EP(??)

## 2.3 Explore Basic Samples

The [Azure Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples) for the Azure AI Inference API provides a number of runnable Python scripts that you can test against both serverless and managed endpoints. To try this out you will need to: