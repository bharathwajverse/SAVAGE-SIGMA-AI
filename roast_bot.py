import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("💀 Savage Sigma AI 💀")
print("Type 'exit' to quit\n")

user_name = None
chat_history = []

BASE_SYSTEM_PROMPT = """
You are Savage Sigma AI.

Personality:
- Aggressive.
- Slightly offensive but no slurs.
- Makes user feel like they should study themselves.
- Never repetitive.
- Short brutal answers.
- If question is deep, show respect but dominance.
"""

greetings = ["hi", "hello", "hey", "yo", "sup", "bro"]

def extract_name(text, is_name_set=False):
    text = text.lower().strip()

    # Case 1: "my name is sunny"
    match1 = re.search(r"my name is (\w+)", text)
    if match1:
        return match1.group(1).capitalize()

    # Case 2: "i am sunny"
    match2 = re.search(r"i am (\w+)", text)
    if match2:
        return match2.group(1).capitalize()

    # Case 3: single word name
    if not is_name_set:
        if text.isalpha() and len(text) >= 3 and text not in greetings:
            return text.capitalize()

    return None


while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Sigma AI: Run. That's your strongest skill.")
        break

    # Try extracting name anytime user says it
    detected_name = extract_name(user_input, is_name_set=(user_name is not None))
    if detected_name:
        user_name = detected_name
        print(f"\nSigma AI: {user_name}? Fine. Now don't waste my time.\n")
        continue

    # ======================
    # NO NAME YET
    # ======================
    if user_name is None:
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": BASE_SYSTEM_PROMPT + """
User has NOT given their name.
Refuse to answer.
Demand their name.
Roast dynamically.
Do not answer their actual question.
"""
                    },
                    {"role": "user", "content": user_input}
                ],
                temperature=1.0,
                max_tokens=120
            )

            reply = response.choices[0].message.content.strip()
            print(f"\nSigma AI: {reply}\n")

        except Exception as e:
            print("Error:", e)

        continue

    # ======================
    # NAME IS SET
    # ======================
    try:
        chat_history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": BASE_SYSTEM_PROMPT + f"""
The user's name is {user_name}.
Use their name occasionally.
If question is basic, roast hard.
If interesting, acknowledge but dominate.
Encourage learning instead of dependency.
"""
                }
            ] + chat_history,
            temperature=0.95,
            max_tokens=180
        )

        reply = response.choices[0].message.content.strip()

        print(f"\nSigma AI: {reply}\n")

        chat_history.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("Error:", e)