#!/bin/bash

# Télécharger llama.cpp si non présent
if [ ! -d "llama.cpp" ]; then
  git clone https://github.com/ggerganov/llama.cpp.git
  cd llama.cpp && cmake -B build && cmake --build build --config Release && cd ..
fi
