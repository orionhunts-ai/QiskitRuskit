    """
    
    Base Langchain Configuration
    
    """

from portkey_ai.llms.langchain import ChatPortkey
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

portkeyChatModel = ChatPortkey(api_key="PORTKEY_API_KEY", virtual_key="VIRTUAL_KEY")

class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""


    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split(", ")

template = """You are a helpful assistant who generates comma separated lists.
A user will pass in a category, and you should generate 5 objects in that category in a comma separated list.
ONLY return a comma separated list, and nothing more."""
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])
chain = chat_prompt | portkeyChatModel | CommaSeparatedListOutputParser()
chain.invoke({"text": "colors"})
# >> ['red', 'blue', 'green', 'yellow', 'orange']