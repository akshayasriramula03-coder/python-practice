from textblob import TextBlob


def analyze_sentiment(message):
    """
    Analyze the sentiment of a customer message.
    Returns Positive, Negative, or Neutral.
    """

    analysis = TextBlob(message)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return "Positive"

    elif polarity < -0.1:
        return "Negative"

    else:
        return "Neutral"