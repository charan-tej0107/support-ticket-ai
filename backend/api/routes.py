# backend/api/routes.py

from fastapi import Request
from fastapi import APIRouter
from pydantic import BaseModel
from backend.pipeline.pipeline import run_pipeline
from backend.services.llm_service import generate_response

# ✅ EXISTING IMPORTS
from backend.services.embedding_service import get_embedding
from backend.services.database_service import save_ticket, get_tickets, detect_issue_spike
from backend.utils.logger import log

# 🔥 NEW IMPORTS
from backend.services.solution_service import generate_solution
from backend.feedback.feedback_handler import add_feedback

import uuid   # 🔥 NEW

router = APIRouter()

class TicketRequest(BaseModel):
    text: str

# 🔥 NEW MODEL FOR FEEDBACK
class FeedbackRequest(BaseModel):
    ticket_id: str
    rating: int


@router.post("/ticket")
async def create_ticket(request: TicketRequest):
    
    log("Received ticket")

    result = run_pipeline(request.text)

    confidence = result.get("confidence", 0)
    priority = result.get("priority", "Low")

    # ✅ Governance Rules
    if confidence >= 85 and priority != "High":
        resolution = "Auto-Resolved"
        escalation = "No"
        approval = "Not Required"
    else:
        resolution = "Pending Human Review"
        escalation = "Yes"
        approval = "Required"

    # ✅ Explainability
    explanation = f"Classified as {result.get('category')} based on detected keywords. Confidence score is {confidence}%."

    # ✅ Embedding
    embedding = get_embedding(request.text)

    # 🔥 Similarity Check
    stored_tickets = get_tickets()
    similar_ticket = next(
        (t for t in stored_tickets if request.text.lower() in t["input"].lower()),
        None
    )

    # 🔥 Smart Solution
    response = generate_solution(result, similar_ticket)

    # 🔥 CREATE UNIQUE ID
    ticket_id = str(uuid.uuid4())

    # ✅ Audit Log
    audit = {
        "input_text": request.text,
        "category": result.get("category"),
        "confidence": confidence,
        "decision": resolution
    }

    # ✅ Save Ticket
    ticket = {
        "ticket_id": ticket_id,   # 🔥 ADDED
        "input": request.text,
        "category": result.get("category"),
        "priority": priority,
        "confidence": confidence,
        "response": response,
        "embedding": embedding
    }

    save_ticket(ticket)

    log(f"Ticket stored: {ticket['category']}")

    # 🔥 Pattern Detection
    spikes = detect_issue_spike()

    return {
        "ticket_id": ticket_id,   # 🔥 RETURN THIS
        "category": result.get("category"),
        "priority": priority,
        "confidence": confidence,
        "ai_response": response,
        "resolution": resolution,
        "escalation": escalation,
        "approval": approval,
        "explanation": explanation,
        "audit": audit,
        "alerts": spikes,
        "engine": "Hybrid AI Pipeline v2.0"
    }


# 🔥 NEW FEEDBACK API
@router.post("/feedback")
async def submit_feedback(feedback: FeedbackRequest):
    add_feedback(feedback.ticket_id, feedback.rating)

    return {
        "message": "Feedback received successfully",
        "status": "Success"
    }