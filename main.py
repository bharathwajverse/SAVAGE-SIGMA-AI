import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("Simple Groq Chatbot")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye.")
        break

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=500
        )

        print("\nAI:", response.choices[0].message.content)
        print("\n")

    except Exception as e:
        print("Error:", e)
