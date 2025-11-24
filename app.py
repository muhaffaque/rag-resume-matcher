import streamlit as st
from src.retrieval import retrieve_top_resumes

st.title("🎯 Resume Matcher (RAG App)")

jd_text = st.text_area("Paste Job Description")
uploaded_files = st.file_uploader("Upload Resumes (PDF)", accept_multiple_files=True, type=["pdf"])
k_value = st.number_input("Select number of top resumes to retrieve", min_value=1, max_value=20, value=3, step=1)

if st.button("Find Top Matches"):
    with st.spinner("Processing..."):
        results = retrieve_top_resumes(jd_text, uploaded_files,k_value)
    st.success("✅ Top Matching Resumes")
    for i, res in enumerate(results, 1):
        st.write(f"**{i}. {res['candidate_name']}** — ({res['file_name']})  \n📊 *Similarity Score:* {res['similarity_score']}")