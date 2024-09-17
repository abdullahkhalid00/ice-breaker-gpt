import os
from groq import Groq
from utils import load_instructions


def generate_question(instructions=load_instructions('./instructions.txt')):
    client = Groq(api_key=os.environ.get('GROQ_API_KEY'))
    response = client.chat.completions.create(
        model='gemma2-9b-it',
        messages=[
            {
                'role': 'system',
                'content': instructions
            }
        ],
        max_tokens=1024,
        temperature=1.2,
        stream=None,
        stop=None,
    )
    return response.choices[0].message.content.strip()
