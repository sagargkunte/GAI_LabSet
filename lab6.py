from transformers import pipeline

analyzer = pipeline("sentiment-analysis")

feedbacks = [
    "You are very good , amazing!",
    "Shit why did you do that stuff"
]

for text in feedbacks:
    result = analyzer(text)[0]
    print(text)
    print(result["label"],result["score"])
    print()