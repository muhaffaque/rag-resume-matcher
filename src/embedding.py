import os,sys

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from src.utils.logger import get_logger
from src.utils.exception import CustomException
from src.config.config import EMBED_MODEL

logger = get_logger(__name__)

def build_vectorstore(texts, metadata):
    try:
        if not texts:
            raise ValueError("No resume text provided for embedding.")
        
        # # Create text splitter (for chunking)
        # text_splitter = RecursiveCharacterTextSplitter(
        #     chunk_size=1000,      
        #     chunk_overlap=100,   
        #     separators=["\n\n", "\n", ".", " "]
        # )
        embedding = HuggingFaceEmbeddings(model_name=EMBED_MODEL) 
        vectorstore = FAISS.from_texts(texts, embedding, metadatas=metadata) 
        logger.info("✅ FAISS index built successfully")
        return vectorstore 
    
    except Exceptionas e:
        logger.error(f"❌ Error building vectorstore: {e}") 
        raise CustomException(e, sys)



