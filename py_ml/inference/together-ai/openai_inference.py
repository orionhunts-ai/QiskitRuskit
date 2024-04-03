import os
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="openai",
        api_key="V4NjnMLB1RiAPGFOvZu0KDAOZYU="
    )
)

chat_complete = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What's a Fractal?"}],
)

print(chat_complete.choices[0].message.content)