#!/bin/bash

# Créer le dossier modèle
mkdir -p models

# Télécharger llama.cpp si non présent
if [ ! -d "llama.cpp" ]; then
  git clone https://github.com/ggerganov/llama.cpp.git
  cd llama.cpp && cmake -B build && cmake --build build --config Release && cd ..
fi

# Télécharger le modèle (Q4_K_M)
MODEL_URL="https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF/resolve/main/openhermes-2.5-mistral-7b.Q4_K_M.gguf"
wget -nc -O models/openhermes.q4_k_m.gguf "$MODEL_URL"

