
import uuid
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='.')
CORS(app)


@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


SESSIONS = {}

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
    
    
    match1 = re.search(r"my name is (\w+)", text)
    if match1:
        return match1.group(1).capitalize()
    
    
    match2 = re.search(r"i am (\w+)", text)
    if match2:
        return match2.group(1).capitalize()
    
   
    if not is_name_set:
        if text.isalpha() and len(text) >= 3 and text not in greetings:
            return text.capitalize()
    
    return None

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_input = data.get("message", "").strip()
    session_id = data.get("sessionId")
    
    if not session_id or session_id not in SESSIONS:
        session_id = str(uuid.uuid4())
        SESSIONS[session_id] = {
            "user_name": None,
            "chat_history": []
        }
        
    session_data = SESSIONS[session_id]
    user_name = session_data["user_name"]
    chat_history = session_data["chat_history"]
    
    if user_input.lower() == "exit":
        reply = "Run. That's your strongest skill."
        session_data["user_name"] = None
        session_data["chat_history"] = []
        return jsonify({"reply": reply, "sessionId": session_id})
    
    detected_name = extract_name(user_input, is_name_set=(user_name is not None))
    if detected_name:
        session_data["user_name"] = detected_name
        reply = f"{detected_name}? Fine. Now don't waste my time."
        return jsonify({"reply": reply, "sessionId": session_id})
    
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
            return jsonify({"reply": reply, "sessionId": session_id})
        
        except Exception as e:
            return jsonify({"reply": f"Error: {str(e)}", "sessionId": session_id})
    
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
        
        if len(chat_history) > 20:
            chat_history = chat_history[-18:]
            
        session_data["chat_history"] = chat_history
        
        return jsonify({"reply": reply, "sessionId": session_id})
    
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}", "sessionId": session_id})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("💀 Savage Sigma AI Backend Running 💀")
    print(f"Frontend: http://127.0.0.1:{port}")
    app.run(debug=True, host='0.0.0.0', port=port)
