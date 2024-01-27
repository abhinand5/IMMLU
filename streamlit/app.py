import streamlit as st
from translation import translate
from download_data import return_df

lang_dict = {
      "Tamil": 'ta'
    , "Telugu": 'te'
    , "Hindi": 'hi'
    , "Kannada": 'kn'
    , "Malayalam": 'ml'
    , "Marathi": 'mr'
    , "Bengali": 'bn'
}

tgt = st.selectbox(label = "Choose Language", 
                    options = list(lang_dict.keys()))

df = return_df()

english_df = df.sample(1, random_state = 42)
translated_df = english_df.copy()

#TODO: Translate MCQs, get approval from user



