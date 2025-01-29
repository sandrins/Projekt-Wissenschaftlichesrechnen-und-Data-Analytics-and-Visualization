import streamlit as st
import pandas as pd
import os

#st.set_page_config(layout="wide")

st.title("Fahrer und Teams")

'''
Auf dieser Seite finden Sie eine Übersicht der Fahrer und Teams der Formel 1-Saison 2024. Neben Namen der Teams und Fahrer,
werden auch Informationen wie Alter, Startnummer und Anzahl der Siege angezeigt. Klicken Sie auf die Dropdown-Menüs, um 
mehr über die Fahrer zu erfahren.

Die Pokale und die Medaillen neben den Teamnamen, zeigen die Platzierung in der Team-Weltmeisterschaft 2024 an. Die Pokale und 
Medaillen neben den Fahrernamen, zeigen die Platzierung in der Fahrer-Weltmeisterschaft 2024 an. Der Pokal (🏆) steht für den ersten Platz, 
die Medaillen (🥈🥉) für den zweiten und dritten Platz in der jeweiligen Wertung.
'''
file_path = os.path.join(os.getcwd(), "Projekt/P_data", "Driver_Data.csv")
df = pd.read_csv(file_path, sep=",") #"Data/Driver_Data.csv"

def dropDown(n):
    driver_data = df[n]
    txt = st.write(f'''
            Age: {driver_data[0]}\n
            Number: {driver_data[1]}\n
            Wins: {driver_data[2]}
        ''')


cols = st.columns(2)
with st.container():
    with cols[0]:
        # McLaren
        st.header("McLaren 🏆")
        colsR = st.columns(2)
        with st.container():
            with colsR[0]:
                st.image("Projekt/P_data/Driver_Photos/lannor01.png", width=200)
                with st.expander("Lando Norris 🥈"):
                    dropDown("Lando Norris")
            with colsR[1]:
                st.image("Projekt/P_data/Driver_Photos/oscpia01.png", width=200)
                with st.expander("Oscar Piastri"):
                    dropDown("Oscar Piastri")
        
        # Red Bull
        st.header("Red Bull 🥉")
        colsR = st.columns(2)
        with st.container():
            with colsR[0]:
                st.image("Projekt/P_data/Driver_Photos/maxver01.png", width=200)
                with st.expander("Max Verstappen 🏆"):
                    dropDown("Max Verstappen")
            with colsR[1]:
                st.image("Projekt/P_data/Driver_Photos/serper01.png", width=200)
                with st.expander("Sergio Pérez"):
                    dropDown("Sergio Perez")
        
        # Aston Martin
        st.header("Aston Martin")
        colsR = st.columns(2)
        with st.container():
            with colsR[0]:
                st.image("Projekt/P_data/Driver_Photos/feralo01.png", width=200)
                with st.expander("Fernando Alonso"):
                    dropDown("Fernando Alonso")
            with colsR[1]:
                st.image("Projekt/P_data/Driver_Photos/lanstr01.png", width=200)
                with st.expander("Lance Stroll"):
                    dropDown("Lance Stroll")

        # Haas
        st.header("Haas")
        colsR = st.columns(2)
        with st.container():
            with colsR[0]:
                st.image("Projekt/P_data/Driver_Photos/kevmag01.png", width=200)
                with st.expander("Kevin Magnussen"):
                    dropDown("Kevin Magnussen")
            with colsR[1]:
                st.image("Projekt/P_data/Driver_Photos/nichul01.png", width=200)
                with st.expander("Nico Hülkenberg"):
                    dropDown("Nico Hülkenberg")
        
        # Williams
        st.header("Williams")
        colsR = st.columns(2)
        with st.container():
            with colsR[0]:
                st.image("Projekt/P_data/Driver_Photos/alealb01.png", width=200)
                with st.expander("Alexander Albon"):
                    dropDown("Alexander Albon")
            with colsR[1]:
                st.image("Projekt/P_data/Driver_Photos/logsar01.png", width=200)
                with st.expander("Logan Sargeant"):
                    dropDown("Logan Sargeant")
        
    with cols[1]:
        # Ferrari
        st.header("Ferrari 🥈")
        colsR = st.columns(2)
        with st.container():
            with colsR[0]:
                st.image("Projekt/P_data/Driver_Photos/chalec01.png", width=200)
                with st.expander("Charles Leclerc 🥉"):
                    dropDown("Charles Leclerc")
            with colsR[1]:
                st.image("Projekt/P_data/Driver_Photos/carsai01.png", width=200)
                with st.expander("Carlos Sainz"):
                    dropDown("Carlos Sainz")
        
        # Mercedes
        st.header("Mercedes")
        colsR = st.columns(2)
        with st.container():
            with colsR[0]:
                st.image("Projekt/P_data/Driver_Photos/lewham01.png", width=200)
                with st.expander("Lewis Hamilton"):
                    dropDown("Lewis Hamilton")
            with colsR[1]:
                st.image("Projekt/P_data/Driver_Photos/georus01.png", width=200)
                with st.expander("George Russell"):
                    dropDown("George Russell")
        
        # Alpine
        st.header("Alpine")
        colsR = st.columns(2)
        with st.container():
            with colsR[0]:
                st.image("Projekt/P_data/Driver_Photos/estoco01.png", width=200)
                with st.expander("Esteban Ocon"):
                    dropDown("Esteban Ocon")
            with colsR[1]:
                st.image("Projekt/P_data/Driver_Photos/piegas01.png", width=200)
                with st.expander("Pierre Gasly"):
                    dropDown("Pierre Gasly")
        
        # VCARB
        st.header("VCARB")
        colsR = st.columns(2)
        with st.container():
            with colsR[0]:
                st.image("Projekt/P_data/Driver_Photos/danric01.png", width=200)
                with st.expander("Daniel Ricciardo"):
                    dropDown("Daniel Ricciardo")
            with colsR[1]:
                st.image("Projekt/P_data/Driver_Photos/yuktsu01.png", width=200)
                with st.expander("Yuki Tsunoda"):
                    dropDown("Yuki Tsunoda")

        # Kick Sauber
        st.header("Kick Sauber")
        colsR = st.columns(2)
        with st.container():
            with colsR[0]:
                st.image("Projekt/P_data/Driver_Photos/valbot01.png", width=200)
                with st.expander("Valtteri Bottas"):
                    dropDown("Valtteri Bottas")
            with colsR[1]:
                st.image("Projekt/P_data/Driver_Photos/guazho01.png", width=200)
                with st.expander("Zhou Guanyu"):
                    dropDown("Zhou Guanyu")