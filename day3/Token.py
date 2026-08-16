import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai?")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role="user"

#3 prompts
prompt1 = "hii"
prompt2 = "Explain time travel in details"
prompt3 = "Write essay on machine learning in 100 words"

prompts=[prompt1, prompt2, prompt3]
for prompt in prompts:
    messages = {
        "role": role,
        "content": prompt
    }
    messages = [messages]
    response = client.chat.completions.create(
        model=model, messages=messages, max_tokens=500
    )
    usage = response.usage
    print(f"Prompt: {prompt} --> your tokens: {usage.prompt_tokens}, completion tokens: {usage.completion_tokens}, total tokens: {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")

#     response = client.chat.completions.create(
#         model=model,
#         messages=messages
#     )

#     print(response)
#     print("##########################################")
#     print(response.choices[0].message.content)

# messages = [
#     {
#         "role": "user",
#         "content": "Do you know Sakshi?"
#     }
# ]

# response = client.chat.completions.create(
#     model=model,
#     messages=messages
# )

# print(response)
# print("##########################################")
# print(response.choices[0].message.content)