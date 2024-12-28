import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import helper

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
st.caption('Code zur Berechnung der Streckenlänge')

'''
In der folgenden Tabelle ist die jewilige Rundenlänge jedes Fahrers. Es ist zu sehen, 
dass jeder Fahrer eine unterschiedliche Distanz zurücklegte, um eine Runde zu fahren.
Dies ist ganz normal, da nicht jeder Fahrer genau die gleiche Linie fährt.

Als Vergleich die Rundenlängen von Wikipedia mit 5891 Meter und zusätzlich habe  ich selbst auf 
GoogleMaps die Ideallinie abgemessen und bin auf 5800 Meter gekommen.

Auf der rechten Seite ist das Streckenlayout des GP von Grossbritannien in Silverstone 
dargestellt und wurde aus den X- und Y-Koordinaten geplotet. Die Kurven sind mit Nummern
versehen, um die Strecke besser zu verstehen und die beiden DRS-Geraden wurden mit ihren Namen
beschriftet. Start/Ziel ist mit einem lila Punkt markiert.
'''


s = []
for i in helper.drivers:
    s.append(int(i.strecke))

paare = list(sorted(zip([d.name for d in helper.drivers], [d.fullname for d in helper.drivers], s), key=lambda pair: pair[2]))

data = {
    "Fahrer": [pair[1] for pair in paare],
    "Rundenlänge [m]": [pair[2] for pair in paare]
}

df = pd.DataFrame(data)
df = df.set_index("Fahrer")

driver = helper.drivers[3]

cols = st.columns(2)
with st.container():
    with cols[0]:
        st.subheader('Rundenlängen')
        st.subheader('')
        st.dataframe(df)

    with cols[1]:
        st.subheader('Silverstone 2024')
        helper.plotTrack2D(driver, True)
        st.caption("Streckenlayout Silverstone")