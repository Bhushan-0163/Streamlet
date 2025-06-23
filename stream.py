import streamlit as st
import string

st.title("Word Count Dictionary Generator - By Bhushan")

st.write(
    """
    Paste or type your paragraph below.  
    Click **Get Word Counts** to see how many times each word appears!
    """
)

paragraph = st.text_area("Enter your paragraph here:")

if st.button("Get Word Counts"):
    if paragraph.strip():
        translator = str.maketrans('', '', string.punctuation)
        cleaned = paragraph.translate(translator).lower()
        words = cleaned.split()
        word_counts = {word: words.count(word) for word in set(words)}
        st.write(word_counts)
    else:
        st.warning("Please enter some text.")
