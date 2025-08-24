import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

model = pickle.load(open("mb.pkl", "rb"))

with open("cv.pkl", "rb") as f:
    cv = pickle.load(f)

languages = ['Estonian', 'Swedish', 'Thai', 'Tamil', 'Dutch', 'Japanese',
             'Turkish', 'Latin', 'Urdu', 'Indonesian', 'Portugese', 'French',
             'Chinese', 'Korean', 'Hindi', 'Spanish', 'Pushto', 'Persian',
             'Romanian', 'Russian', 'English', 'Arabic']

st.title("🌍 Language Detection App")
st.write("Type a sentence and I’ll detect the language!")

user_input = st.text_area("Enter your text here:")

if st.button("Detect Language"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        data = cv.transform([user_input]).toarray()
        pred = model.predict(data)[0]
        st.success(f"**Detected Language:** {pred}")
