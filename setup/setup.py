# this setup python script creates the relevant assistant, vector store and vector files on the openai platform
# please create an openai account/organization, project and API key before running this script
# please install openai pip package before running this script

from openai import OpenAI
from assistant import Assistants
from vectorstore import VectorStores

OPENAI_ORG = ""
OPENAI_PRJ = ""
OPENAI_KEY = ""

# create client
client = OpenAI(
    organization=OPENAI_ORG,
    project=OPENAI_PRJ,
    api_key=OPENAI_KEY
)

# create assistant
assistant_simon = client.beta.assistants.create(
    name=Assistants.Simon.name,
    instructions=Assistants.Simon.instructions,
    model=Assistants.Simon.model,
    tools=Assistants.Simon.tools
)
print(assistant_simon)

# create vector store and upload vector files
vector_store_edi = client.beta.vector_stores.create(
    name=VectorStores.EdiStore.name
)
print(vector_store_edi)
file_paths = ["./vectorfiles/schema/MyCustomINVSchema.txt", "./vectorfiles/schema/MyCustomPOSchema.txt", "./vectorfiles/schema/MyCustomSISchema.txt", "./vectorfiles/rules/mapping-rules.txt"]
file_streams = [open(path, "rb") for path in file_paths]
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
  vector_store_id = vector_store_edi.id, files = file_streams
)
print(file_batch.status)
print(file_batch.file_counts)

# update assistant with vector store
assistant_simon = client.beta.assistants.update(
  assistant_id = assistant_simon.id,
  tool_resources = {"file_search": {"vector_store_ids": [vector_store_edi.id]}},
)
print(assistant_simon)