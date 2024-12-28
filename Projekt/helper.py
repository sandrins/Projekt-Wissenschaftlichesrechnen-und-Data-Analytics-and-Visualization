import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
from scipy import interpolate
from scipy.interpolate import splrep, splev, spalde, UnivariateSpline

# Masse des Formel-1-Fahrzeugs mit Fahrer
m_fahrzeug = 798 #kg

def getDriver(driver_name):
    for driver in drivers:
        if driver.fullname == driver_name:
            return driver
    return None

def calcTrackLength(self):
        s = np.sqrt(np.diff(self.x)**2 + np.diff(self.y)**2)
        strecke = np.sum(s)
        strecke_cumsum = np.cumsum(s)
        # Bestimmen der Kilometeridizes
        km_points = np.arange(1, int(strecke_cumsum[-1] // 1000) + 1) * 1000
        km_indizes = [np.argmax(strecke_cumsum >= km) for km in km_points]

        return strecke, strecke_cumsum, km_indizes

def plotTrack2D(driver, include_km_markers=True):
    # Beispiel-Daten (ersetze dies durch deine echten Daten)
    data = {
        "X": driver.x,
        "Y": driver.y
    }
    df1 = pd.DataFrame(data)

    # Streckenbeschriftungen (als Text)
    labels = [
        (50, 500, '1'),
        (290, 400, '2'),
        (480, 650, '3'), 
        (550, 430, '4'),
        (650, 700, '5'),
        (100, 800, 'Wellington Straight'),
        (100, 1150, '6'), 
        (-50, 900, '7'),
        (0, 1250, '8'),
        (650, 1320, '9'), 
        (640, 870, '10'), 
        (820, 700, '11'),
        (800, 555, '12'), 
        (840, 410, '13'), 
        (700, 260, '14'),
        (780, -50, 'Hangar Straight'), 
        (220, -350, '15'), 
        (-80, -50, '16'), 
        (-160, -160, '17'), 
        (-280, 60, '18')
    ]

    # Plotly-Plot erstellen
    fig = px.line(df1, x="X", y="Y")

    # Streckenbeschriftungen als Annotationen hinzufügen
    for x, y, label in labels:
        fig.add_annotation(
            x=x, y=y, 
            text=label, 
            showarrow=False, 
            font=dict(size=20, color='green'),
        )
    
    # Start/Ziel-Punkt hinzufügen
    fig.add_scatter(x=[driver.x[0]], y=[driver.y[0]], 
                    mode='markers', 
                    marker=dict(size=10, color='purple'),
                    name='Start/Ziel',)
    
    if include_km_markers:
        colors = ['yellow', 'pink', 'brown', 'cyan', 'orange']
        # Kilometer-Marker hinzufügen
        for i, ind in enumerate(driver.ind):
            fig.add_scatter(
                x=[driver.x[ind]], y=[driver.y[ind]],  
                mode='markers',
                marker=dict(size=10, color=colors[i]),
                name=f'{i+1} km',
                showlegend=True
            )

    # Layout-Anpassungen
    fig.update_layout(
        xaxis=dict(showgrid=True, title=""),
        yaxis=dict(showgrid=True, title="", scaleanchor="x"),
        showlegend=True,
        width=600,
        height=600,
        title=f'Streckenlayout Silverstone 2024',
        title_font=dict(size=20),
        template='plotly_dark'
    )

    # Den Plot in Streamlit anzeigen
    st.plotly_chart(fig)

def calcSpeed(self):
        spline = splrep(self.t[:-1], self.strecke_cumsum, k=3, s=3200)
        # Ableitung der Geschwindigkeit und berechnung an den Stützstellen
        ds1 = splev(self.t, spline, der=1)

        return ds1

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

def calcCentripetalAcceleration(v, r):
    # Zentripetalbeschleunigung berechnen
    a_z = (v**2) / r
    # Rückgabe
    return a_z

def calcCentripetalForce(a_z):
    # Gewicht initialisieren
    m = m_fahrzeug #kg
    # Zentripetalkraft berechnen
    f_z = a_z * m
    # Rückgabe
    return f_z

def calcAerodynamicForce(f_z):
    # Gewicht initialisieren
    m = 798 #kg
    # Reibungskoeffizient initialisieren
    mu= 1.258
    # Aerodinamische Kraft berechnen
    f_aero = f_z/mu - (m * 9.81)
    # Rückgabe
    return f_aero

def calcAerodynamicForceSpez(a_z, m, mu):
    # Zentripealkraft berechnen
    f_z = a_z * m
    # Aerodinamische Kraft berechnen
    f_aero = f_z/mu - (m * 9.81)
    # Rückgabe
    return f_aero

class Driver:
    def __init__(self, name, fullname):
        self.name = name
        self.fullname = fullname
        path = f"Projekt\P_data\{name}_data.csv"
        df = pd.read_csv(path, sep=";")
        self.x = df["X [m]"].values
        self.y = df["Y [m]"].values
        self.z = df["Z [m]"].values
        self.t = df["Time [s]"].values
        self.speed_kmh = df["Speed [km/h]"].values

        self.strecke, self.strecke_cumsum, self.ind = calcTrackLength(self)
        self.ds1 = calcSpeed(self)
        self.r, self.r_mx, self.r_my = calcRadiusOfCurvature(self.x, self.y, self.t)
        self.a_z = calcCentripetalAcceleration(self.ds1, self.r)
        self.f_z = calcCentripetalForce(self.a_z)
        self.f_aero = calcAerodynamicForce(self.f_z)
    
    
def initDriver():
    drivers = []
    ver = Driver('VER','Max Verstappen') #Max Verstappen
    drivers.append(ver)
    rus = Driver('RUS','George Russell') #George Russell
    drivers.append(rus)
    ham = Driver('HAM','Lewis Hamilton') #Lewis Hamilton
    drivers.append(ham)
    nor = Driver('NOR','Lando Norris') #Lando Norris
    drivers.append(nor)
    pia = Driver('PIA','Oscar Piastri') #Oscar Piastri
    drivers.append(pia)
    hul = Driver('HUL','Nico Hülkenberg') #Nico Hülkenberg
    drivers.append(hul)
    sai = Driver('SAI','Carlos Sainz') #Carlos Sainz
    drivers.append(sai)
    stro = Driver('STR','Lance Stroll') #Lance Stroll
    drivers.append(stro)
    alb = Driver('ALB','Alexander Albon') #Alexander Albon
    drivers.append(alb)
    alo = Driver('ALO','Fernando Alonso') #Fernando Alonso
    drivers.append(alo)
    
    return drivers

drivers = initDriver()