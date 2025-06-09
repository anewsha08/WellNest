import time, random

responses = {
    "stress": ["Stress is tough. Try the 4-7-8 breathing technique. Ready?", 
               "Let’s pause. Want to try a 1-minute meditation?"],
    "sad": ["I’m sorry. Would music or a walk help?", 
            "Sadness passes. Want to talk about it?"]
}

def print_slowly(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def ask_bot(question):
    for keyword, options in responses.items():
        if keyword in question:
            return random.choice(options)
    return random.choice(["I’m listening. Go on.", "How does that make you feel?"])

if __name__ == "__main__":
    print_slowly("Bot: Hi! I’m your mental health helper. Type 'exit' to quit.")
    last_keyword = None

    while True:
        user_input = input("You: ").lower()
        if user_input in ['exit', 'quit']:
            print_slowly("Bot: Take care. Remember, you matter. ❤️")
            break

        # Simulate "thinking"
        time.sleep(random.uniform(0.2, 1.0))
        print_slowly("Bot: " + ask_bot(user_input))
