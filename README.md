# OpenAI EDI Assistant

This repository contains information about creating simple OpenAI EDI Assistants. The assistants are a simple chatbot that can be used to answer questions about Electronic Data Interchange (EDI) using the OpenAI API platform.

All you have to do is create an account on the OpenAI platform: https://platform.openai.com/ and buy some credits

Within this account you create a project (or use the default one) and create an API key.

This sample requires Python 3.10+ and the OpenAI Python package. You can install the OpenAI package by running the following command:
```
pip install openai
```

## Installation
The folder "setup" contains information on setting up the OpenAI objects:
- Assistants (Amanda & Simon): The assistant object that will be used to interact with the OpenAI API using a chat interface
- VectorStore (SteStore & EdiStore): The vector store object that will be used by the assistant to provide optimized answers
- VectorFiles: The content for the vector store object (which will be used to provide optimized answers)

To setup everything just simply open setup.py and change the values for
```
OPENAI_ORG = "org-..."
OPENAI_PRJ = "proj_..."
OPENAI_KEY = "sk-proj-..."
```

After this you can run the setup.py file by calling
```
python setup.py
``` 

## Usage
The folder "thread" contains information on using the OpenAI thread with the created assistant object.
- Data - this folder contains data files which can be added as context to a propmt
- Prompt - this folder contains prompt definitions which can be used to generate responses

To use the assistant object you
- open the Playground on the OpenAI platform
- you switch to the project you created
- open the Assistants menu
- start chatting by using the prompts and upload data files