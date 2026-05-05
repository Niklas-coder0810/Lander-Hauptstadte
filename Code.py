import streamlit as st
import random
import requests

# -----------------------------
# 196 Länder + Hauptstädte
# -----------------------------
countries = {
    "Afghanistan": "Kabul",
    "Albanien": "Tirana",
    "Algerien": "Algier",
    "Andorra": "Andorra la Vella",
    "Angola": "Luanda",
    "Argentinien": "Buenos Aires",
    "Armenien": "Jerewan",
    "Australien": "Canberra",
    "Österreich": "Wien",
    "Aserbaidschan": "Baku",
    "Bahamas": "Nassau",
    "Bahrain": "Manama",
    "Bangladesch": "Dhaka",
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
    "Dominikanische Republik": "Santo Domingo",
    "Ecuador": "Quito",
    "Ägypten": "Kairo",
    "El Salvador": "San Salvador",
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
    "Kasachstan": "Astana",
    "Kenia": "Nairobi",
    "Kolumbien": "Bogotá",
    "Kroatien": "Zagreb",
    "Kuba": "Havanna",
    "Kuwait": "Kuwait-Stadt",
    "Laos": "Vientiane",
    "Lettland": "Riga",
    "Libanon": "Beirut",
    "Litauen": "Vilnius",
    "Luxemburg": "Luxemburg",
    "Malaysia": "Kuala Lumpur",
    "Malediven": "Malé",
    "Mexiko": "Mexiko-Stadt",
    "Mongolei": "Ulaanbaatar",
    "Marokko": "Rabat",
    "Nepal": "Kathmandu",
    "Niederlande": "Amsterdam",
    "Neuseeland": "Wellington",
    "Nigeria": "Abuja",
    "Nordkorea": "Pjöngjang",
    "Norwegen": "Oslo",
    "Oman": "Maskat",
    "Pakistan": "Islamabad",
    "Peru": "Lima",
    "Philippinen": "Manila",
    "Polen": "Warschau",
    "Portugal": "Lissabon",
    "Rumänien": "Bukarest",
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
    "Vietnam": "Hanoi",
    "Zypern": "Nikosia"
}

# -----------------------------
# Bild holen (Wikipedia)
# -----------------------------
def get_image(country):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{country}"
        r = requests.get(url).json()
        return r["thumbnail"]["source"]
    except:
        return None

# -----------------------------
# Session State
# -----------------------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "level" not in st.session_state:
    st.session_state.level = 1

if "country" not in st.session_state:
    st.session_state.country = random.choice(list(countries.keys()))

if "options" not in st.session_state:
    st.session_state.options = []

if "correct" not in st.session_state:
    st.session_state.correct = ""

# -----------------------------
# Neue Frage
# -----------------------------
def new_question():
    country = random.choice(list(countries.keys()))
    correct = countries[country]

    wrong = random.sample(
        [v for v in countries.values() if v != correct],
        2
    )

    options = wrong + [correct]
    random.shuffle(options)

    st.session_state.country = country
    st.session_state.correct = correct
    st.session_state.options = options

# -----------------------------
# Erste Frage laden
# -----------------------------
if st.session_state.options == []:
    new_question()

# -----------------------------
# UI
# -----------------------------
st.title("🌍 Geo Quiz (196 Länder)")
st.write("Welche Hauptstadt gehört zum Land?")

st.subheader(st.session_state.country)

img = get_image(st.session_state.country)
if img:
    st.image(img, use_container_width=True)

# -----------------------------
# Antwort prüfen
# -----------------------------
def check(ans):
    if ans == st.session_state.correct:
        st.success("Richtig! +1 Punkt 🎉")
        st.session_state.score += 1
    else:
        st.error(f"Falsch ❌ Richtige Antwort: {st.session_state.correct}")
        if st.session_state.score > 0:
            st.session_state.score -= 1

    st.session_state.level = st.session_state.score // 25 + 1

# -----------------------------
# Buttons A B C
# -----------------------------
cols = st.columns(3)

for i, opt in enumerate(st.session_state.options):
    with cols[i]:
        if st.button(opt):
            check(opt)

# -----------------------------
# Nächste Frage
# -----------------------------
if st.button("➡️ Nächstes Land"):
    new_question()

# -----------------------------
# Score & Level
# -----------------------------
st.markdown("---")
st.write(f"🏆 Punkte: {st.session_state.score}")
st.write(f"📈 Level: {st.session_state.level}")

if st.session_state.score > 0 and st.session_state.score % 25 == 0:
    st.success("🔥 LEVEL UP!")
    st.balloons()
