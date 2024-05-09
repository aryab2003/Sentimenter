from textblob import TextBlob
import pandas as pd
import streamlit as st
import fitz
from collections import Counter
import matplotlib.pyplot as plt


# Function to perform sentiment analysis
def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = (
        "Positive" if polarity > 0 else ("Negative" if polarity < 0 else "Neutral")
    )
    return polarity, sentiment


# Function to highlight keywords in the text
def highlight_keywords(text, keywords):
    for keyword in keywords:
        text = text.replace(
            keyword, f'<mark style="background-color: yellow;">{keyword}</mark>'
        )
        text = text.replace(
            keyword.lower(),
            f'<mark style="background-color: yellow;">{keyword.lower()}</mark>',
        )
        text = text.replace(
            keyword.upper(),
            f'<mark style="background-color: yellow;">{keyword.upper()}</mark>',
        )
    return text


# Function to plot sentiment distribution
def plot_sentiment_distribution(sentiments):
    labels, counts = zip(*Counter(sentiments).items())
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    return fig


st.header("Sentiment Analysis")

# For text analysis
with st.expander("Analyze Text"):
    text = st.text_input("Enter the text")
    if text:

        polarity, sentiment = perform_sentiment_analysis(text)
        st.write("Polarity:", round(polarity, 2))
        st.write("Sentiment:", sentiment)

        # Highlight keywords
        keywords = [
            "positive",
            "negative",
            "neutral",
            "good",
            "bad",
            "excellent",
            "awful",
            "great",
            "terrible",
            "nice",
            "so-so",
            "awesome",
            "horrible",
            "satisfactory",
            "unsatisfactory",
            "fine",
            "poor",
            "amazing",
            "dreadful",
            "wonderful",
            "disappointing",
            "superb",
            "mediocre",
            "fantastic",
            "atrocious",
            "brilliant",
            "subpar",
            "phenomenal",
            "substandard",
            "outstanding",
            "inferior",
            "exceptional",
            "lousy",
            "stellar",
            "average",
            "remarkable",
            "unsatisfying",
            "splendid",
            "inferior",
            "impressive",
            "disappointing",
            "delightful",
            "unpleasant",
            "satisfying",
            "unsatisfying",
            "marvelous",
            "unimpressive",
            "positive",
            "negative",
            "satisfied",
            "unsatisfied",
            "content",
            "discontent",
            "happy",
            "sad",
            "joyful",
            "unhappy",
            "contented",
            "dissatisfied",
            "glad",
            "unfortunate",
            "fortunate",
            "ecstatic",
            "miserable",
            "elated",
            "depressed",
            "cheerful",
            "gloomy",
            "cheery",
            "melancholy",
            "uplifting",
            "heartbreaking",
            "pleased",
            "unpleased",
            "hopeful",
            "hopeless",
            "exhilarated",
            "despondent",
            "excited",
            "dejected",
            "enthusiastic",
            "disheartened",
            "optimistic",
            "pessimistic",
            "thrilled",
            "defeated",
            "eager",
            "apathetic",
            "energized",
            "drained",
            "invigorated",
            "exhausted",
            "delighted",
            "discouraged",
            "overwhelmed",
            "underwhelmed",
            "radiant",
            "disappointed",
            "vibrant",
            "desperate",
            "entertained",
            "bored",
            "amused",
            "tedious",
            "engaging",
            "dull",
            "captivating",
            "mind-numbing",
            "fascinating",
            "uninteresting",
            "exciting",
            "dreary",
            "stimulating",
            "sleep-inducing",
            "exhilarating",
            "tiring",
            "inspiring",
            "wearisome",
            "refreshing",
            "wearying",
            "restful",
            "exhausting",
            "relaxing",
            "draining",
            "energizing",
            "enervating",
            "invigorating",
            "fatiguing",
            "soothing",
            "revitalizing",
            "tedious",
            "rejuvenating",
            "boring",
            "refreshing",
            "invigorating",
            "tiring",
            "exhilarating",
            "inspiring",
            "wearying",
            "restful",
            "enervating",
            "energizing",
            "relaxing",
            "revitalizing",
            "soothing",
            "fatiguing",
            "rejuvenating",
        ]
        highlighted_text = highlight_keywords(text, keywords)
        st.write("Highlighted Text:")
        st.markdown(highlighted_text, unsafe_allow_html=True)

# For PDF analysis
with st.expander("Analyze PDF"):
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        pdf_bytes = uploaded_file.read()
        text = ""
        with fitz.open("pdf", pdf_bytes) as pdf_document:
            for page in pdf_document:
                text += page.get_text()

        language = detect_language(text)
        st.write(f"Detected Language: {language}")

        polarity, sentiment = perform_sentiment_analysis(text)
        st.write("Polarity:", round(polarity, 2))
        st.write("Sentiment:", sentiment)

        # Plot sentiment distribution
        sentiments = [
            "Positive" if p > 0 else ("Negative" if p < 0 else "Neutral")
            for p in TextBlob(text).sentiment.polarity
        ]

        # Display the plot inside the expander
        st.pyplot(plot_sentiment_distribution(sentiments))
