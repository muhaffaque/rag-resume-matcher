from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.helper.name_clean import clean_output
from src.utils.logger import get_logger
from src.embedding import build_vectorstore
from src.data_ingestion import read_pdf
from src.config.config import GROQ_API_KEY
from dotenv import load_dotenv
import os

logger = get_logger(__name__)

def retrieve_top_resumes(jd_text, uploaded_files, k=3):
    resumes_texts, metadata = [], []
    for file in uploaded_files:
        text = read_pdf(file)
        resumes_texts.append(text)
        metadata.append({"file_name": file.name})
    
    vectorstore = build_vectorstore(resumes_texts, metadata)

    if not GROQ_API_KEY:
        raise ValueError("❌ GROQ_API_KEY not found in .env file.")
    logger.info("✅ GROQ API is connected")

    llm = ChatGroq(model="qwen/qwen3-32b", groq_api_key=GROQ_API_KEY, temperature=0.3)

    prompt = PromptTemplate(
        input_variables=["resume_text"],
        template=(
            "You are an expert information extractor.\n"
            "Your ONLY job is to extract the **candidate’s full name** from the text below.\n"
            "Do not include anything else — no explanations, no reasoning, no thinking tags.\n"
            "Return only the name as plain text.\n\n"
            "Resume:\n{resume_text}\n\n"
            "Full name:" 
        )
    )

    extract_name_chain = prompt | llm | StrOutputParser()

    # ✅ Now retrieve with scores
    results = vectorstore.similarity_search_with_score(jd_text, k=k)

    output = []
    for doc, score in results:
        raw_name = extract_name_chain.invoke({"resume_text": doc.page_content[:1000]}).strip()
        name = clean_output(raw_name)
        output.append({
            "file_name": doc.metadata.get("file_name", "Unknown"),
            "candidate_name": name,
            "similarity_score": round(score, 4)
        })

    # ✅ Sort ascending (lower = more similar)
    output = sorted(output, key=lambda x: x["similarity_score"])

    logger.info("✅ Retrieved top resumes successfully")
    return output

