from groq import Groq
import os

client = Groq(api_key="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")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print(response.choices[0].message.content)
