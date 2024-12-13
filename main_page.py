import streamlit as st

st.set_page_config(layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Login Seite")
    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")
    if st.button("Log in"):
        if username and password:  # Überprüfung, ob etwas eingetragen wurde
            st.session_state.logged_in = True
            st.success("Erfolgreich eingeloggt!")
            st.rerun()  # Seite neu laden, um den Zustand zu aktualisieren
        else:
            st.error("Bitte Benutzername und Passwort eingeben")


def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

#Pages
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

start_page = st.Page("Projekt\start_page.py", title="Home", icon=":material/home:", default=True)
about_page = st.Page("Projekt\\about_page.py", title="About", icon=":material/info:")
drivers_page = st.Page("Projekt\drivers_page.py", title="Fahrer und Teams")
gp_page = st.Page("Projekt\gp_page.py", title="Übersicht")
track_page = st.Page("Projekt\\track_page.py", title="Rundenlänge")
speed_page = st.Page("Projekt\speed_page.py", title="Geschwindigkeitsvergleich")
besch_page = st.Page("Projekt\\turns_page.py", title="Visualisierung Zentripetalbeschleunigung")

#Loginlogik
if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Home": [start_page, logout_page, about_page],
            "Fahrer und Teams": [drivers_page],
            "Analyse Q3 Silverstone 2024": [gp_page, track_page, speed_page, besch_page],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()