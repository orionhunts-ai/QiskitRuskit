from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
# Where the model is running. e.g. us-central1 or europe-west4 for haiku


client = AnthropicVertex(project_id=os.getenv("PROJECT_ID"), region=os.getenv("REGION"))

message = client.messages.create(
    model="claude-3-haiku@20240307", #@TODO user to select model
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hey Claude!",
        }
    ],
)
