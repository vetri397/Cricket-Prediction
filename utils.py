import streamlit as st
import pandas as pd
import joblib


@st.cache_resource
def load_model():
    return joblib.load("cricket_predictor.pkl")


@st.cache_data
def load_features():
    return pd.read_csv("features.csv")


@st.cache_data
def load_matches():
    return pd.read_csv("data/matches.csv")


@st.cache_data
def load_deliveries():
    return pd.read_csv("data/deliveries.csv")