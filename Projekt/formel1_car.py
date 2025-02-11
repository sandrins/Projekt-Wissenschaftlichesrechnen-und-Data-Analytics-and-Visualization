import streamlit as st
import pandas as pd

st.title("Formel 1 Auto")

'''
Ein Formel-1-Fahrzeug der Saison 2024 repräsentiert den Höhepunkt 
moderner Motorsporttechnologie und Aerodynamik. Hier sind einige 
der wichtigsten Technologien und Merkmale, die ein solches Fahrzeug 
auszeichnen:
'''

st.subheader("Aerodynamik")
'''
Die Aerodynamik eines Formel-1-Autos der Saison 2024 ist entscheidend 
für die Leistung. 

Der Bodeneffekt (Ground Effect) spielt eine zentrale Rolle. Durch 
präzise gestaltete Venturitunnel am Unterboden wird die Luft unter 
dem Fahrzeug beschleunigt, was den Luftdruck verringert und den Abtrieb 
signifikant erhöht. Dies heisst, dass das Fahrzeug an den Boden gezogen 
wird. Dies ermöglicht höhere Kurvengeschwindigkeiten und sorgt 
gleichzeitig für eine verbesserte Fahrzeugstabilität.

Ein weiteres wichtiges Element ist die aktive Aerodynamik, wie der 
verstellbare Heckflügel (DRS - Drag Reduction System). Dieser kann 
in bestimmten Zonen der Strecke geöffnet werden, um den Luftwiderstand 
zu reduzieren und die Höchstgeschwindigkeit zu steigern. Diese Funktion 
ist besonders wichtig für Überholmanöver und wird strategisch eingesetzt. Im folgenden Bild ist zu sehen, wie das DRS-System aktiviert ist.
'''
st.image("Projekt/P_data/GP_Photos/Lando_Norris,Chinese_GP_2024.jpg", width=600)
st.caption("Lando Norris, McLaren, GP von China 2024")
'''
Die Fahrzeugkarosserie ist mit komplexen Winglets, Leitblechen und 
Flügelelementen versehen, die den Luftstrom optimieren. Diese kleinen 
Details haben große Auswirkungen auf die Balance, die Effizienz und die 
Kühlung der Komponenten. Selbst minimale Änderungen an diesen Bauteilen 
können den Unterschied zwischen Sieg und Niederlage ausmachen. In den 
letzten Jahren hat sich auch der Fokus auf die Reduzierung von 
Luftverwirbelungen hinter dem Fahrzeug verstärkt, um das Verfolgen 
anderer Autos zu erleichtern und pannende Rennen zu fördern.
'''

st.subheader("Antrieb")
'''
Das Herz eines Formel-1-Fahrzeugs ist die Power Unit, ein 
Hybridantriebssystem, das einen 1,6-Liter-V6-Turbomotor mit mehreren 
Energierückgewinnungssystemen kombiniert. Der Motor erreicht beeindruckende 
Drehzahlen von bis zu 15.000 U/min und arbeitet mit einem außergewöhnlich 
hohen thermischen Wirkungsgrad.

Die Energierückgewinnungssysteme (ERS) bestehen aus zwei Hauptkomponenten: 
Der MGU-H wandelt Abwärme aus dem Turbolader in elektrische Energie um, 
während die MGU-K kinetische Energie aus der Bremsphase speichert. Diese 
Energie wird in hochentwickelten Lithium-Ionen-Batterien gespeichert und 
steht für zusätzliche Leistung zur Verfügung, wodurch der Hybridantrieb bis 
zu 160 zusätzliche PS liefern kann. Die Kombination aus Verbrennungs- und 
Elektromotor sorgt für eine beeindruckende Balance aus Leistung und Effizienz.

Im Bild unten ist ein Antriebsstrangs von Mercedes zu sehen.
'''
st.image("Projekt/P_data/GP_Photos/Mercedes_Antrieb.jpeg", width=600)
st.caption("Antriebsstrang von Mercedes")