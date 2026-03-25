# backend/services/embedding_service.py

def get_embedding(text):
    return [ord(c) for c in text[:10]]