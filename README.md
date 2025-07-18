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
- [ ] Choix du modèle
- [ ] Backend minimal
- [ ] Frontend simple
- [ ] Pitch + vidéo de démonstration

## 🔓 Licence

MIT — réutilisable librement avec attribution.

## 🔗 Liens (à venir)

- Démo vidéo
- Documentation technique
- Présentation pédagogique
