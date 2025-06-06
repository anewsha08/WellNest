# chatbot.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_bot(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful and empathetic medical assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Welcome to the HealthBot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Take care! Goodbye.")
            break

        answer = ask_bot(user_input)
        print("Bot:", answer)

        if any(word in user_input.lower() for word in ["anxious", "depressed", "sad", "panic", "stress"]):
            print("Bot: I'm here for you. You're not alone. Would you like breathing exercises or help connecting with a therapist?")
