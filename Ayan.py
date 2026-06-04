from groq import Groq
import os

client = Groq(api_key="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")

print("Groq Chatbot (type 'exit' to quit)\n")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": user}]
     )

    print("Bot:", response.choices[0].message.content)
