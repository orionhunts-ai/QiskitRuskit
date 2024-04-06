# Global settings
from llama_index.core import Settings
from portkey_ai.llms.llama_index import PortkeyLLM

portkey = PortkeyLLM(api_key="PORTKEY_API_KEY", virtual_key="VIRTUAL_KEY")
Settings.llm = portkey

# or use it locally like this
index.as_query_engine(llm=portkey)

# Use this service context in the query engine
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(llm=portkey)
response = query_engine.query("What did the author do growing up?")
print(response)


