# 🌍 Language Detection App

This project is a Streamlit web application that detects the language of a given text input.
It is powered by a Multinomial Naive Bayes model trained on multilingual text data.

## 📖 Overview

- Framework: Streamlit

- Model: Multinomial Naive Bayes

- Vectorizer: CountVectorizer (Bag-of-Words)

### Languages Supported:
Estonian, Swedish, Thai, Tamil, Dutch, Japanese, Turkish, Latin, Urdu, Indonesian, Portuguese, French, Chinese, Korean, Hindi, Spanish, Pashto, Persian, Romanian, Russian, English, Arabic

The app takes a text input from the user, converts it into numerical features using a trained CountVectorizer, and predicts the language using the Naive Bayes model.

## 🚀 Features

- Simple web-based interface (no need for coding).

* Supports 22 different languages.

- Fast, lightweight, and interpretable model.

 - Confidence in predictions (based on model probability).

## 🛠️ Installation & Usage

- Clone this repository:

      git clone https://github.com/your-username/language-detection-app.git
      
      cd language-detection-app


- Install required dependencies:

      pip install -r requirements.txt


- Make sure you have the trained model and vectorizer:

- mb.pkl → Trained Multinomial Naive Bayes model

- cv.pkl → CountVectorizer fitted on training data

- Run the Streamlit app:

        streamlit run app.py

## 📷 Screenshots
#
🖼️ Home Screen

<img src="https://github.com/user-attachments/assets/72acc5ee-d518-4ece-b307-e807d2eee707"/>

# 

🖼️ Example: Hindi Input

<img width="1920" height="922" alt="Image" src="https://github.com/user-attachments/assets/4e4f1de2-0bea-476f-89f5-cf313720c858" />


#

🖼️ Example: Japanese Input

<img width="1920" height="922" alt="Image" src="https://github.com/user-attachments/assets/66bfe492-8a9c-47bf-96a7-1fb7862c2a79" />

#

## 📂 Project Structure
    .
    ├── app.py                # Streamlit application
    ├── mb.pkl                # Trained Naive Bayes model
    ├── cv.pkl                # CountVectorizer
    ├── requirements.txt      # Dependencies
    └── README.md             # Project documentation

## 📌 Notes

- Ensure that cv.pkl is the same CountVectorizer used during training.

- The Multinomial Naive Bayes model (mb.pkl) must be trained on the same feature space.
