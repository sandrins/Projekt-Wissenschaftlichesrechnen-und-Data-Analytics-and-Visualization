import streamlit as st
import helper

st.set_page_config(layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Login Seite")
    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")
    if st.button("Log in"):
        if username=='test' and password=='test':  # Überprüfung, ob etwas eingetragen wurde
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

## Home
start_page = st.Page("start_page.py", title="Home", icon=":material/home:", default=True)
about_page = st.Page("about_page.py", title="About", icon=":material/info:")
projektarbeit_page = st.Page("projektarbeit_page.py", title="Projektarbeit")

## Die Formel 1
formel1_page = st.Page("formel1_page.py", title="Die Formel 1 - Die Königsklasse des Motorsports")
drivers_page = st.Page("drivers_page.py", title="Fahrer und Teams")

## Analyse Q3 Silverstone 2024
gp_page = st.Page("gp_page.py", title="Übersicht")
track_page = st.Page("track_page.py", title="Rundenlänge")
speed_page = st.Page("speed_page.py", title="Geschwindigkeitsvergleich")
krümmungsradius_page = st.Page("turns_page.py", title="Krümmungsradius")
az_fz_page = st.Page("a_z__f_z_page.py", title="Zentripetalbeschleunigung und -kraft")
haftreibung_page = st.Page("haftreibungskoeffizient_page.py", title="Haftreibungskoeffizient")
faero_page = st.Page("F_aero_page.py", title="Aerodynamische Kraft")


#Loginlogik
if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Home": [start_page, logout_page, about_page, projektarbeit_page],
            "Die Formel 1": [formel1_page, drivers_page],
            "Analyse Q3 Silverstone 2024": [gp_page,
                                            track_page,
                                            speed_page,
                                            krümmungsradius_page,
                                            az_fz_page,
                                            haftreibung_page,
                                            faero_page],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()