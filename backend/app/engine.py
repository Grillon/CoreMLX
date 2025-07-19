import requests
def query_model(payload):
    prompt = payload.messages[-1].content
    res = requests.post(
        "http://localhost:8001/completion",
        json={"prompt": prompt, "n_predict": 128},
        timeout=60
    )
    data = res.json()
    finish_reason = {
    "limit": "length",
    "stopword": "stop",
    "user": "user_stop",
    "": "unknown"
}.get(data.get("stop_type", ""), "unknown")

    return {
        "content": data.get("content", ""),
        "model": data.get("model", ""),
        "tokens_predicted": data.get("tokens_predicted", 0),
        "tokens_evaluated": data.get("tokens_evaluated", 0),
        "timings": data.get("timings", {}),
        "index": data.get("index",""),
        "prompt_ms": data.get("timings", {}).get("prompt_ms", 0.0),
        "prompt": data.get("prompt",""),
        "finish_reason": finish_reason
    }
