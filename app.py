from src.agent import app

print("AI Document Assistant")
print("Type 'exit' to quit.")

messages = []

while True:
    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": question
    })

    try:
        result = app.invoke({
            "messages": messages
        })

        messages = result["messages"]

        print("\nAnswer:")
        print(messages[-1].content)

    except Exception as e:
        print("\nSomething went wrong.")
        print("Error:", e)