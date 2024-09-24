class SimpleChatbot:
    def __init__(self):
        self.greetings = ["hi", "hello", "hey", "howdy"]
        self.farewells = ["bye", "goodbye", "see you", "take care"]
        self.default_responses = [
            "I'm sorry, I don't understand that.",
            "Could you please rephrase?",
            "That's interesting! Tell me more."
        ]

    def respond(self, user_input):
        # Normalize the input to lowercase
        user_input = user_input.lower()

        # Check for greetings
        if any(greet in user_input for greet in self.greetings):
            return "Hello! How can I assist you today?"

        # Check for farewells
        elif any(farewell in user_input for farewell in self.farewells):
            return "Goodbye! Have a great day!"

        # Check for specific queries
        elif "your name" in user_input:
            return "I am a simple chatbot created to assist you."

        elif "help" in user_input:
            return "Sure! What do you need help with?"

        elif "weather" in user_input:
            return "I can't provide real-time weather updates, but I hope it's nice where you are!"

        # Default response for unrecognized input
        else:
            return self.default_responses[0]

def chat():
    print("Welcome to the Simple Chatbot! Type 'exit' to end the chat.")
    bot = SimpleChatbot()

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = bot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == '__main__':
    chat()