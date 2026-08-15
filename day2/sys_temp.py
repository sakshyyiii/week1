import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"

# User role and prompt
role = "user"
prompt = "suggest aa name for my food company."

# System message
message_system = {
    "role": "system",
    "content": "You are a brand manager who suggests name for myy food company, name should be in one word. "
}

# User message
message = {
    "role": role,
    "content": prompt
}

# Final messages list
messages = [
    message_system,
    message
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2
)

print(response)

print("##########################################")

answer = response.choices[0].message.content
print(answer)