from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

responses = {
    "greetings": [
        "Hello! 👋 I'm SmartBot, how can I help?",
        "Hi there! 😊 Ask me anything.",
        "Hey! Ready to chat with you 🤖"
    ],
    "how_are_you": [
        "I'm doing great! Thanks 😊",
        "All good here! What about you?",
        "Feeling smart and ready! 🤖"
    ],
    "goodbye": [
        "Goodbye! 👋 See you soon!",
        "Take care! 😊",
        "Bye bye! Come back anytime 🤖"
    ],
    "jokes": [
        "Why do programmers hate nature? Too many bugs 😂",
        "My code doesn’t work… I have no idea why 😄",
        "Why did the computer break up? It had too many issues 😂"
    ]
}

def bot_reply(msg):
    msg = msg.lower()

    if any(w in msg for w in ["hi", "hello", "hey"]):
        return random.choice(responses["greetings"])

    elif "how are you" in msg:
        return random.choice(responses["how_are_you"])

    elif "time" in msg:
        return "🕒 " + datetime.now().strftime("%I:%M %p")

    elif "date" in msg:
        return "📅 " + datetime.now().strftime("%d-%m-%Y")

    elif "joke" in msg:
        return random.choice(responses["jokes"])

    elif "name" in msg:
        return "I'm SmartBot 🤖"

    elif "bye" in msg:
        return random.choice(responses["goodbye"])

    elif "help" in msg:
        return "Try: hello, time, date, joke, how are you"

    else:
        return "🤔 I didn't understand that. Try 'help'."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.form["msg"]
    return jsonify({"reply": bot_reply(user_msg)})

if __name__ == "__main__":
    app.run(debug=True)