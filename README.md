# CoreMLX
🧠 Infrastructure IA open source — reproductible, modulaire, sans dépendance cloud.

## Core ML eXtensible

**Chatbot local, modulaire et évolutif** — conçu pour servir de socle libre à des démonstrations MLOps, DevOps, Docker et CI/CD.

## 🎯 Objectif

Créer un système d’inférence local basé sur un modèle préentraîné encapsulé dans une API compatible OpenAI, avec une interface utilisateur simple. Le tout doit être modulaire, documenté, exécutable en local et évolutif vers des fonctionnalités avancées (RAG, fine-tuning, observabilité).

## 🚀 Démarrage rapide

```bash
# Structure des scripts :
# ./scripts/
# ├── 01_create_venv.sh        # Crée l'environnement virtuel
# ├── 02_install_prerequis.sh  # Installe les dépendances Python
# ├── 03_install_model.sh      # Télécharge le modèle GGUF
# ├── 04_build_llamacpp.sh     # (Optionnel) Clone et compile llama.cpp
# ├── 05_run_model.sh          # Lance le modèle en local
# └── mybin.sh                 # Installe les binaires dans ~/.local/bin

# Chaque script a une fonction simple. Reprise possible en cas d’échec.

git clone https://github.com/Grillon/CoreMLX.git
# perso je prefere ssh
# git clone git@github.com:Grillon/CoreMLX.git
cd CoreMLX

./scripts/01_create_venv.sh
./scripts/02_install_prerequis.sh
./scripts/03_install_model.sh

# (Optionnel, pour compiler et installer llama.cpp)
./scripts/04_build_llamacpp.sh
./scripts/mybin.sh -i $PWD/llama.cpp/build/bin/

# Lancement modèle
./scripts/05_run_model.sh

# (ou directement)
llama-server -m ./models/openhermes-2.5-mistral-7b.Q4_K_M.gguf --port 8001
```
Dans un autre terminal

```bash
source .venv/bin/activate
fastapi dev backend/app/main.py
```

On teste dans un troisième terminal : 

```bash
# test llama.cpp
curl -s -X POST http://localhost:8001/completion \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Combien les humains ont-il de doigts ?", "n_predict": 64}' | jq -r '.content'

# test fastapi

curl -X 'POST' \
  'http://127.0.0.1:8000/v1/chat/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "messages": [
    {
      "role": "user",
      "content": "Combien de doigts les humains ont-ils?"
    }
  ]
}'
```

Ou, en Python test llama.cpp :

```python
import requests

prompt = "Combien les humains ont-il de doigts ?"
response = requests.post(
    "http://localhost:8001/completion",
    json={"prompt": prompt, "n_predict": 64}
)
print(response.json()["content"])
```

en python test fastAPI :

```python
import requests

data = {
  "messages": [
    {
      "role": "user",
      "content": "Combien de doigts les humains ont-ils?"
    }
  ]
}

response = requests.post(
  "http://127.0.0.1:8000/v1/chat/completions",
  json=data
)

print(response.json())
```

Dans un autre quatrième terminal on lance le front : 

```bash
source .venv/bin/activate
streamlit run frontend/app.py
```

## 🧱 Architecture (Phase 1)

- `backend/` → FastAPI exposant `/v1/chat/completions`
- `model/` → wrapper autour d’un modèle local (e.g. `llama.cpp`, `phi-2`)
- `frontend/` → Streamlit, interface de chat simple

## ✅ Avancement

Phase 1 en cours :
- [x] Structuration projet
- [x] Choix du modèle
- [x] Backend minimal
- [x] Frontend simple
- [x] Pitch + vidéo de démonstration

---

## 📚 Contexte du modèle

CoreMLX utilise le modèle **OpenHermes 2.5** (base Mistral), développé par **Nous Research**, un collectif initialement actif dans l’écosystème blockchain via le projet **Bittensor**.

Faute de soutien suffisant malgré la qualité de leur contribution, ils ont quitté l’écosystème crypto pour se concentrer sur la création de modèles libres, précis et expressifs. OpenHermes est le fruit de cette transition.

Cette trajectoire — quitter un environnement instable pour structurer un socle technique ouvert — résonne avec l’intention de ce projet.

## 🧪 Configs testées

|Marque|modèle|CPU|GPU|RAM|OS|
|HP|Elitebook840 G6|Corei58thGen|None|32Go|Ubuntu 24.04.2 LTS|

## 📺 Démo

[Vidéo de présentation (1min15)](https://youtu.be/7Kb_3M7986I)

## 🔓 Licence

MIT — réutilisable librement avec attribution.

## 🔗 Liens 

* model full precision  : [OpenHermes-2.5-Mistral-7B sur huggingface](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B)
* model quantisé orienté cpu: [OpenHermes-2.5-Mistral-7B-GGUF sur HuggingFace](https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF)
* llama.cpp: [llama.cpp](https://github.com/ggml-org/llama.cpp)
* fastAPI: [FastAPI](https://fastapi.tiangolo.com/)
* streamlite: [Streamlite](https://streamlit.io/#install)


## 📺 À venir

- 📘 Documentation technique
- 🧑 Présentation pédagogique

## 🧭 Phase actuelle

Cette version correspond à la **Phase 1** de CoreMLX :  
> Un chatbot local, basé sur un modèle Mistral, encapsulé dans une API FastAPI compatible OpenAI, avec une interface Streamlit.

Les prochaines phases incluront :  
- CI/CD  
- Observabilité  
- RAG  
- Fine-tuning  
- Changement de modèle à chaud  
