# OpenAI EDI Assistant

This repository contains information about creating a simple OpenAI EDI Assistant. The assistant is a simple chatbot that can be used to answer questions about Electronic Data Interchange (EDI) using the OpenAI API platform.

All you have to do is create an account on the OpenAI platform: https://platform.openai.com/ and buy some credis

## Installation
The folder "setup" contains information on setting up the OpenAI objects:
- Assistant (Simon): The assistant object that will be used to interact with the OpenAI API using a chat interface
- Vector-Store: The vector store object that will be used by the assistant to provide optimized answers
- Vector-Files: The content for the vector store object (which will be used to provide optimized answers)

## Usage
The folder "thread" contains information on using the OpenAI thread with the created assistant object.
- Data - this folder contains data files which can be added as context to a propmt
- Prompt - this folder contains prompt definitions which can be used to generate responses