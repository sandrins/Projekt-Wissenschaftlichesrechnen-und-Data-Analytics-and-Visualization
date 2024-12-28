import streamlit as st
import pandas as pd

st.title("Die Formel 1 - Die Königsklasse des Motorsports")

'''
Die Formel 1 ist  eine der prestigeträchtigsten Rennserien der Welt. 
Jedes Jahr treten die besten Fahrer und Teams in einer Weltmeisterschaft 
gegeneinander an, um den Titel des Fahrers- und Konstrukteursweltmeisters 
zu erringen. Mit High-Tech-Fahrzeugen, die Geschwindigkeiten von über 
350 km/h erreichen, stellt die Formel 1 eine Kombination aus 
Ingenieurskunst, Strategie und fahrerischem Können dar.
'''

st.subheader("Die Geschichte")
'''
Die Formel 1 wurde 1950 ins Leben gerufen und hat sich seitdem zu 
einer der aufregendsten und technologisch fortschrittlichsten 
Rennserien der Welt entwickelt. Das erste Rennen fand in Silverstone, 
Großbritannien, statt. Seitdem hat sich die Formel 1 kontinuierlich 
weiterentwickelt, wobei sowohl die Fahrzeuge als auch die Regeln immer 
wieder angepasst wurden, um die Sicherheit zu erhöhen und die 
Wettbewerbsfähigkeit zu gewährleisten. Berühmte Fahrer wie 
Ayrton Senna, Michael Schumacher und Lewis Hamilton prägten die 
Geschichte der Serie und trugen zur weltweiten Popularität bei.
'''

st.subheader("Das Rennwochenende")
'''
Ein Rennwochenende in der Formel 1 besteht aus drei Hauptabschnitten:

**1. Freie Trainings (Freitag und Samstag):**
Fahrer und Teams nutzen mehrere Trainingssessions, um das Fahrzeug-Setup zu optimieren, die Strecke zu
analysieren und Strategien zu entwickeln. Dabei werden auch Daten über Reifenverschleiß und Treibstoffverbrauch
gesammelt.

**2. Qualifikation (Samstag):**
Die Qualifikation entscheidet über die Startpositionen für das Rennen. Sie besteht aus drei Abschnitten
(Q1, Q2 und Q3), in denen die Fahrer versuchen, die schnellste Runde zu fahren. Nur die schnellsten zehn
Fahrer schaffen es in die letzte Runde (Q3), die die vorderen Startplätze festlegt.

**3. Rennen (Sonntag):**
Der Höhepunkt des Wochenendes ist das Rennen. Die Fahrer starten entsprechend ihrer Qualifikationsplatzierung
und versuchen, als Erster die Ziellinie zu überqueren. Neben Geschwindigkeit spielen Boxenstopps, Reifenstrategie
und das Wetter eine entscheidende Rolle.

Jedes Rennen bietet die Gelegenheit, Punkte zu sammeln, die am Ende der Saison über die Weltmeisterschaft entscheiden.
Ein Formel-1-Wochenende ist daher nicht nur ein Spektakel für Fans, sondern auch eine technologische und taktische
Herausforderung für die Teams.
'''

st.subheader("Das Punktesystem")
'''
Das Punktesystem der Formel 1 belohnt die ersten zehn Fahrer, die ein 
Rennen beenden. Der Sieger erhält 25 Punkte, der Zweitplatzierte 18 
Punkte und der Drittplatzierte 15 Punkte. Danach sinkt die Punktzahl 
schrittweise bis zum 10. Platz, der noch 1 Punkt erhält. Zusätzlich 
gibt es einen Punkt für die schnellste Rennrunde, sofern der Fahrer 
unter den Top 10 ins Ziel kommt. Diese Punkte tragen sowohl zur Fahrer- 
als auch zur Konstrukteurswertung bei, die am Ende der Saison über die 
Meisterschaft entscheiden.
'''

st.subheader("Der Rennkalender 2024")
'''
Die Formel-1-Saison 2024 umfasste 24 Rennen auf einigen der ikonischsten 
Rennstrecken der Welt sowie neuen aufregenden Austragungsorten. Der 
Saisonauftakt fand in Bahrain statt, und das Finale wurde in Abu Dhabi 
auf dem Yas Marina Circuit ausgetragen. Zu den Höhepunkten zählten das 
prestigeträchtige Rennen in Monaco, das Nachtrennen in Singapur und das 
Heimrennen vieler Teams in Silverstone. Den genauen Rennkalender 
finden Sie in der nachfolgenden Tabelle. 
'''

df = pd.read_csv("Projekt\P_data\Rennkalender_2024.csv", sep=",", index_col=0)
st.dataframe(df, width=800, height=878)
st.caption("Rennkalender 2024")

'''
Weitere Informationen zu den einzelnen Rennen und den Ergebnissen finden Sie auf der offiziellen [Formel-1-Website](https://www.formula1.com/).
'''

