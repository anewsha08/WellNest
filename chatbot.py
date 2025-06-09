def ask_bot(question):
    return "I'm here for you. It sounds like you're feeling stressed. Would you like breathing exercises or to talk to someone?"

if __name__ == "__main__":
    print("Welcome to the HealthBot. Type 'exit' to quit.")
    last_response = None  # To track the last bot response that requires a yes/no answer
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ['exit', 'quit']:
            print("Bot: Take care! Goodbye.")
            break
        
        # Check if the user is responding to the last question
        if last_response and user_input in ['yes', 'no']:
            if "breathing exercises" in last_response.lower() or "calming techniques" in last_response.lower():
                if user_input == 'yes':
                    print("Bot: Great! Let's begin. Breathe in slowly for 4 seconds, hold for 4 seconds, then exhale for 6 seconds. Repeat this cycle.")
                else:
                    print("Bot: No problem. Remember these techniques are available whenever you need them.")
            elif "talk to someone" in last_response.lower():
                if user_input == 'yes':
                    print("Bot: I can connect you with a professional. Would you prefer online chat or phone support?")
                else:
                    print("Bot: Understood. I'm here if you change your mind.")
            last_response = None  # Reset after handling
            continue
            
        answer = ask_bot(user_input)
        print("Bot:", answer)
        last_response = answer  # Store this response for possible yes/no handling

        if any(word in user_input for word in ["anxious", "depressed", "sad", "panic", "stress"]):
            follow_up = "Bot: You're not alone. Would you like me to guide you through some calming techniques?"
            print(follow_up)
            last_response = follow_up  # Store this as the last response
