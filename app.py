import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import streamlit as st
import random

# Page configuration
st.set_page_config(page_title="Youtrition", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            background-color: #000000;
            color: #ffffff;
        }
        .circle {
            width: 60px;
            height: 60px;
            background-color: #6d31fd;
            border-radius: 50%;
            display: inline-block;
            margin: 10px;
        }
        .semi-circle {
            width: 60px;
            height: 30px;
            background-color: #ffdf5f;
            border-top-left-radius: 60px;
            border-top-right-radius: 60px;
            display: inline-block;
            margin: 10px;
        }
        .rectangle {
            width: 120px;
            height: 40px;
            background-color: #066b6b;
            display: inline-block;
            margin: 10px;
        }
        .header {
            font-size: 48px;
            color: #ffffff;
            font-weight: bold;
        }
        .subheader {
            font-size: 20px;
            color: #ff8127;
        }
        .highlight {
            background-color: #ffdf5f;
            color: #000000;
            padding: 5px 10px;
            border-radius: 10px;
            font-weight: bold;
        }
        .cta-button {
            background-color: #ff8127;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: bold;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">Youtrition</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Personalized nutrition from your gut microbes</div>', unsafe_allow_html=True)
st.markdown('<div class="circle"></div><div class="semi-circle"></div><div class="rectangle"></div>', unsafe_allow_html=True)

# Input fields
st.write("Please answer the following questions to calculate your personalized nutrition advice:")

ibs = st.selectbox("Do you have Irritable Bowel Syndrome (IBS)?", 
                   ["Yes - Diagnosed by a Medical Professional", "Yes- Self Diagnosis", "No"])
ibd = st.selectbox
