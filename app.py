import streamlit as st

st.title("AI Repo Explainer")

repo_url = st.text_input("GitHub Repo URL")

if st.button("Analyze"):
    st.write("Analysis will appear here.")

