from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import PlainTextResponse

from app.chatbot import router as chatbot_router
from app.auth import router as auth_router

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Pinewood Clinic Bot API",
    description="Secure healthcare chatbot simulation",
    version="1.0"
)

app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    lambda r, e: PlainTextResponse("Rate limit exceeded", status_code=429)
)

app.include_router(auth_router, prefix="/auth")
app.include_router(chatbot_router, prefix="/chat")






