import streamlit as st
import helper
import pandas as pd
import plotly.express as px

st.title("Geschwindigkeitsvergleich")

'''
Auf dieser Seite kann die Geschwindigkeit auf der schnellsten Q3 Runde zwischen den Fahrern verglichen werden.
Die Geschwindigkeit ist die Ableitung der Strecke nach der Zeit.
'''
# Formel Geschwindigkeit
st.latex(r"v = \frac{ds}{dt}")
st.caption("Formel für die Geschwindigkeit $v$")
'''

Mit der folgenden Funktion wird der Geschwindigkeitsverlauf berechnet.
'''

code = (
    """
    def calcSpeed(t, x, y):
        # Strecke berechnen
        s = np.sqrt(np.diff(x)**2 + np.diff(y)**2)
        strecke_cumsum = np.cumsum(s)
        spline = splrep(t[:-1], strecke_cumsum, k=3, s=3200)
        # Ableitung der Geschwindigkeit und berechnung an den Stützstellen
        ds1 = splev(t, spline, der=1)

        return ds1 
    """)

st.code(code, language='python')
st.caption('Code zur Berechnung der Geschwindigkeit')

'''
Der Geschwindigkeitsverlauf kann nur von unterschiedlichen Fahrern miteinander vergliechen werden.

Im Plot wird die Geschwindigkeits entlang der Strecke dargestellt.
'''

# Auswahl links
drivers1 = ['Max Verstappen', 'George Russell','Lewis Hamilton','Lando Norris','Oscar Piastri','Nico Hülkenberg','Carlos Sainz','Lance Stroll','Alexander Albon','Fernando Alonso']
# Auswahl rechts
drivers2 = ['George Russell', 'Max Verstappen','Lewis Hamilton','Lando Norris','Oscar Piastri','Nico Hülkenberg','Carlos Sainz','Lance Stroll','Alexander Albon','Fernando Alonso']

def plotSpeed(driver):
    data = {
        'Strecke [m]': driver.strecke_cumsum,
        'Geschwindigkeit berechnet [km/h]': driver.ds1[:-1]*3.6,
        'Geschwindigkeit gemessen [km/h]': driver.speed_kmh[:-1]
    }
    df = pd.DataFrame(data)
    fig = px.line(df, 
                  x='Strecke [m]', 
                  y=['Geschwindigkeit berechnet [km/h]','Geschwindigkeit gemessen [km/h]'],
                  title=f'{driver.fullname} Geschwindigkeitsverlauf')
    fig.update_layout(
        xaxis=dict(showgrid=True, title="Strecke [m]"),
        yaxis=dict(showgrid=True, title="Geschwindigkeit [km/h]"),
        legend_title = 'Legende',
        legend = dict(x=0.4, y=0)
    )
    st.plotly_chart(fig, theme="streamlit")

def plotSpeedOnTrack(driver):
    data = {
        'X [m]': driver.x,
        'Y [m]': driver.y,
        'Geschwindigkeit berechnet [km/h]': driver.ds1*3.6
    }
    df = pd.DataFrame(data)
    fig = px.scatter(df,
                  x='X [m]',
                  y='Y [m]',
                  color='Geschwindigkeit berechnet [km/h]',
                  color_continuous_scale='Jet',
                  title=f'{driver.fullname} Geschwindigkeit auf der Strecke')

    fig.update_layout(
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True, scaleanchor="x"),
        coloraxis_colorbar=dict(title='Geschwindigkeit [km/h]'),
        height=600
    )
    st.plotly_chart(fig, theme='streamlit')


cols = st.columns(2)
with st.container():
    with cols[0]:
        driver1 = st.selectbox("Wähle einen Fahrer", drivers1)
        driver_ = helper.getDriver(driver1)
        plotSpeed(driver_)
        plotSpeedOnTrack(driver_)
    with cols[1]:
        driver2 = st.selectbox("Wähle einen Fahrer", drivers2)
        if driver2 != driver1:
            driver_ = helper.getDriver(driver2)
            plotSpeed(driver_)
            plotSpeedOnTrack(driver_)
        else:
            st.error('Wähle einen anderen Fahrer')