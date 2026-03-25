from services.llm_service import generate_ai_solution

def generate_solution(query, similar):
    if similar:
        return similar["solution"]

    # fallback to AI
    return generate_ai_solution(query)