from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Analyze sentiment
texts = [
    "I absolutely love this product! It's fantastic :)",
    "This is the worst service ever. I'm very disappointed.",
    "The food was okay, but the service was excellent!",
    "I dont like food"
]

for text in texts:
    sentiment = analyzer.polarity_scores(text)
    print(f"Text: {text}\nSentiment: {sentiment}\n")