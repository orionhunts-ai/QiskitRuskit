"""

OpenAI Gateway Template

"""


import os
from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders
import asyncio
from portkey_ai import AsyncPortkey

portkey = AsyncPortkey(
    if api_key == None:
        api_key=os.getenv(api_key="V4NjnMLB1RiAPGFOvZu0KDAOZYU\="):
        
    virtual_key="VIRTUAL_KEY"
)

async def main():
    chat_completion = await portkey.chat.completions.create(
        messages=[{'role': 'user', 'content': 'Say this is a test'}],
        model='gpt-4'
    )

    print(chat_completion)

asyncio.run(main())


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("PORTKEY_GATEWAY_URL"),
    default_headers=createHeaders(
        provider="openai",
        api_key="V4NjnMLB1RiAPGFOvZu0KDAOZYU="
    )
)

chat_complete = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[{"role": "user", "content": "What's a Fractal?"}],
)

print(chat_complete.choices[0].message.content)

