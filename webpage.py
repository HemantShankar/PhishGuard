import streamlit as st
import pickle  
# import pandas as pd
import numpy as np
# from xgboost import XGBClassifier
from url_script_main import featureExtraction


with open('XGBoostClassifier.pickle.dat', 'rb') as file:
    model = pickle.load(file)
# Function to process the URL input and predict using the loaded model
def predict_url(url):
    # st.write(f"Processing the URL....")
    processed_url = featureExtraction(url)

    # st.write(processed_url)
    # st.write("Model is predicting.....")
    prediction = model.predict(np.array(processed_url).reshape(1, -1))
    # st.write(f"Generating Result....")  
    return prediction[0]


# Streamlit UI
st.set_page_config(page_title="PhishGuard", page_icon="🔒", layout="centered",initial_sidebar_state="collapsed",)
st.sidebar.title("About")
st.sidebar.info(
    """
    This web application allows you to detect phishing websites by analyzing URLs using a Machine Learning model. 
    It is Developed by [Hemant Shankar](https://www.linkedin.com/in/hemant-shankar/).
    
    - **Python libraries:** Streamlit, XGBoost, scikit-learn, BeautifulSoup
    - **Model:** Pre-trained XGBoost classifier
    - **Github Repo:** [YourRepo](https://github.com/HemantShankar)
    """
)
# Header
st.markdown("<h1 style='text-align: center; font-size: 67px; margin-top: -30px; color: white;'>URL Phishing Detection</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-top: -50px; color: blue;'>Protect yourself from malicious websites</h2>", unsafe_allow_html=True)
st.write("") # Adding space
st.write("") # Adding space
st.write("") # Adding space
# Input section
url_input = st.text_input("Enter the URL you want to check", placeholder="https://example.com", max_chars=1064)

#Predict button
st.write("") # Adding space
# col1, col2, col3, col4, col5 = st.columns([1, 1, 1,1,1]) # Making Horizontal division
# with col3:
if st.button("Check URL"):
    if url_input:
        prediction = predict_url(url_input)
        if prediction == 1:
            st.success("The website is Genuine ✅")
        else:
            st.error("Warning: This is a Phishing website ❌")
    else:
        st.warning("Please enter a valid URL")   

st.write("") # Adding space
st.write("") # Adding space
st.write("") # Adding space
st.write("") # Adding space
st.write("") # Adding space
st.write("") # Adding space
st.write("") # Adding space
# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 22px; margin-top: -15px; color: gray;'>Developed by Hemant Shankar | Powered by Machine Learning</p>",
    unsafe_allow_html=True
)
# Custom HTML for social media links with icons
st.markdown("""
    <style>
        .social-icons {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: -20px;
        }
        .social-icons a {
            margin: 0 8px;
            text-decoration: none;
        }
        .social-icons img {
            width: 55px;  /* Adjust the size of icons */
            height: 55px;
        }
    </style>
""", unsafe_allow_html=True)

# Social Media Links (use your own social media URLs)
st.markdown("""
<div class="social-icons">
    <a href="https://www.linkedin.com/in/hemant-shankar/" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Linkedin_icon.svg" alt="LinkedIn">
    </a>
    <a href="https://www.instagram.com/_hemantshankar_/" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
    </a>
    <a href="https://github.com/HemantShankar" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg" alt="GitHub">
    </a>
</div>
""", unsafe_allow_html=True)
