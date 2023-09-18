import requests
import streamlit as st

# Define the RapidAPI endpoint and headers
url = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"
headers = {
    "X-RapidAPI-Key": "a1439f3da5mshe93f907f5f927c1p19244fjsn9ed70508941f",
    "X-RapidAPI-Host": "dictionary-by-api-ninjas.p.rapidapi.com"
}

# Set page title and background image
st.set_page_config(
    page_title="Word Meaning Finder by Altamish",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="auto",
)

# Define custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-image: url('https://unsplash.com/photos/BlIhVfXbi9s'); /* Add your background image file path here */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: Arial, sans-serif;
        color: #333;
    }
    .stApp {
        max-width: 800px;
        padding: 2rem;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        margin-top: 2rem;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stTextInput {
        background-color: #f8f8f8;
    }
    .stButton>button {
        background-color: #0072B2;
        color: #fff;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #00548B;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app title and header
st.title("Word Meaning Finder")

# Input field for user to enter a word
word = st.text_input("Enter a word:")

# Create a button to trigger the API call
if st.button("Find Meaning"):
    if word:
        querystring = {"word": word}
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        if "meaning" in data:
            st.subheader("Meaning:")
            for meaning in data["meaning"]:
                st.write(meaning + "/n")
        else:
            st.error("Word not found or API request failed. Please try another word.")
    else:
        st.warning("Please enter a word to find its meaning.")
