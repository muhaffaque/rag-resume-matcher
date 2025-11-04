from dotenv import load_dotenv
import os
load_dotenv()

GROQ_API_KEY = os.get_env("GROQ_API_KEY")
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"