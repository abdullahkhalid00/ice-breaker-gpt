import os

from groq import Groq
from utils import load_instructions


client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

system_prompt = {
    'role': 'system',
    'content': load_instructions('./instructions.txt')
}

response = client.chat.completions.create(
    model='gemma2-9b-it',
    messages=[system_prompt],
    max_tokens=1024,
    temperature=1.2,
    stream=None,
    stop=None,
)

print(response.choices[0].message.content.strip())
