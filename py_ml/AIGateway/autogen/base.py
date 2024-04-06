from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Import the portkey library to fetch helper functions
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

config_list = [
    {
        "api_key": 'Your OpenAI Key', 
        "model": "gpt-3.5-turbo",
        "base_url": PORTKEY_GATEWAY_URL,
        "api_type": "openai",
        "default_headers": createHeaders(
            api_key = "Your Portkey API Key",
            provider = "openai",
        )
    }
]

assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False}) # IMPORTANT: set to True to run code in docker, recommended
user_proxy.initiate_chat(assistant, message="Say this is also a test - part 2.")
# This initiates an automated chat between the two agents to solve the task