import numpy as np
import pandas as pd
from scipy import interpolate
from scipy.interpolate import splrep, splev, spalde, UnivariateSpline

class Driver:
    def __init__(self, name):
        self.name = name
        path = f"Projekt\P_data\{name}_data.csv"
        df = pd.read_csv(path, sep=";")
        self.x = df["X [m]"].values
        self.y = df["Y [m]"].values
        self.z = df["Z [m]"].values
        self.t = df["Time [s]"].values
        self.speed_kmh = df["Speed [km/h]"].values

    def calcTrackLength(self):
        s = np.sqrt(np.diff(self.x)**2 + np.diff(self.y)**2)
        strecke = np.sum(s)
        strecke_cumsum = np.cumsum(s)

        return strecke, strecke_cumsum