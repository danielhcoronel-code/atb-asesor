import streamlit as st

st.set_page_config(page_title="ATB - Asesor Técnico Pro", page_icon="🚜")

st.title("🚜 ATB: Asesor Técnico de Bolsillo")
st.markdown("---")

# --- EXPLICACIÓN PREVIA (Lo que pediste) ---
st.info("""
**Nota de Rigor Técnico:** Este sistema no solo analiza fierros. Para que el consejo sea útil, 
necesitamos entender tus limitaciones físicas, tu entorno familiar y el destino real del vehículo. 
Un motor potente no sirve si la ergonomía del asiento te lastima o si no entran todos tus nietos.
""")

# --- PANEL DE CONFIGURACIÓN ---
st.sidebar.header("👤 Perfil del Usuario")
edad = st.sidebar.slider("¿Qué edad tiene el conductor?", 18, 95, 66)
familia = st.sidebar.number_input("¿Cuántos viajan usualmente?", 1, 7, 2)

# --- LISTA DE CONDICIONES FÍSICAS (Multiselección) ---
st.sidebar.subheader("🩺 Factores de Salud")
condiciones = st.sidebar.multiselect(
    "Seleccione si padece alguna condición que limite el confort:",
    ["Lumbalgia Crónica / Dolor de Espalda", "Movilidad Reducida (Dificultad para subir/bajar)", "Problemas de Visión Nocturna", "Fatiga rápida en viajes largos"]
)

st.sidebar.header("🛣️ Destino y Uso")
destino = st.sidebar.selectbox("Uso principal:", 
    ["Trabajo de campo / Carga pesada", "Uso mixto (Pueblo y Ruta)", "Viajes largos / Turismo de aventura"])
terreno = st.sidebar.selectbox("Terreno más frecuente:", 
    ["Asfalto", "Ripio consolidado (Jacobacci y zona)", "Piedra suelta / Arena", "Barro / Nieve profunda"])

# --- LÓGICA DE PROCESAMIENTO ---
if st.sidebar.button("GENERAR VEREDICTO TÉCNICO"):
    st.header("📋 Veredicto de Compatibilidad Real")
    
    # Análisis de salud y ergonomía
    if "Lumbalgia Crónica / Dolor de Espalda" in condiciones or edad > 65:
        st.warning("⚠️ **ALERTA DE ERGONOMÍA:** Por su perfil, el sistema penaliza vehículos con suspensiones traseras de elásticos rígidos (sin carga). Se recomienda buscar esquemas de suspensión independiente o amortiguación con válvulas de confort.")
    
    if familia > 4:
        st.error("🚨 **ALERTA DE ESPACIO:** Para más de 4 personas, una pickup cabina simple queda descartada. Se requiere SUV de 3 filas o PickUp Cabina Doble con buen espacio en plazas traseras.")

    # Simulación de puntajes técnicos
    st.subheader("Opciones sugeridas para su realidad:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### La Opción Lógica")
        st.write("**Toyota Hilux SRX / GR-S**")
        st.write("- **Puntaje:** 89%")
        st.write("- **Por qué:** Mejor reventa y service en la zona de Río Negro.")
        if "Lumbalgia Crónica / Dolor de Espalda" in condiciones:
            st.write("*Nota: La GR-S tiene mejor amortiguación para su espalda que la versión común.*")

    with col2:
        st.write("### La Opción Confort")
        st.write("**Ford Ranger (Nueva Generación)**")
        st.write("- **Puntaje:** 94%")
        st.write("- **Por qué:** Su nueva suspensión y butacas son las más ergonómicas del mercado hoy.")
        st.progress(94)

    st.markdown("---")
    st.write("#### 🛡️ Resumen de Análisis Físico-Mecánico:")
    st.write(f"- **Esfuerzo de acceso:** {'Bajo (Recomendado)' if edad > 65 else 'Estándar'}")
    st.write(f"- **Capacidad de Habitáculo:** {'Suficiente' if familia <= 4 else 'Crítica'}")
    st.write(f"- **Resistencia de Chasis:** {'Alta para ' + terreno if 'Ripio' in terreno else 'Estándar'}")
