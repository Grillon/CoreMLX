import streamlit as st
import requests
import re

def clean_markdown(text):
    # Supprime les titres Markdown (lignes commençant par #)
    return re.sub(r'^#+\s*', '', text, flags=re.MULTILINE).strip()


st.title("CoreMLX - Chat minimal")

if "history" not in st.session_state:
    st.session_state["history"] = []

user_input = st.text_input("Vous :", "")

if st.button("Envoyer") and user_input:
    st.session_state["history"].append({"role": "user", "content": user_input})

    response = requests.post(
        "http://localhost:8000/v1/chat/completions",
        json={
            "model": "openhermes-2.5-q4_k_m",
            "messages": st.session_state["history"]
        }
    )
    assistant_msg = response.json()["choices"][0]["message"]["content"]
    st.session_state["history"].append({"role": "assistant", "content": assistant_msg})

for msg in st.session_state["history"]:
    label = "Vous" if msg["role"] == "user" else "CoreMLX"
    st.markdown(f"**{label}** : {clean_markdown(msg['content'])}")

