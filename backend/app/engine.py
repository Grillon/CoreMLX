from fastapi.responses import JSONResponse

def query_model(payload):
    prompt = payload.get("messages", [{}])[-1].get("content", "")
    response = {
        "id": "mock-response",
        "object": "chat.completion",
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": f"You said: {prompt}"
            },
            "finish_reason": "stop"
        }],
        "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    }
    return JSONResponse(content=response)
