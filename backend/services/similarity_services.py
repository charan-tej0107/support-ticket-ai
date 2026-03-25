def find_similar_ticket(query, stored_tickets):
    for ticket in stored_tickets:
        if query.lower() in ticket.get("input", "").lower():
            return ticket
    return None