feedback_store = []

def add_feedback(ticket_id, rating):
    feedback_store.append({
        "ticket_id": ticket_id,
        "rating": rating
    })

def get_feedback():
    return feedback_store