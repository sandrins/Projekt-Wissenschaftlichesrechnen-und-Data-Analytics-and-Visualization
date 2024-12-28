import streamlit as st
import pandas as pd
import plotly.express as px
import helper

st.title("Krümmungsradius")

'''
Mit der folgenden Formel kann der Krümmungsradius einer Kurve berechnet werden.
'''
# Formel Krümmungsradius aus den x- und y-Koordinaten
st.latex(r"r = \left| \frac{\left( x'(t)^2 + y'(t)^2 \right) ^{\frac{3}{2}}}{x'(t) \cdot y''(t) - x''(t) \cdot y'(t)} \right|")
st.caption("Formel für den Krümmungsradius $r$")

'''
In diesem Fall wird der Krümmungsradius für jeden Punkt entlang der Strecke berechnet. 

Der Krümmungsradius wird mit der folgenden Funktion berechnet. Es wird aber nicht nur der Krümmungsradius berechnet, 
sondern auch der Radiusmittelpunkt.
'''
code = (
    """
    def calcRadiusOfCurvature(x, y, t):
        # Spline-Interpolation
        spline_x = splrep(t, x, k=3)
        spline_y = splrep(t, y, k=3)
        # Erste Ableitung
        dx1 = splev(t, spline_x, der=1)
        dy1 = splev(t, spline_y, der=1)
        # Zweite Ableitung
        dx2 = splev(t, spline_x, der=2)
        dy2 = splev(t, spline_y, der=2)
        # Krümmungsradius berechnen
        r = abs(((np.sqrt(dx1**2 + dy1**2))**3)/((dx1*dy2) - (dx2*dy1)))
        # Radiusmittelpunkt berechnen
        r_mx = x - ((dy1*(dx1**2 + dy1**2))/((dx1 * dy2) - (dx2 * dy1)))
        r_my = y + ((dx1*(dx1**2 + dy1**2))/((dx1 * dy2) - (dx2 * dy1)))
        #Rückgabe
        return r, r_mx, r_my 
    """)

st.code(code, language='python')
st.caption('Code zur Berechnung des Krümmungsradius')

'''
Mit der Dropdown-Liste kann der Fahrer ausgewählt werden, für den der Krümmungsradiusverlauf anzeigt werden soll.
Der sichtbare Bereich der y-Achse wurde begrenzt, um die Unterschiede besser sichtbar zu machen.
Interessant sind vor allem kleinen Krümmungsradien, da an diesen Stellen Kurven zu finden sind. 
Bei sehr grossen Krümmungsradien handelt es sich um Geraden.
'''

# Auswahl
drivers = ['Max Verstappen', 'George Russell','Lewis Hamilton','Lando Norris','Oscar Piastri','Nico Hülkenberg','Carlos Sainz','Lance Stroll','Alexander Albon','Fernando Alonso']
driver_selected = st.selectbox("Wähle einen Fahrer", drivers)

driver = helper.getDriver(driver_selected)

data = {
        'Strecke [m]': driver.strecke_cumsum,
        'Radius [m]': driver.r[:-1],
    }
df = pd.DataFrame(data)
fig = px.line(df, 
    x='Strecke [m]', 
    y=['Radius [m]'],
    title=f'{driver.fullname} Krümmungsradius')
fig.update_layout(
    xaxis=dict(showgrid=True, title="Strecke [m]"),
    yaxis=dict(showgrid=True, title="Krümmungsradius [m]", range=[0, 1000]),
    showlegend=False
    )
st.plotly_chart(fig, theme="streamlit")


