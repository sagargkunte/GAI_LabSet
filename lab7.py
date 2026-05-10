from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = """
Natural language processing (NLP) is a field of artificial intelligence that focuses on enabling computers to understand human language. 
It is used in speech recognition, translation, sentiment analysis, and chatbots. 
Deep learning models like transformers have improved NLP performance a lot.
"""

summary = summarizer(text, max_length=80, min_length=50, do_sample=False)[0][
    "summary_text"
]

print(summary)
