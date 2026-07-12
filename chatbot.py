"""
Task 4: Basic Rule-Based Chatbot
Concepts used: if-elif, functions, loops, input/output
"""


def get_response(user_input):
    """Return a predefined reply based on the user's message."""
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text in ("how are you", "how are you?"):
        return "I'm fine, thanks! How about you?"
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    elif text in ("what is your name", "who are you"):
        return "I'm a simple rule-based chatbot."
    elif text in ("thanks", "thank you"):
        return "You're welcome!"
    else:
        return "Sorry, I don't understand that. Try saying hello, how are you, or bye."


def chat():
    """Main loop that keeps the conversation going until the user says bye."""
    print("Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Chatbot:", reply)

        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chat()
