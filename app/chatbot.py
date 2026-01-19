from fastapi import APIRouter, HTTPException
from app.schemas import ChatRequest
from app.security import enforce_security
from app.kb_search import search_kb
import logging

router = APIRouter()

logging.basicConfig(
    filename="app/logs/chatbot.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@router.post("/")
def chat(request: ChatRequest):
    logging.info("Chat request received")

    if not enforce_security(request.message):
        logging.warning("Blocked malicious input")
        raise HTTPException(status_code=403, detail="Request not allowed")

    kb_results = search_kb(request.message)

    if kb_results:
        return {"response": " ".join(kb_results)}

    return {
        "response": (
            "I’m Pinewood Clinic Bot. I can help with general clinic information, "
            "appointment guidance, or connect you with a representative."
        )
    }










