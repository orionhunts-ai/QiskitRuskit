from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

config_list = [
    {
        "api_key": 'Your Anyscale API Key', 
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "base_url": PORTKEY_GATEWAY_URL,
        "api_type": "openai", # Portkey conforms to the openai api_type
        "default_headers": createHeaders(
            api_key = "Your Portkey API Key",
            provider = "anyscale",
        )
    }
]

assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False}) # IMPORTANT: set to True to run code in docker, recommended
user_proxy.initiate_chat(assistant, message="Say this is also a test - part 2.")
# This initiates an automated chat between the two agents to solve the task