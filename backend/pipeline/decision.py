def make_decision(data):
    category = data["category"]
    confidence = data["confidence"]

    if category == "Security":
        priority = "Critical"
        decision = "Auto Escalated"   # 🔥 better wording

    elif confidence > 80:
        priority = "High"
        decision = "Auto Resolved"

    else:
        priority = "Medium"
        decision = "Review Suggested"

    return {
        **data,
        "priority": priority,
        "decision": decision
    }