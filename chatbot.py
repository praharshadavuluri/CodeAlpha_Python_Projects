# Basic Chatbot

print("====================================")
print("      WELCOME TO BASIC CHATBOT")
print("====================================")
print("Type 'bye' to exit the chatbot.\n")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! Welcome.")

    elif user == "hi":
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot: My name is CodeAlpha ChatBot.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "python":
        print("Bot: Python is a powerful programming language.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")