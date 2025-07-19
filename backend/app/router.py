from fastapi import APIRouter
from .schemas import ChatRequest
from .engine import query_model

router = APIRouter()

@router.post("/v1/chat/completions")
def chat_completion(payload: ChatRequest):
    raw = query_model(payload)

    return {
        "id": "coremlx-response",
        "object": "chat.completion",
        "model": raw["model"]+" en réalité mistral7B_Q4_K_M",
        "choices": [{
            "index": raw["index"],
            "message": {
                "role": "assistant",
                "content": raw["content"]
            },
            "finish_reason": raw["finish_reason"]
        }],
        "usage": {
            "prompt": raw["prompt"],
            "prompt_tokens": raw["tokens_evaluated"],
            "completion_tokens": raw["tokens_predicted"],
            "total_tokens": raw["tokens_predicted"]+raw["tokens_evaluated"]
        },
        "timings": {
        "prompt_ms": raw["prompt_ms"],
        "predicted_ms": raw["timings"].get("predicted_ms", 0.0),
        "latency_ms": raw["timings"].get("predicted_ms", 0.0)
}

    }

