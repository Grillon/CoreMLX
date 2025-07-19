# CoreMLX
## Core ML eXtensible

**Chatbot local, modulaire et évolutif** — conçu pour servir de socle libre à des démonstrations MLOps, DevOps, Docker et CI/CD.

## 🎯 Objectif

Créer un système d’inférence local basé sur un modèle préentraîné encapsulé dans une API compatible OpenAI, avec une interface utilisateur simple. Le tout doit être modulaire, documenté, exécutable en local et évolutif vers des fonctionnalités avancées (RAG, fine-tuning, observabilité).

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
- [ ] Pitch + vidéo de démonstration

---

## 📚 Contexte du modèle

CoreMLX utilise le modèle **OpenHermes 2.5** (base Mistral), développé par **Nous Research**, un collectif initialement actif dans l’écosystème blockchain via le projet **Bittensor**.

Faute de soutien suffisant malgré la qualité de leur contribution, ils ont quitté l’écosystème crypto pour se concentrer sur la création de modèles libres, précis et expressifs. OpenHermes est le fruit de cette transition.

Cette trajectoire — quitter un environnement instable pour structurer un socle technique ouvert — résonne avec l’intention de ce projet.

## 🧪 Test du modèle

* installer llama.cpp

> Le plus simple est de prendre directement les binaires. Le plus sûr et souverain : compiler depuis les sources.


***Si vous faite le choix de compiler alors vous pouvez utiliser les scripts setup.sh et mybin.sh***

```bash
cd scripts
./scripts/setup.sh # clone llama.cpp le build et ensuite telecharge le model q4
./scripts/mybin.sh -i $dossier_build_bin_llamacpp # installe les binaires compilés ; passer le chemin en 2e argument
```

* lancer le model

```bash
# si vous n'avez pas utilisé les scripts
mkdir models
cd models
wget https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF/resolve/main/openhermes-2.5-mistral-7b.Q4_K_M.gguf
cd ..
# Ici on lance le serveur du model
llama-server -m models/openhermes-2.5-mistral-7b.Q4_K_M.gguf --port 8001
```

* tester avec curl + jq (dans votre repo de distribution favori)

```bash
prompt='Combien les humains ont-il de doigts ?'
curl -s -X POST http://localhost:8001/completion \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"$prompt\", \"n_predict\": 64}" \
  | jq -r '.content'
```

## 🔓 Licence

MIT — réutilisable librement avec attribution.

## 🔗 Liens 

* model full precision  : [OpenHermes-2.5-Mistral-7B sur huggingface](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B)
* model quantisé orienté cpu: [OpenHermes-2.5-Mistral-7B-GGUF sur huggingface](TheBloke/OpenHermes-2.5-Mistral-7B-GGUF)
* llama.cpp: [llama.cpp](https://github.com/ggml-org/llama.cpp)
* fastAPI: [FastAPI](https://fastapi.tiangolo.com/)
* streamlite: [Streamlite](https://streamlit.io/#install)

* (à venir)

- Démo vidéo
- Documentation technique
- Présentation pédagogique
