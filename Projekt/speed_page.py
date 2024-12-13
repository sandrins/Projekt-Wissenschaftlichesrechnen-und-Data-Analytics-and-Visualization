import streamlit as st
import copy

st.title("Geschwindigkeitsvergleich")

'''
Auf dieser Seite kann die Geschwindigkeit auf der schnellsten Q3 Runde zwischen den Fahrern verglichen werden.
'''

drivers1 = ["Max", "Lewis"]
drivers2 = ["Lewis", "Max"]

cols = st.columns(2)
with st.container():
    with cols[0]:
        driver1 = st.selectbox("Wähle einen Fahrer", drivers1)
    with cols[1]:
        driver2 = st.selectbox("Wähle einen Fahrer", drivers2)