# Task 4: Basic Chatbot

A simple rule-based chatbot built in Python. It matches user input against a
set of predefined phrases and responds accordingly.

## Features

- Recognizes common greetings and phrases:
  - `hello` / `hi` / `hey` → `Hi!`
  - `how are you` → `I'm fine, thanks! How about you?`
  - `bye` / `goodbye` / `exit` / `quit` → `Goodbye!` (ends the chat)
  - `what is your name` / `who are you` → `I'm a simple rule-based chatbot.`
  - `thanks` / `thank you` → `You're welcome!`
- Falls back to a friendly "I don't understand" message for anything else.
- Case-insensitive and ignores extra spaces (e.g. "HELLO", " hello " both work).

## Key Concepts Used

- **Functions** – logic is split into `get_response()` and `chat()`.
- **if-elif statements** – used to match user input to the right reply.
- **Loops** – a `while True` loop keeps the conversation going.
- **Input/Output** – `input()` reads what the user types, `print()` shows replies.

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. Make sure you have Python installed. Check with:
   ```bash
   python --version
   ```
2. Run the chatbot:
   ```bash
   python chatbot.py
   ```
3. Type a message and press Enter. Type `bye`, `goodbye`, `exit`, or `quit`
   at any time to end the conversation.

## Example Session

```
Chatbot: Hello! Type 'bye' to end the chat.
You: hello
Chatbot: Hi!
You: how are you
Chatbot: I'm fine, thanks! How about you?
You: bye
Chatbot: Goodbye!
```

## Project Structure

```
.
├── chatbot.py   # Main chatbot script
└── README.md    # Project documentation
```

## Possible Improvements

- Add more phrases and synonyms to `get_response()`.
- Use simple keyword matching (e.g. `"weather" in text`) instead of exact
  phrase matching, so the bot understands more variations.
- Store conversation history to a file.
- Add basic natural language processing (NLP) for smarter matching.
