# backend/pipeline/pipeline.py

from backend.pipeline.preprocessing import preprocess   # ✅ ADDED
from backend.pipeline.confidence import adjust_confidence

def run_pipeline(text: str):
    text = preprocess(text)   # ✅ ADDED (preprocessing)

    text_lower = text.lower()

    # 🚨 SECURITY OVERRIDE (UNCHANGED)
    if any(word in text_lower for word in [
        "hack", "hacked", "breach", "data leak",
        "leaking", "unauthorized", "cyber attack"
    ]):
        result = {
            "category": "Security",
            "priority": "High",
            "confidence": 0.96,
            "resolution": "Escalate Immediately",
            "escalation": "Yes",
            "approval": "Required",
            "explanation": "Critical security issue detected.",
            "ai_response": "🚨 Immediate escalation required."
        }
        return adjust_confidence(result)

    # EXISTING LOGIC (UNCHANGED)
    if any(word in text_lower for word in ["payment", "refund", "charged"]):
        result = {"category": "Billing", "priority": "High", "confidence": 0.92}

    elif any(word in text_lower for word in ["login", "password", "account"]):
        result = {"category": "Account", "priority": "High", "confidence": 0.90}

    elif any(word in text_lower for word in ["crash", "error", "bug", "upload", "not working"]):
        result = {"category": "Technical", "priority": "Medium", "confidence": 0.87}

    elif any(word in text_lower for word in ["delivery", "order", "shipping"]):
        result = {"category": "Delivery", "priority": "Medium", "confidence": 0.85}

    else:
        result = {"category": "General", "priority": "Low", "confidence": 0.78}

    return adjust_confidence(result)