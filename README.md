# EmranBot: Rule-Based AI Chatbot

A command-line chatbot that answers using explicit rules and dictionary lookups, with no machine learning involved. Built as **Project 1** of the DecodeLabs Artificial Intelligence Industrial Training Kit (Batch 2026).

## Features

- Continuous conversation loop that runs until the user exits
- Input sanitization: handles upper/lower case, extra spaces and punctuation
- Knowledge base with 11 intents (greetings, small talk, AI basics, help, time, date and more)
- Fallback reply for anything the bot doesn't understand
- Random reply variation so the bot doesn't repeat itself
- Live answers for `time` and `date`
- Simple memory: tell it `my name is <name>` and ask `what is my name`
- Clean exit with `exit`, `quit`, `bye` or `goodbye` (Ctrl+C also exits safely)
- Unit tests included

## How it works

The bot follows the **IPO model** (Input, Process, Output):

1. **Input**: read the message and sanitize it (`lower()`, `strip()`, remove punctuation).
2. **Process**: look the cleaned text up in a dictionary that maps patterns to intents.
3. **Output**: print a reply, or the fallback if no rule matches.

Instead of a long `if-elif` ladder (O(n)), all patterns are stored in one dictionary, so each lookup is O(1) using `dict.get()`, which also provides the fallback in a single operation.

## Getting started

Requires **Python 3.9+**.

```bash
git clone https://github.com/imran5775/Rule-Based-Chatbot.git
cd Rule-Based-Chatbot
python chatbot.py
```

Run the tests:

```bash
python -m unittest -v
```

## Example conversation

```
EmranBot | Rule-Based AI Chatbot | by Muhammad Imran
Type 'help' for ideas, 'bye' to exit.

You:   HELLO
EmranBot: Hi there! How can I help you?
You: my name is imran
EmranBot: Nice to meet you, Imran!
You: What is my name?
EmranBot: Your name is Imran.
You: who made you
EmranBot: I was built by Muhammad Imran as part of the DecodeLabs AI internship.
You: asdfgh
EmranBot: Sorry, I don't understand that yet. Type 'help' to see what I can do.
You: bye
EmranBot: Goodbye! Have a great day.
```

## Project structure

```
rule-based-chatbot/
├── chatbot.py        # chatbot logic and main loop
├── test_chatbot.py   # unit tests
├── README.md
└── .gitignore
```

## Adding your own intents

Add a new entry to the `INTENTS` dictionary in `chatbot.py`:

```python
"weather": {
    "patterns": ["how is the weather", "weather"],
    "responses": ["I can't check the weather yet, but I hope it's nice!"],
},
```

## Future improvements

- Keyword and fuzzy matching so slight spelling mistakes still work
- Semantic matching with embeddings (the natural next step after this project)
- Hybrid mode: rules first, then pass unknown questions to an LLM
- Load intents from a JSON file

## Author

**Muhammad Imran**
DecodeLabs AI Internship, Batch 2026
