""" 
Together AI with Portkey Virtual Key
"""
import portkey



completion = portkey.chat.completions.create(
    messages= [{ "role": 'user', "content": 'Say this is a test' }],
    model='togethercomputer/llama-2-70b-chat'
)

print(completion)