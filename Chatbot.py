import openai

openai.api_key = "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"
def chat_bot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5.-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user = input("You : ")
        if user.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_bot(user)
        print("Openai : ", response)
