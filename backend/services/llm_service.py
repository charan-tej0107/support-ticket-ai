# backend/services/llm_service.py

def generate_response(data):
    try:
        category = data.get("category", "General")
        priority = data.get("priority", "Low")

        if category == "Billing":
            return f"This seems like a billing issue. Please check your transactions or contact support. Priority level: {priority}."

        elif category == "Account":
            return f"This appears to be an account issue. Try resetting your password or verifying your login details. Priority level: {priority}."

        elif category == "Technical":
            return f"This looks like a technical problem. Please try restarting the app or updating it. Priority level: {priority}."

        elif category == "Delivery":
            return f"Your issue is related to delivery. Please track your order or contact support. Priority level: {priority}."

        elif category == "Security":   # ✅ ADDED (IMPORTANT)
            return "🚨 Security alert detected. Our team has been notified and this issue is being handled with highest priority."

        else:
            return f"This is a general inquiry. Please contact support for more information. Priority level: {priority}."

    except Exception as e:
        print("LLM Error:", e)
        return "Unable to generate response at the moment."