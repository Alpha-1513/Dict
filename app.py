import requests
import streamlit as st

# Define the RapidAPI endpoint and headers
url = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"
headers = {
    "X-RapidAPI-Key": "a1439f3da5mshe93f907f5f927c1p19244fjsn9ed70508941f",
    "X-RapidAPI-Host": "dictionary-by-api-ninjas.p.rapidapi.com"
}

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
                st.write(meaning + "\n")  # Use "\n" for a newline
        else:
            st.error("Word not found or API request failed. Please try another word.")
    else:
        st.warning("Please enter a word to find its meaning.")
        
