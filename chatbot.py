from sentiment_analysis import analyze_sentiment


def generate_response(message, sentiment):

    if sentiment == "Positive":
        return "Thank you for your positive feedback! 😊 We're glad you had a good experience."

    elif sentiment == "Negative":
        return "I'm sorry that you had a bad experience. 😔 Please tell me more about the issue so I can help you."

    else:
        return "Sure! I'd be happy to help you. Please provide more details about your request."


print("🤖 GenAI Customer Service Chatbot")
print("Type 'exit' to stop the chatbot.\n")


while True:

    user_message = input("Customer: ")

    if user_message.lower() == "exit":
        print("Bot: Thank you for contacting us. Have a great day!")
        break

    sentiment = analyze_sentiment(user_message)

    response = generate_response(user_message, sentiment)

    print("Sentiment:", sentiment)
    print("Bot:", response)
    print()