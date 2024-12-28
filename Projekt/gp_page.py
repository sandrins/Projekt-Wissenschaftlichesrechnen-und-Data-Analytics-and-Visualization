import streamlit as st
import pandas as pd
import helper

st.title("Übersicht")

'''
Auf dieser Seite gibt es einige Informationen zum Grossen Preis von Grossbritannien 2024 
der in Silverstone ausgetragen wurde.
'''

st.subheader("Die Strecke")

'''
Im folgenden Bild ist das Streckenlayout des GP von Grossbritannien in Silverstone dargestellt. Die Kurven sind mit grünen Nummern
versehen, um die Strecke besser zu verstehen und die beiden DRS-Geraden wurden mit ihren Namen
beschriftet. Start/Ziel ist mit einem lila Punkt markiert.
'''

helper.plotTrack2D(helper.drivers[0], False)

st.subheader("Resultat Q3")

'''
George Russell hat im Q3 die schnellste Runde gefahren und sich somit die Pole gesichert für das Rennen am Sonntag.
'''

times = []

for i in helper.drivers:
    t_max = max(i.t)
    minuten = int(t_max // 60)
    sekunden = int(t_max % 60)
    millisekunden = int(round((t_max % 1) * 1000))
    times.append(f'{minuten}:{sekunden:02d}:{millisekunden:03d}')

paare = list(sorted(zip([d.name for d in helper.drivers], [d.fullname for d in helper.drivers], times), key=lambda pair: pair[2]))

data = {
    "Rang": [1,2,3,4,5,6,7,8,9,10],
    "Fahrer": [pair[1] for pair in paare],
    "Rundenzeiten": [pair[2] for pair in paare]
}
df = pd.DataFrame(data)
df = df.set_index("Rang")

cols = st.columns(2)
with st.container():
    with cols[0]:        
        st.dataframe(df)
    with cols[1]:
        st.image("Projekt\P_data\Driver_Photos\georus01.png", width=400)
        st.caption("George Russell")