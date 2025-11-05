
# 🧠 Resume Selector — RAG Application  

###🚀 Features

An **AI-powered Resume Shortlisting System** built using **Retrieval-Augmented Generation (RAG)** to match **resumes** against **job descriptions** semantically.  
This project helps recruiters or HR professionals automatically identify the **top-matching resumes** from a pool of candidates using **LangChain**, **FAISS**, **HuggingFace embeddings**, and **Groq LLM**.

---

## 🚀 Features  

- 🔍 **Semantic Matching** — Finds resumes most relevant to a given job description using sentence embeddings.  
- 🧠 **RAG Architecture** — Combines retrieval (FAISS) with language generation (Groq LLM).  
- ⚙️ **Modular Design** — Clean separation of modules for data ingestion, embedding, and retrieval.  
- 🧾 **Custom Logging & Exception Handling** — Built-in debug logs and structured error management.  
- 🎨 **Interactive Streamlit UI** — Upload multiple resumes and instantly visualize top matches.  
- 📊 **Similarity Scoring** — Displays how closely each resume matches the job description.  

---

## 🏗️ Project Structure  

```bash
project_root/
├── app.py                   # Streamlit main app  
├── .env                     # API keys and environment variables  
├── requirements.txt  
├── src/  
│   ├── config/              # Config settings (model names, paths)  
│   ├── data_ingestion.py    # PDF text extraction  
│   ├── embedding.py         # HuggingFace + FAISS vector store  
│   ├── retrieval.py         # Query + LLM + scoring logic  
│   ├── helper/  
│   │   └── name_clean.py    # Cleans LLM outputs  
│   └── utils/  
│       ├── logger.py        # Logging setup  
│       └── exception.py     # Custom error handling  
├── logs/                    # Daily log files  
└── data/  
    ├── resumes/             # Input PDF resumes  
    └── job_descriptions/    # Sample JD text  
```

## ⚙️ Installation

1. Clone the Repository
git clone https://github.com/<your-username>/resume-selector-rag.git
cd resume-selector-rag

2. Create and Activate Virtual Environment
python -m venv env
env\Scripts\activate     # On Windows
or
source env/bin/activate  # On macOS/Linux

3. Install Dependencies
pip install -r requirements.txt

4.Add Environment Variables
Create a .env file in the project root:
GROQ_API_KEY=your_api_key_here


🧠 Usage

Run the Streamlit App
streamlit run app.py

In the Browser UI:
Paste the Job Description in the text box.

Upload one or more Resumes (PDF format).

Select how many top resumes you want to retrieve.

Click Find Top Matches → See ranked results with similarity scores.

