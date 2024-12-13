import streamlit as st
import pandas as pd
from helper import Driver

st.title("Übersicht")

'''
Auf dieser Seite gibt es einige Informationen zum Grossen Preis von Grossbritannien 2024 
der in Silverstone ausgetragen wurde.
'''

st.subheader("Resultat Q3")

'''
George Russell hat im Q3 die schnellste Runde gefahren und sich somit die Pole gesichert für das Rennen am Sonntag.
'''

ver = Driver('VER') #Max Verstappen
rus = Driver('RUS') #George Russell
ham = Driver('HAM') #Lewis Hamilton
nor = Driver('NOR') #Lando Norris
pia = Driver('PIA') #Oscar Piastri
hul = Driver('HUL') #Nico Hülkenberg
sai = Driver('SAI') #Carlos Sainz
stro = Driver('STR') #Lance Stroll
alb = Driver('ALB') #Alexander Albon
alo = Driver('ALO') #Fernando Alonso

drivers = [ver, rus, ham, nor, pia, hul, sai, stro, alb, alo]
drivers_fullname = ['Max Verstappen','George Russell','Lewis Hamilton','Lando Norris','Oscar Piastri',
                    'Nico Hülkenberg','Carlos Sainz','Lance Stroll','Alexander Albon','Fernando Alonso']
times = []

for i in drivers:
    t_max = max(i.t)
    minuten = int(t_max // 60)
    sekunden = int(t_max % 60)
    millisekunden = int(round((t_max % 1) * 1000))
    times.append(f'{minuten}:{sekunden:02d}:{millisekunden:03d}')

paare = list(sorted(zip(drivers, drivers_fullname, times), key=lambda pair: pair[2]))

data = {
    "Rang": [1,2,3,4,5,6,7,8,9,10],
    "Fahrer": [pair[1] for pair in paare],
    "Rundenzeiten": [pair[2] for pair in paare]
}

df = pd.DataFrame(data)
df = df.set_index("Rang")
st.dataframe(df)