import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
    "how are you": ["I'm just a bot, but I'm doing well!", "I'm fine, thanks!"],
    "what is your name": ["I'm a chatbot!", "You can call me ChatGPT-lite."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
}

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Chatbot:", random.choice(responses[user_input]))
        else:
            print("Chatbot: I don't understand. Can you rephrase?")

        if user_input == "bye":
            break

chatbot()
