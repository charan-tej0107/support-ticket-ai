def adjust_confidence(data):
    try:
        # safety check
        if not isinstance(data, dict):
            return {
                "category": "General",
                "priority": "Low",
                "confidence": 78.0
            }

        confidence = data.get("confidence", 0.5)

        # small smart boosts
        if data.get("category") == "Security":
            confidence += 0.1
        elif data.get("category") == "Account":
            confidence += 0.05

        # clamp between 0 and 1
        confidence = min(confidence, 1.0)

        # convert to percentage
        data["confidence"] = round(confidence * 100, 2)

        return data

    except Exception as e:
        print("Confidence Error:", e)
        return {
            "category": "Error",
            "priority": "Low",
            "confidence": 0
        }