# Exploring OpenAI Models

The OpenAI API provides a comprehensive way to access state-of-the-art AI models for natural language processing, image generation, semantic search and speech recognition [for developers](https://platform.openai.com/docs/quickstart). 

## 1. Model Families & Versions

## 2. Model Deployment Options

Want to start exploring these? You have three options for the deploying the _foundation_ OpenAI models. Once deployed, you will need the right _authentication_ credential for that provider, to access the model from code.

| Provider | Description | Auth|
| --- | --- |--- |
| OpenAI Deployment |  Sign up for developer access with the pay-as-you-go plan on the OpenAI platform. [Create an API key](https://platform.openai.com/docs/quickstart/create-and-export-an-api-key) and export it to an `OPENAI_API_KEY` environment variable that gets used by the default `openai` Python package. Then [explore samples](https://platform.openai.com/docs/quickstart?language-preference=python) with code. | `OPENAI_API_KEY` (project)|
| Azure OpenAI Deployment | Get an active Azure subscription with permissions to create or use an Azure AI hub resource (requires a user role of Azure AI Developer, Contributor, or Owner). Then [deploy an Azure OpenAI model](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-openai) and explore the [playground quickstart](https://learn.microsoft.com/en-us/azure/ai-studio/quickstarts/get-started-playground) or the [code-first quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line%2Ctypescript%2Cpython-new&pivots=programming-language-python) to try your first chat application. | Azure Managed Identity |
|GitHub Model Marketplace | You can [find and experiment with AI models for free](https://docs.github.com/en/github-models/prototyping-with-ai-models) using a personal access token on GitHub. Then just switch the token to a paid Azure account to move from prototyping to production. **The playground is [rate limited](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits)**.|`GITHUB_TOKEN` (personal access token) |

Note that the GitHub Model Marketplace uses Azure AI deployments of these models under the hood, so you will see an endpoint in the form `https://models.inference.ai.azure.com` with the deployed model identified in a `model` parameter passed into the API call. 

## 3. Model Usage Options

Based on the provider, you can use deployed models in three ways:

1. **Playground** - no-code option for interactive prompt engineering.
1. **Provider SDK** - code-first option with provider SDK (e.g., `openai` Python library)
1. **Azure AI Inference SDK** - code-first option with common API (provider--agnostic)

The Azure AI Inference API is influenced by the OpenAI API syntax and capabilities so the transition from OpenAI SDK to Azure AI Model Inference SDK may feel more seamless.

Note that the GitHub Model Marketplace has samples for both the provider-specific SDK (where this exists) and the Azure AI Model Inference SDK (for all listed models) to help you get started.


## 4. Ideation with Prompty

[Prompty](https://www.prompty.ai/docs) isn an _asset class and format_ for LLM prompts that is designed to enhance observability, understandability, and portability. Let's break this down:

??? info "What is an Asset Class?"

    - A [digital asset](https://business.adobe.com/blog/basics/digital-asset-management#what-is-a-digital-asset) is any type of mediat or data that is stored in a digital format. This includes images, videos, audio, documents, web pages, and code files.
    - An _asset class_ is a group of assets that share similar characteristics, such as the type of media or the purpose of the asset.
    - A _prompty asset_ is a digital asset that is designed to be used as a prompt template for a large language model. It uses a `.prompty` extension with a schema that adheres to the [Prompty Specification](https://www.prompty.ai/docs/prompty-specification), defined in YAML.

??? info "What does Asset Portability mean?"

    - Prompty assets are agnostic to underlying models, programming languages, and frameworks. You can use the same prompt template (content) and _configure_ just the metadata (frontmatter) to switch models.
    - Prompty tooling and runtime can then _activate_ the asset and convert it to language-specific or framework-specific code for execution. Developers can use built-in runtime options, or create custom runtimes for their needs.

??? info "What does Asset Understandability mean?"

    - Prompty files are written in Markdown-like syntax, making them readable by default.
    - The _frontmatter_ section of a Prompty file contains metadata about the prompt, such as the model to use, the types of inputs and outputs expected, and the name, description, and authors, for that template.
    - The _template_ section of the Prompty file contains the content for enhancing the default user prompt ("question"). This includes the _system_ context, _instruction_ context and _documentation_ context for prompt engineering.

??? info "What does Asset Observability mean?"

    - The Prompty runtime (library) comes with built-in support for tracing, generating logs in OpenTelemetry-compliant formats in the console, or as stored JSON files.
    - The Prompty extension (tool) provides a viewer that loads the tracer logs and displays them in an interactive UI, allowing developers to see the execution flow of the prompt and the performance metrics for each step.

Prompty currently supports different model deployments, using relevant _prompty invokers_ that understand how to interact with that specific provider and deployment endpoint.

??? info "OpenAI Model Invoker - for OpenAI deployments"

    ```yaml
    openaiModel:
    type: object
    description: Model used to generate text
    properties:
      type:
        type: string
        description: Type of the model
        const: openai
      name:
        type: string
        description: Name of the model
      organization:
        type: string
        description: Name of the organization
    additionalProperties: false
    ```

??? info "Azure OpenAI Model Invoker - for Azure OpenAI deployments"

    ```yaml
    azureOpenaiModel:
    type: object
    description: Model used to generate text
    properties:
      type:
        type: string
        description: Type of the model
        const: azure_openai
      api_version:
        type: string
        description: Version of the model
      azure_deployment:
        type: string
        description: Deployment of the model
      azure_endpoint:
        type: string
        description: Endpoint of the model
    additionalProperties: false
    ```
    
??? info "Serverless Model Invoker - for MaaS, GitHub Model Markeplace deployments"

    ```yaml
    maasModel:
    type: object
    description: Model used to generate text
    properties:
      type:
        type: string
        description: Type of the model
        const: azure_serverless
      azure_endpoint:
        type: string
        description: Endpoint of the model
    additionalProperties: false
    ``` 

In the last case, it uses the Azure AI Model Inference API under the hood.