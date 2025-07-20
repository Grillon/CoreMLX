#!/bin/bash
source .venv/bin/activate
llama-server -m models/openhermes-2.5-mistral-7b.Q4_K_M.gguf --port 8001
