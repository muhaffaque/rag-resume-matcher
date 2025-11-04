import sys
from PyPDF2 import PdfReader
from Pathlib import Path
from src.utils.logger import get_logger
from src.utils.exception import CustomException

logger = get_logger(__name__)

def read_file(file):
    try:
        text = ""
        if hasattr(file, "read"):  #if uploaded through sreamlit
            from io import BytesIO
            file.seek(0)
            pdf_reader = PdfReader(BytesIO(file.read()))
            for page in pdf_reader.pages:
                text+=page.extract_text() or ""
        else:  # if it's a path
            with open(file, "rb") as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() or ""
                   
        logger.info(f"✅ Extracted text from {getattr(file, 'name', file)}")
        return text


    except Exception as e:
        logger.error(f"❌ Error reading PDF {getattr(file, 'name', file)}: {e}")
        raise CustomException(e, sys)

