import streamlit as st
import helper

st.title("Haftreibungskoeffizient")

'''
Um die erforderliche aerodynamische Kraft bestimmen, wird er Haftreibungskoeffizent zwischen Reifen und Asphalt benötigt.
Jedoch ist im Internet keine genaue Angabe zu finden von Pirelli oder den Formel-1-Teams.

Daher habe ich mich dazu entschieden, den Haftreibungskoeffizienten selbst zu berechnen.
Mit der folgenden Formel wird der Haftreibungskoeffizient $\mu$ zwischen den Reifen eines Formel-1-Fahrzeugs und dem Asphalt berechnet.
'''

st.latex(r"F_{\text{Haft}} = \mu \cdot F_N")
st.latex(r"m \cdot a_{max} = \mu \cdot m \cdot g")
st.caption("Formeln zur Herleitung des Haftreibungskoeffizienten $\mu$")

# Umstellen nach dem Haftreibungskoeffizienten
st.latex(r"\mu = \frac{a_z}{g}")
st.caption(" Formel für den Haftreibungskoeffizienten $\mu$")

'''
Es wird angenommen, dass ein Formel-1-Fahrzeug von 0 auf 200km/h in 4.5 Sekunden beschleunigt.
Dies ergibt eine maximale Beschleunigung von $a_{max}$ = 12.35 ${\\text{m}/\\text{s}}^2$.
Dei Erdbeschleunigung beträgt $g$ = 9.81 ${\\text{m}/\\text{s}}^2$.

Somit ergibt sich ein Haftreibungskoeffizient von: 1.258
'''


'''
Achtung: Der hier berechnete Haftreibungskoeffizient ist ein theoretischer Wert.
Für einen genaueren Wert müssen Tests auf einer Rennstrecke durchgeführt werden.
'''


