# Wildfire AIM - AI Backend

## Overview
Wildfire AIM (AI Mitigation) is a wildfire mitigation and prevention system powered by Microsoft Azure AI Technologies, developed for the AI Innovation Challenge in June 2025.

## AI Backend Architecture

For the AI Backend, we manually set this up through the Azure portal.

We used the Microsoft Learn Tutorial: [Implement Retrieval Augmented Generation (RAG) with Azure OpenAI Service](https://microsoftlearning.github.io/mslearn-openai/Instructions/Exercises/02-use-own-data.html) and grounded the data with files from the `grounding-data/prescribed-burning` folder.

### Grounding Data Sources
Grab the PDF files from the `grounding-data/prescribed-burning` folder and upload them to the Azure portal per the tutorial instructions.

### Overview of set up instructions from the Tutorial:

Step 1: Provision Resources
- Provision an Azure OpenAI resource
- Provision an Azure AI Search resource
- Provision an Azure Storage Account resource

Step 2: Upload your Data

Step 3: Deploy AI models

Step 4: Create an Index
