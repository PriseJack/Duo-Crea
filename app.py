
import streamlit as st
import openai

openai.api_key = st.secrets["openai_api_key"]

st.title("❤️ Générateur d'idées de contenus Instagram & TikTok")
st.subheader("Amour romantique et humoristique")

plateforme = st.selectbox("Choisis la plateforme :", ["Instagram", "TikTok", "Instagram & TikTok"])
detail = st.text_input("Sujet spécifique ou détail (optionnel)", placeholder="ex : premier rendez-vous drôle")

if st.button("Générer des idées 🚀"):
    prompt = f"""
    Tu es expert en création de contenus viraux, drôles et romantiques.
    Génère des idées courtes et précises adaptées à {plateforme}.
    Sujet : Amour romantique et humoristique.
    Détail spécifique : {detail if detail else 'aucun'}.
    Propose :
    - 3 idées pour des vidéos TikTok courtes.
    - 3 idées pour Instagram (story, reel ou carrousel).
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Tu es expert en contenus réseaux sociaux humoristiques et romantiques."},
                {"role": "user", "content": prompt}
            ]
        )
        st.markdown(response["choices"][0]["message"]["content"])
    except Exception as e:
        st.error(f"Erreur lors de la génération : {e}")
