from backend.services.llm_service import generate_response

def generate_solution(data, similar_ticket=None):
    if similar_ticket:
        return f"✅ Reused Solution: {similar_ticket.get('response')}"
    
    from backend.services.llm_service import generate_response
    return generate_response(data)