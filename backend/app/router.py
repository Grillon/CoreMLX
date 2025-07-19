from fastapi import APIRouter
from .engine import query_model
from .schemas import ChatRequest  # si séparé

router = APIRouter()

@router.post("/v1/chat/completions")
async def chat_completion(payload: ChatRequest):
    return query_model(payload.dict())
