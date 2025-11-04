import re 

def clean_output(text: str) -> str:
    """
    Clean unwanted tags or reasoning traces like <think></think> from the LLM output.
    """
    if not text:
        return "Unknown"
    
    # Remove <think>...</think> blocks or any HTML-style tags
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    
    # Remove any remaining brackets, multiple spaces, or line breaks
    text = re.sub(r"\s+", " ", text).strip()
    
    # Remove prefixes like "Full name:" if accidentally returned
    text = re.sub(r"(?i)^full name[:\-]*\s*", "", text).strip()

    return text
