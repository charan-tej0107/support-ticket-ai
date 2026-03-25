# backend/services/database_service.py

# ✅ DEFINE THIS AT TOP (IMPORTANT)
tickets_db = []

def save_ticket(ticket):
    tickets_db.append(ticket)

def get_tickets():
    return tickets_db

# 🔥 FIXED FUNCTION
def detect_issue_spike():
    count = {}

    for t in tickets_db:   # ✅ NOW WORKS
        cat = t["category"]
        count[cat] = count.get(cat, 0) + 1

    return {k: v for k, v in count.items() if v > 3}