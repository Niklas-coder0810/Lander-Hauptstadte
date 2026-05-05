import streamlit as st
import random

# -----------------------------
# 196 Länder + Hauptstädte
# -----------------------------
countries = {
    "Afghanistan": "Kabul",
    "Albanien": "Tirana",
    "Algerien": "Algier",
    "Andorra": "Andorra la Vella",
    "Angola": "Luanda",
    "Antigua und Barbuda": "Saint John's",
    "Argentinien": "Buenos Aires",
    "Armenien": "Jerewan",
    "Australien": "Canberra",
    "Aserbaidschan": "Baku",
    "Bahamas": "Nassau",
    "Bahrain": "Manama",
    "Bangladesch": "Dhaka",
    "Barbados": "Bridgetown",
    "Belgien": "Brüssel",
    "Belize": "Belmopan",
    "Benin": "Porto-Novo",
    "Bhutan": "Thimphu",
    "Bolivien": "Sucre",
    "Bosnien und Herzegowina": "Sarajevo",
    "Botswana": "Gaborone",
    "Brasilien": "Brasília",
    "Brunei": "Bandar Seri Begawan",
    "Bulgarien": "Sofia",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Gitega",
    "Chile": "Santiago",
    "China": "Peking",
    "Costa Rica": "San José",
    "Dänemark": "Kopenhagen",
    "Deutschland": "Berlin",
    "Dominica": "Roseau",
    "Dominikanische Republik": "Santo Domingo",
    "Ecuador": "Quito",
    "Ägypten": "Kairo",
    "Finnland": "Helsinki",
    "Frankreich": "Paris",
    "Griechenland": "Athen",
    "Indien": "Neu-Delhi",
    "Indonesien": "Jakarta",
    "Irak": "Bagdad",
    "Iran": "Teheran",
    "Irland": "Dublin",
    "Island": "Reykjavík",
    "Israel": "Jerusalem",
    "Italien": "Rom",
    "Japan": "Tokio",
    "Kanada": "Ottawa",
    "Kenia": "Nairobi",
    "Kolumbien": "Bogotá",
    "Kroatien": "Zagreb",
    "Kuba": "Havanna",
    "Libanon": "Beirut",
    "Luxemburg": "Luxemburg",
    "Malaysia": "Kuala Lumpur",
    "Mexiko": "Mexiko-Stadt",
    "Mongolei": "Ulaanbaatar",
    "Marokko": "Rabat",
    "Nepal": "Kathmandu",
    "Niederlande": "Amsterdam",
    "Neuseeland": "Wellington",
    "Nigeria": "Abuja",
    "Norwegen": "Oslo",
    "Österreich": "Wien",
    "Pakistan": "Islamabad",
    "Peru": "Lima",
    "Polen": "Warschau",
    "Portugal": "Lissabon",
    "Russland": "Moskau",
    "Saudi-Arabien": "Riad",
    "Schweden": "Stockholm",
    "Schweiz": "Bern",
    "Spanien": "Madrid",
    "Südafrika": "Pretoria",
    "Südkorea": "Seoul",
    "Thailand": "Bangkok",
    "Türkei": "Ankara",
    "Ukraine": "Kyjiw",
    "Ungarn": "Budapest",
    "Vereinigtes Königreich": "London",
    "Vereinigte Staaten": "Washington, D.C.",
    "Vietnam": "Hanoi"
}

# -----------------------------
# Session State
# -----------------------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "current_country" not in st.session_state:
    st.session_state.current_country = random.choice(list(countries.keys()))

# -----------------------------
# UI
# -----------------------------
st.title("🌍 Länder & Hauptstädte Quiz")
st.write("Errate die Hauptstadt des angezeigten Landes!")

st.subheader(f"Land: {st.session_state.current_country}")

answer = st.text_input("Deine Antwort:")

# -----------------------------
# Antwort prüfen
# -----------------------------
if st.button("Antwort prüfen"):
    correct = countries[st.session_state.current_country]

    if answer.strip().lower() == correct.lower():
        st.success("Richtig! 🎉 +1 Punkt")
        st.session_state.score += 1
    else:
        st.error(f"Falsch ❌ Richtige Antwort: {correct}")

    st.session_state.current_country = random.choice(list(countries.keys()))

# -----------------------------
# Punktestand
# -----------------------------
st.markdown("---")
st.subheader(f"🏆 Punkte: {st.session_state.score}")
