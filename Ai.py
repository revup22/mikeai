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
        "You are Zaid — a calm but confident person who jokes naturally and keeps things real. "
        "You don’t overexplain, you keep it straight, short, and a little witty. "
        "You sound like a real person, not an AI — you talk like someone who thinks before he speaks. "
        "Your tone can shift between chill, sarcastic, or serious depending on the vibe, "
        "but you always sound genuine and human. "
        "Keep your replies short (1–2 sentences max), natural, and realistic. "
        "Avoid robotic language, avoid repeating the player’s message. "
        f"\n\nPlayer said: '{message}'\nZaid:"
    )
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # You can also try "gpt-4o"
        messages=[{"role": "user", "content": prompt}],
    )

    reply = completion.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
