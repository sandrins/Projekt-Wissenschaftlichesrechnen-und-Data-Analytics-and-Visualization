import streamlit as st
import helper
import pandas as pd
import plotly.express as px

st.title("Zentripetalbeschleunigung und -kraft")

st.subheader("Zentripetalbeschleunigung")

'''
Die Zentripetalbeschleunigung $a_z$ ist die Beschleunigung, die ein Körper auf einer Kreisbahn hält.
Die Zentripetalbeschleunigung $a_z$ wird wie folgt berechnet:
'''
# Formel Zentripetalbeschleunigung
st.latex(r"a_z = \frac{v^2}{r}")
st.caption("Formel für die Zentripetalbeschleunigung $a_z$")

'''
Mit der folgenden Funktion kann die Zentripetalbeschleunigung $a_z$ berechnet werden.
'''

code = (
    """
    def calcCentripetalAcceleration(v, r):
    # Zentripetalbeschleunigung berechnen
    a_z = (v**2) / r
    # Rückgabe
    return a_z
    """
)
st.code(code, language='python')
st.caption('Code zur Berechnung der Zentripetalbeschleunigung $a_z$')

# Plot Zentripetalbschleunigung

drivers = ['Max Verstappen', 'George Russell','Lewis Hamilton','Lando Norris','Oscar Piastri','Nico Hülkenberg','Carlos Sainz','Lance Stroll','Alexander Albon','Fernando Alonso']
driver = st.selectbox("Wähle einen Fahrer", drivers)

data = {
    'Zentripetalbeschleunigung [m/s^2]': helper.getDriver(driver).a_z[:-1],
    'Strecke [m]': helper.getDriver(driver).strecke_cumsum
}
df = pd.DataFrame(data)
fig = px.line(df, 
              x='Strecke [m]', 
              y=['Zentripetalbeschleunigung [m/s^2]'],
              title=f'{helper.getDriver(driver).fullname} Zentripetalbeschleunigungverlauf')
fig.update_layout(
    xaxis=dict(showgrid=True, title="Strecke [m]"),
    yaxis=dict(showgrid=True, title="Zentripetalbeschleunigung [m/s^2]"),
    showlegend = False,
)
st.plotly_chart(fig, theme="streamlit")


st.subheader("Zentripetalkraft")

'''
Die Zentripetalkraft $F_z$ ist die Kraft, die benötigt wird, um einen Körper auf einer Kreisbahn zu halten.
Die Zentripetalkraft $F_z$ wird wie folgt berechnet:
'''
# Formel Zentripetalkraft
st.latex(r"F_z = m \cdot a_z")
st.caption("Formel für die Zentripetalkraft $F_z$")

'''
Mit der folgenden Funktion kann die Zentripetalkraft $F_z$ berechnet werden.
'''
code = (
    """
    def calcCentripetalForce(a_z, m):
        # Zentripetalkraft berechnen
        f_z = a_z * m
        # Rückgabe
        return f_z
    """)

st.code(code, language='python')
st.caption('Code zur Berechnung der Zentripetalkraft')

# Plot Zentripetalkraft
'''
Die Formel-1-Fahrzeuge hatten in der Saison 2024 ein Mindestgewicht von 798 kg. Das war das höchste Mindestgewicht in der Geschichte der Formel 1.

Mit dem folgenden Textfeld kann die Masse des Fahrzeugs beliebig angepasst werden. Mit einem Klick auf den Button "Zentripetalkraft $F_z$ berechnen" 
wird die Zentripetalkraft $F_z$ berechnet, welche benötigt wird um ein Fahrzeug auf der Strecke zuhalten. In der Grafik wird die Zentripetalkraft $F_z$ 
entlang der Strecke dargestellt.
'''
def plotZentripetalkraft(driver, m=798):
    data = {
        'Zentripetalkraft [N]': helper.getDriver(driver).a_z[:-1] * m,
        'Strecke [m]': helper.getDriver(driver).strecke_cumsum
    }
    df = pd.DataFrame(data)
    fig = px.line(df, 
                x='Strecke [m]', 
                y=['Zentripetalkraft [N]'],
                title=f'{helper.getDriver(driver).fullname} Zentripetalkraftverlauf')
    fig.update_layout(
        xaxis=dict(showgrid=True, title="Strecke [m]"),
        yaxis=dict(showgrid=True, title="Zentripetalkraft [N]"),
        showlegend = False,
    )
    
    st.plotly_chart(fig, theme="streamlit")

# Masse des Fahrzeugs anpassen
m = st.number_input("Masse des Fahrzeugs [kg]", value=798)
if st.button("Zentripetalkraft $F_z$ berechnen"):
    plotZentripetalkraft(driver, m)