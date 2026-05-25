def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in ["hello", "hi", "hey"]:
        return "Hello there!"
    elif  user_input in ["how are you", "how are you doing"]:
        return "I'm fine thanks! How about you?"
    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple chatbot."
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a nice day."
    elif user_input in ["what can you do", "help"]:
        return "I can chat with you using simple replies."
    elif user_input in ["thank you", "thanks"]:
        return "You're welcome!"
    else:
        return "Sorry, I don't understand that."
print("Simple Chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    reply  = chatbot_response(user_input)
    print("Bot:" ,reply)
    if user_input.lower() == "bye":
        break