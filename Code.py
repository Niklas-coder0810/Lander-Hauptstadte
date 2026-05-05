import streamlit as st
import random
import requests

# -----------------------------
# 🌍 196 LÄNDER + HAUPTSTÄDTE
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
    "Kasachstan": "Astana",
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
    "Simbabwe": "Harare",
    "Syrien": "Damaskus",
    "Irland": "Dublin",
    "Island": "Reykjavík",
    "Kenia": "Nairobi",
    "Ghana": "Accra",
    "Marokko": "Rabat",
    "Äthiopien": "Addis Abeba",
    "Tansania": "Dodoma",
    "Uganda": "Kampala",
    "Zentralafrikanische Republik": "Bangui",
    "Südsudan": "Juba",
    "Sudan": "Khartum"
}

# -----------------------------
# 🌄 Bilder (stabil + fallback Natur/Städte)
# -----------------------------
def get_image(country):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{country}"
        r = requests.get(url, timeout=3).json()
        if "thumbnail" in r:
            return r["thumbnail"]["source"]
    except:
        pass

    fallback = [
        "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
        "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa",
        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        "https://images.unsplash.com/photo-1469474968028-56623f02e42e"
    ]

    return random.choice(fallback)

# -----------------------------
# 🎮 STATE
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

if "msg" not in st.session_state:
    st.session_state.msg = ""

# -----------------------------
# 🔄 neue Frage
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
    st.session_state.msg = ""

# -----------------------------
# erste Frage
# -----------------------------
if not st.session_state.options:
    new_question()

# -----------------------------
# 🎨 UI HEADER
# -----------------------------
st.title("🌍 Willkommen beim Geo Quiz")
st.write("Teste dein Wissen über 196 Länder 🔥")

st.markdown("---")

st.subheader(st.session_state.country)

st.image(get_image(st.session_state.country), use_container_width=True)

# -----------------------------
# 🧠 CHECK
# -----------------------------
def check(ans):
    if ans == st.session_state.correct:
        st.session_state.score += 1
        st.session_state.msg = random.choice(["🎉 Richtig!", "🔥 Stark!", "💯 Perfekt!", "🚀 Mega!"])
    else:
        if st.session_state.score > 0:
            st.session_state.score -= 1
        st.session_state.msg = random.choice(["❌ Falsch!", "😅 Nope!", "🤔 Versuch nochmal!"])

    st.session_state.level = st.session_state.score // 25 + 1

# -----------------------------
# 🔘 BUTTONS
# -----------------------------
cols = st.columns(3)

for i, opt in enumerate(st.session_state.options):
    with cols[i]:
        if st.button(opt, key=f"{opt}-{i}"):
            check(opt)

# -----------------------------
# ➡️ NEXT
# -----------------------------
if st.button("➡️ Nächstes Land"):
    new_question()

# -----------------------------
# 📊 OUTPUT
# -----------------------------
if st.session_state.msg:
    st.subheader(st.session_state.msg)

st.write(f"🏆 Punkte: {st.session_state.score}")
st.write(f"📈 Level: {st.session_state.level}")

if st.session_state.score > 0 and st.session_state.score % 25 == 0:
    st.success("🔥 LEVEL UP!")
    st.balloons()
