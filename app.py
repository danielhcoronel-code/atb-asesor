import streamlit as st

st.set_page_config(page_title="ATB - Asesor Técnico Pro", page_icon="🚜")

st.title("🚜 ATB: Asesor Técnico de Bolsillo")
st.markdown("---")

st.info("""
**Rigor Técnico ATB:** El vehículo es tu segunda piel. Analizamos qué estructura te conviene 
según tu fisonomía, tus gustos y el terreno que pisás.
""")

# --- PANEL DE CONFIGURACIÓN ---
st.sidebar.header("👤 Perfil del Usuario")
nombre = "Daniel" # Esto es para personalizar el veredicto
edad = st.sidebar.slider("¿Qué edad tiene el conductor?", 18, 95, 66)
familia = st.sidebar.number_input("¿Cuántos viajan usualmente?", 1, 7, 2)

# --- PREGUNTA POR EL "ENVOLTORIO" ---
st.sidebar.header("🛡️ Preferencia de Estilo")
envoltorio = st.sidebar.selectbox(
    "¿Qué tipo de vehículo preferís que te 'envuelva'?",
    ["Pickup (Robusta y Alta)", "SUV (Confort y Espacio)", "Sedán (Estable y Bajo)", "Deportivo (Ágil y Rápido)"]
)

# --- LISTA DE SALUD ---
st.sidebar.subheader("🩺 Factores de Salud")
condiciones = st.sidebar.multiselect(
    "Seleccione condiciones para ajustar ergonomía:",
    ["Lumbalgia Crónica / Dolor de Espalda", "Movilidad Reducida", "Uso de anteojos permanentes"]
)

st.sidebar.header("🛣️ Destino y Uso")
terreno = st.sidebar.selectbox("Terreno más frecuente:", 
    ["Asfalto", "Ripio / Tierra (Zona Jacobacci)", "Piedra / Arena", "Nieve / Barro"])

# --- LÓGICA DE PROCESAMIENTO ---
if st.sidebar.button("GENERAR VEREDICTO TÉCNICO"):
    st.header("📋 Veredicto de Compatibilidad")
    
    # Cruce de datos: Gusto vs. Realidad
    if envoltorio == "Sedán (Estable y Bajo)" and "Ripio" in terreno:
        st.error(f"⚠️ **Incompatibilidad Física:** Daniel, un Sedán en el ripio sufre por despeje. El 'envoltorio' es cómodo pero la mecánica va a estar expuesta a golpes en el cárter.")
    
    if envoltorio == "Deportivo (Ágil y Rápido)" and edad > 60:
        st.warning("⚠️ **Advertencia de Ergonomía:** Los deportivos tienen butacas muy bajas. Entrar y salir puede ser un desafío para la columna.")

    # Resultados sugeridos
    st.subheader(f"Propuestas para {envoltorio}:")
    
    col1, col2 = st.columns(2)
    with col1:
        if "Pickup" in envoltorio:
            st.write("### Ford Ranger V6")
            st.write("**Puntaje:** 95%")
            st.write("Excelente 'jaula' de seguridad y confort de marcha.")
        else:
            st.write("### Toyota SW4 (SUV)")
            st.write("**Puntaje:** 91%")
            st.write("Te 'envuelve' con la solidez de una chata pero con interior de auto de lujo.")

    with col2:
        st.write("**Variables de Seguridad:**")
        st.write(f"- Altura de cadera: {'Óptima' if 'SUV' in envoltorio or 'Pickup' in envoltorio else 'Baja'}")
        st.write(f"- Protección estructural: Alta")
        st.write(f"- Aptitud para {terreno}: {'Alta' if 'Ripio' in terreno and 'Pickup' in envoltorio else 'Media'}")

    st.success("Análisis finalizado. La máquina priorizó tu comodidad física sobre la estética.")
