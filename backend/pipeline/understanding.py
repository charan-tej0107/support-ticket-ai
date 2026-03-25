from transformers import pipeline

classifier = pipeline("zero-shot-classification")

CATEGORIES = ["Access", "Network", "Billing", "Security", "General"]

def understand(text: str):
    result = classifier(text, CATEGORIES)

    return {
        "category": result["labels"][0],
        "confidence": round(result["scores"][0] * 100, 2)
    }