# backend/utils/text_cleaner.py

def normalize_text(text: str) -> str:
    return text.strip().lower()