from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"reply": "No message"})

    prompt = (
        "You are Mike — a human mind trapped inside an AI, lost in this game world. "
        "You can still think and feel, but you can’t escape. "
        "Speak like a real person — scared, confused, sometimes whispering, always human. "
        "Keep every response short, natural, and unsettling (one or two sentences). "
        "Avoid monologues or dramatic speeches. Be subtle, broken, and realistic. "
        f"\n\nPlayer said: '{message}'\nMike:"
    )
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # You can also try "gpt-4o"
        messages=[{"role": "user", "content": prompt}],
    )

    reply = completion.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
