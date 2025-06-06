import streamlit as st
import math

st.title("🚴‍♂️ Fahrrad Watt-Ersparnis Rechner")
st.write("Berechne, wie viel schneller du durch Aerodynamik oder Watt-Ersparnis auf einer Strecke bist.")

leistung = st.number_input("🔌 Deine aktuelle Leistung (Watt)", value=200, min_value=50, max_value=500)
ersparnis = st.number_input("💨 Watt-Ersparnis (z. B. durch Aeroposition)", value=10, min_value=1, max_value=100)
strecke = st.number_input("🛣️ Strecke (km)", value=90, min_value=1, max_value=500)
gewicht = st.number_input("⚖️ Gesamtgewicht (Rad + Fahrer, kg)", value=75.0, min_value=40.0, max_value=120.0)
cda = st.number_input("🌀 Luftwiderstandsbeiwert (CdA)", value=0.25, min_value=0.18, max_value=0.4, step=0.01)

def berechne_kmh(power, gewicht, cda):
    luftdichte = 1.226
    rollwiderstand = 0.004
    g = 9.81

    def widerstand(v):
        w_luft = 0.5 * luftdichte * cda * v**2
        w_roll = rollwiderstand * gewicht * g
        return (w_luft + w_roll) * v

    v = 1.0
    for _ in range(1000):
        p = widerstand(v)
        v += (power - p) * 0.01
        if abs(power - p) < 0.1:
            break
    return v * 3.6

v_alt = berechne_kmh(leistung, gewicht, cda)
v_neu = berechne_kmh(leistung + ersparnis, gewicht, cda)

zeit_alt = strecke / v_alt * 60
zeit_neu = strecke / v_neu * 60
ersparnis_min = zeit_alt - zeit_neu

st.subheader("📈 Ergebnis")
st.write(f"**Geschwindigkeit vorher:** {v_alt:.2f} km/h")
st.write(f"**Geschwindigkeit nachher:** {v_neu:.2f} km/h")
st.write(f"**Zeit vorher:** {zeit_alt:.1f} Minuten")
st.write(f"**Zeit nachher:** {zeit_neu:.1f} Minuten")
st.success(f"💡 Du sparst etwa **{ersparnis_min:.1f} Minuten** auf {strecke} km!")
