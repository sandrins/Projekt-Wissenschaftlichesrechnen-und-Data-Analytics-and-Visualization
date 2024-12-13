import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from helper import Driver

st.title("Rundenlänge")

'''
Aus den X- und Y-Koordinaten wurde die zurückgelegte Distanz der Q3-Runde für jeden Fahrer berechnet.
'''

code = (
    """
    def calcTrackLength(x,y):
        s = np.sqrt(np.diff(x)**2 + np.diff(y)**2)
        strecke = np.sum(s)

        return strecke 
    """)

st.code(code, language='python')


'''
In der folgenden Tabelle ist die jewilige Rundenlänge jedes Fahrers. Es ist zu sehen, 
dass jeder Fahrer eine unterschiedliche Distanz zurücklegte, um eine Runde zu fahren.
Dies ist ganz normal, da nicht jeder Fahrer genau die gleiche Linie fährt.

Als Vergleich die Rundenlängen von Wikipedia mit 5891 Meter und zusätzlich habe  ich selbst auf 
GoogleMaps die Ideallinie abgemessen und bin auf 5800 Meter gekommen.

Auf der rechten Seite ist das Streckenlayout des GP von Grossbritannien in Silverstone 
dargestellt und wurde aus den X- und Y-Koordinaten geplotet.
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
s = []
for i in drivers:
    strecke, strecke_cumsum = i.calcTrackLength()
    s.append(int(strecke))

paare = list(sorted(zip(drivers, drivers_fullname, s), key=lambda pair: pair[2]))

data = {
    "Fahrer": [pair[1] for pair in paare],
    "Rundenlänge [m]": [pair[2] for pair in paare]
}

df = pd.DataFrame(data)
df = df.set_index("Fahrer")

data = {
    "X": nor.x,
    "Y": nor.y
}
df1 = pd.DataFrame(data)

fig = px.line(df1, x="X", y="Y")
fig.update_layout(
    xaxis=dict(showgrid=True, title=""),
    yaxis=dict(showgrid=True, title="", scaleanchor="x"),
    showlegend=False,
    width = 600,
    height = 600,
    title=''
    #title_font=dict(size=28)
)

cols = st.columns(2)
with st.container():
    with cols[0]:
        st.subheader('**Rundenlängen**')
        st.subheader('')
        st.dataframe(df)

    with cols[1]:
        st.subheader('**Silberstone 2024**')
        fig.update_traces(line_color='orange')
        st.plotly_chart(fig, theme="streamlit")

        st.caption("Streckenlayout Silverstone")