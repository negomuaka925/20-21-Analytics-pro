
import streamlit as st
from datetime import date, timedelta

st.set_page_config(
    page_title="20/21 Analytics Pro",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.stApp {
    background: #0b1020;
    color: #f1f5f9;
}
[data-testid="stSidebar"] {
    background: #111827;
}
h1, h2, h3 {
    color: #f8fafc;
}
div[data-testid="stMetric"] {
    background: #151e30;
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #28354a;
}
div.stButton > button {
    background: #f97316;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: bold;
}
.small-note {
    color: #9ca3af;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("# ⚽ 20/21")
st.sidebar.caption("ANALYTICS PRO")
st.sidebar.divider()

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Tableau de bord",
        "Calendrier mondial",
        "Analyse 20/21",
        "Performances",
        "Paramètres",
    ],
)

st.sidebar.divider()
st.sidebar.caption("Version 0.1.0 · Prototype")

st.title("20/21 Analytics Pro")
st.write("La donnée d'abord. La probabilité ensuite.")

st.info(
    "Prototype initial : le fournisseur de données football "
    "n'est pas encore connecté. Aucune prédiction réelle "
    "n'est générée à ce stade."
)

today = date.today()

if page == "Tableau de bord":
    st.subheader("Vue générale")

    col1, col2, col3 = st.columns(3)
    col1.metric("Matchs disponibles", "—")
    col2.metric("Analyses vérifiées", "0")
    col3.metric("Précision mesurée", "En attente")

    st.divider()
    st.subheader("Centre d'analyse")

    st.write(
        "Notre système préparera ici les rencontres "
        "du jour, les probabilités des codes 20 et 21 "
        "et les matchs nécessitant une analyse approfondie."
    )

    st.warning(
        "La précision supérieure à 70 % reste un objectif "
        "à vérifier sur des prédictions enregistrées "
        "avant les matchs."
    )

elif page == "Calendrier mondial":
    st.subheader("Calendrier des compétitions")

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(
            "Du",
            value=today,
            key="start_date",
        )

    with col2:
        end_date = st.date_input(
            "Au",
            value=today + timedelta(days=3),
            key="end_date",
        )

    if start_date > end_date:
        st.error("La date de début doit précéder la date de fin.")
    else:
        st.caption(
            f"Période sélectionnée : {start_date} au {end_date}"
        )

        st.info(
            "Le calendrier mondial apparaîtra ici après "
            "la connexion à l'API football. La couverture "
            "dépendra des compétitions disponibles chez "
            "notre fournisseur."
        )

elif page == "Analyse 20/21":
    st.subheader("Analyse d'une rencontre")

    st.write(
        "Le moteur calculera trois probabilités : "
        "code 20, code 21 et égalité."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Code 20", "—")
    col2.metric("Code 21", "—")
    col3.metric("Égalité", "—")

    st.info(
        "Aucune probabilité ne sera affichée comme réelle "
        "avant l'intégration et la validation du modèle."
    )

elif page == "Performances":
    st.subheader("Historique des prédictions")

    col1, col2, col3 = st.columns(3)
    col1.metric("Prédictions enregistrées", "0")
    col2.metric("Résultats évalués", "0")
    col3.metric("Taux de réussite", "—")

    st.write(
        "Les résultats réels seront comparés aux prévisions "
        "horodatées, sans modifier rétroactivement les choix."
    )

elif page == "Paramètres":
    st.subheader("Configuration")

    st.write("État du système")

    st.markdown("- Interface : prête")
    st.markdown("- Fournisseur football : non connecté")
    st.markdown("- Moteur statistique : à construire")
    st.markdown("- Base de données : à configurer")
    st.markdown("- Abonnements : à intégrer")

    st.caption(
        "Les clés API seront configurées dans les secrets "
        "de l'hébergement, jamais dans le code public."
    )

st.divider()
st.caption(
    "20/21 Analytics Pro · Analyse statistique du football "
    "· Les probabilités ne garantissent aucun résultat."
)
