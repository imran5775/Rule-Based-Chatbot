"""EmranBot: a rule-based chatbot.

DecodeLabs AI Internship, Project 1 | Author: Muhammad Imran
"""

import random
import string
from datetime import datetime

BOT_NAME = "EmranBot"
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye"}
FALLBACK = "Sorry, I don't understand that yet. Type 'help' to see what I can do."

# Knowledge base: each intent has input patterns and possible replies.
INTENTS = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hi there! How can I help you?", "Hello! Nice to see you.", "Hey! What's up?"],
    },
    "salam": {
        "patterns": ["salam", "assalamualaikum", "assalam o alaikum"],
        "responses": ["Walaikum Assalam! How can I help you?"],
    },
    "how_are_you": {
        "patterns": ["how are you", "how are you doing", "whats up"],
        "responses": ["I'm running perfectly, thanks for asking!", "All systems working. How about you?"],
    },
    "bot_name": {
        "patterns": ["what is your name", "who are you"],
        "responses": [f"I'm {BOT_NAME}, a rule-based chatbot."],
    },
    "creator": {
        "patterns": ["who made you", "who created you", "who is your developer"],
        "responses": ["I was built by Muhammad Imran as part of the DecodeLabs AI internship."],
    },
    "what_is_ai": {
        "patterns": ["what is ai", "what is artificial intelligence"],
        "responses": ["AI is the ability of machines to do tasks that normally need human intelligence."],
    },
    "what_is_chatbot": {
        "patterns": ["what is a chatbot", "what is a rule based chatbot"],
        "responses": ["A rule-based chatbot replies using predefined rules instead of learning from data."],
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thanks a lot"],
        "responses": ["You're welcome!", "Happy to help!"],
    },
    "help": {
        "patterns": ["help", "what can you do"],
        "responses": [
            "Try: hello, how are you, who made you, what is ai, time, date, "
            "or 'my name is <name>'. Type 'bye' to exit."
        ],
    },
    "time": {"patterns": ["time", "what is the time", "current time"], "responses": []},
    "date": {"patterns": ["date", "what is the date", "todays date"], "responses": []},
}

# Intents whose reply depends on the moment the question is asked.
DYNAMIC = {
    "time": lambda: f"It's {datetime.now():%I:%M %p} right now.",
    "date": lambda: f"Today is {datetime.now():%A, %d %B %Y}.",
}

# Flat pattern -> intent table gives O(1) lookup instead of an if-elif ladder.
PATTERN_TO_INTENT = {
    pattern: intent
    for intent, data in INTENTS.items()
    for pattern in data["patterns"]
}


def sanitize(text):
    """Lowercase, trim, drop punctuation and extra spaces."""
    text = text.lower().replace("'", "")
    text = text.strip().strip(string.punctuation)
    return " ".join(text.split())


def get_reply(user_text, memory):
    """Return the bot's reply for one user message."""
    text = sanitize(user_text)

    if text.startswith("my name is "):
        memory["name"] = text.removeprefix("my name is ").title()
        return f"Nice to meet you, {memory['name']}!"
    if text == "what is my name":
        name = memory.get("name")
        return f"Your name is {name}." if name else "You haven't told me your name yet."

    intent = PATTERN_TO_INTENT.get(text)
    if intent is None:
        return FALLBACK
    if intent in DYNAMIC:
        return DYNAMIC[intent]()
    return random.choice(INTENTS[intent]["responses"])


def main():
    memory = {}
    print(f"{BOT_NAME} | Rule-Based AI Chatbot | by Muhammad Imran")
    print("Type 'help' for ideas, 'bye' to exit.\n")

    while True:
        try:
            user_text = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print(f"\n{BOT_NAME}: Goodbye!")
            break

        clean = sanitize(user_text)
        if not clean:
            continue
        if clean in EXIT_COMMANDS:
            print(f"{BOT_NAME}: Goodbye! Have a great day.")
            break

        print(f"{BOT_NAME}: {get_reply(user_text, memory)}")


if __name__ == "__main__":
    main()