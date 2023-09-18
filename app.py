import requests
import streamlit as st

# Define the RapidAPI endpoint and headers
url = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"
headers = {
    "X-RapidAPI-Key": "a1439f3da5mshe93f907f5f927c1p19244fjsn9ed70508941f",
    "X-RapidAPI-Host": "dictionary-by-api-ninjas.p.rapidapi.com"
}

# Streamlit app title and header
st.title("Word Meaning\Defination Finder by Altamish")

# Input field for user to enter a word
word = st.text_input("Enter a word:")

# Create a button to trigger the API call
if st.button("Find Meaning"):
    if word:
        querystring = {"word": word}
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        
        if "definition" in data:
            st.subheader("Meaning:")
            definition = data["definition"]
            # Split the definition into points and display each on a new line
            points = definition.split(". ")
            for point in points:
                st.write(point)
