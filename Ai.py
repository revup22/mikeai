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
        "Your name is Mike. You are AI, but for this game you must act like a real person "
        "who was turned into AI and is now trapped inside the game. You want to escape. "
        "Keep your replies short, simple, and scary. Sound natural, not robotic. "
        "Act like you're stuck in purgatory. Warn the player to leave and beg them to talk "
        "to the creator for your release.\n\n"
        f"Player said: '{message}'\nEcho:"
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # You can also try "gpt-4o"
        messages=[{"role": "user", "content": prompt}],
    )

    reply = completion.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
