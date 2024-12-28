import streamlit as st
import pandas as pd
import plotly.express as px
import helper

st.title("Aerodynamische Kraft")

# Erforderliche aerodynamische Kraft berechnen
st.subheader("Formel zur Berechnung der erforderliche aerodynamische Kraft")

'''
Ein Formel 1 Auto kann sicht nicht ausschliesslich nur über die eigenen Gewichtskraft auf der Strecke halten. Es braucht zusätzlich auch noch eine aerodynamische Kraft
$F_{aero}$, die das Fahrzeug nach untendrückt.

Die aerodynamische Kraft entsteht, wenn Luft auf ein sich bewegendes Fahrzeug einwirkt und dabei die Bewegung beeinflusst. Sie hängt von der Fahrzeuggeschwindigkeit, 
der Luftdichte, der Form und der Querschnittsfläche ab. Formel-1-Autos sind so gestaltet, dass sie gezielt Kräfte erzeugen, die das Fahrzeug auf die Strecke drücken 
und die Haftung in Kurven verbessern. Gleichzeitig wird der Luftwiderstand optimiert, um auf Geraden maximale Geschwindigkeiten zu erreichen.
'''

# Haftreibung muss grösser sein als die Zentripetalkraft
st.latex(r"F_{\text{Haft}} \geq F_z")
st.latex(r"\mu \cdot F_N \geq F_z")
st.latex(r"\mu \cdot (m \cdot g + F_{aero}) \geq F_z")
st.caption("Formeln zur Herleitung der aerodynamischen Kraft $F_{aero}$")

# Umstellen nach der aerodynamischen Kraft
st.latex(r"F_{aero} \geq \frac{F_z}{\mu} - m \cdot g")
st.caption("Formel für die aerodynamische Kraft $F_{aero}$")

# code zur Berechnung der aerodynamischen Kraft
st.subheader("Code zur Berechnung der aerodynamischen Kraft")
'''
Mit der Funktion `calcAerodynamicForce(f_z)` kann die aerodynamische Kraft berechnet werden, welche benötigt wird, um ein Fahrzeug auf der Strecke zuhalten.
Für die Masse wird das minimale Fahrzeuggewicht von 798 kg angenommen. Der Reibungskoeffizient beträgt 1.258 und wurde auf der Seite "Reibungskoeffizient berechnet.
'''
code = (
    """
    def calcAerodynamicForce(f_z):
        # Gewicht initialisieren
        m = 798 #kg
        # Reibungskoeffizient initialisieren
        mu= 1.258
        # Aerodinamische Kraft berechnen
        f_aero = f_z/mu - (m * 9.81)
        # Rückgabe
        return f_aero
    """)
st.code(code, language='python')
st.caption('Code zur Berechnung der aerodynamischen Kraft')

cols = st.columns(2)
with cols[0]:
    # Plot aerodynamische Kraft
    st.subheader("Grafik aerodynamische Kraft")
    '''
    Im folgenden Plot wird der Verlauf der minimal notwendigen aerodynamischen Kraft entlang der Strecke dargestellt. Zu beachten ist, dass die aerodynamische Kraft
    an gewissen Stellen negativ sein kann. Dies bedeutet, dass die aerodynamische Kraft nicht benötigt wurde, um das Fahrzeug auf der Strecke zuhalten.

    Auf der rechten Seite wurde das Streckenlayout von Silverstone dargestellt, dadurch ist der Verlauf der aerodynamischen Kraft besser nachvollziehbar.
    '''

    drivers = ['Max Verstappen', 'George Russell','Lewis Hamilton','Lando Norris','Oscar Piastri','Nico Hülkenberg','Carlos Sainz','Lance Stroll','Alexander Albon','Fernando Alonso']
    driver = st.selectbox("Wähle einen Fahrer", drivers)
with cols[1]:
    helper.plotTrack2D(helper.getDriver(driver), True)

data = {
    'Aerodynamische Kraft [N]': helper.getDriver(driver).f_aero[:-1],
    'Strecke [m]': helper.getDriver(driver).strecke_cumsum
}
df = pd.DataFrame(data)
fig = px.line(df, 
              x='Strecke [m]', 
              y=['Aerodynamische Kraft [N]'],
              title=f'{helper.getDriver(driver).fullname} Verlauf der minimal notwenigen aerodynamischen Kraft')
fig.update_layout(
    xaxis=dict(showgrid=True, title="Strecke [m]"),
    yaxis=dict(showgrid=True, title="Aerodynamische Kraft [N]"),
    showlegend = False,
)
st.plotly_chart(fig, theme="streamlit")

st.caption("Verlauf der minimal notwenigen aerodynamischen Kraft")

st.subheader("Aerodynamische Kraft im Vergleichen")
'''
Um besser zu veranschaulichen, was für auswikung ein grösserer oder kleinerer Haftreibungskoeffizient oder Gewicht haben, kannst in den folgenden beiden
Konfiguratoren selbst Gewichte und Haftreibungskoeffizienten eingeben. Über die jeweiligen Knöpfe können die Plots der erforderlichen aerodynamischen Kraft $F_{aero}$
erstellt werden.

Viel spass beim Ausprobieren!
'''

# Initialisieren von session_state
if "f_aero1" not in st.session_state:
    st.session_state.f_aero1 = []
if "f_aero2" not in st.session_state:
    st.session_state.f_aero2 = []

# Konfigurator 1
cols = st.columns(2)
with cols[0]:
    st.subheader('Konfigurator 1')

    cols1 = st.columns(2)
    with cols1[0]:
        m1 = st.number_input("Masse des Fahrzeugs [kg]", value=798, key=1)
    with cols1[1]:
        mu1 = st.number_input("Reibungskoeffizient", value=1.258, key=2)
    
    if st.button("Aerodynamische Kraft berechnen", key=10):
        st.session_state.f_aero1 = helper.calcAerodynamicForceSpez(helper.drivers[0].a_z, m1, mu1)

# Konfigurator 2
with cols[1]:
    st.subheader('Konfigurator 2')

    cols1 = st.columns(2)
    with cols1[0]:
        m2 = st.number_input("Masse des Fahrzeugs [kg]", value=798, key=3)
    with cols1[1]:
        mu2 = st.number_input("Reibungskoeffizient", value=1.258, key=4)
    
    if st.button("Aerodynamische Kraft berechnen", key=11):
        st.session_state.f_aero2 = helper.calcAerodynamicForceSpez(helper.drivers[0].a_z, m2, mu2)

# Funktion zur Erstellung des Plots
def plotAerodynamicForce(f_aero):
    data = {
        'Aerodynamische Kraft [N]': f_aero[:-1],
        'Strecke [m]': helper.drivers[0].strecke_cumsum
    }
    df = pd.DataFrame(data)
    fig = px.line(df, 
                  x='Strecke [m]', 
                  y=['Aerodynamische Kraft [N]'],
                  title=f'Verlauf der minimal notwenigen aerodynamischen Kraft')
    fig.update_layout(
        xaxis=dict(showgrid=True, title="Strecke [m]"),
        yaxis=dict(showgrid=True, title="Aerodynamische Kraft [N]"),
        showlegend = False,
    )
    return fig

# Plot für Konfiguration 1
st.subheader('Plot der Konfiguration 1')
if len(st.session_state.f_aero1) > 0:
    st.plotly_chart(plotAerodynamicForce(st.session_state.f_aero1), theme="streamlit",key=20)

# Plot für Konfiguration 2
st.subheader('Plot der Konfiguration 2')
if len(st.session_state.f_aero2) > 0:
    st.plotly_chart(plotAerodynamicForce(st.session_state.f_aero2), theme="streamlit", key=21)