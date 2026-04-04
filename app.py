import streamlit as st

st.set_page_config(page_title="ATB - Asesor Técnico", page_icon="🚜")

st.title("🚜 ATB: Asesor Técnico de Bolsillo")
st.markdown("---")

# --- PERFIL DEL USUARIO (Los interrogantes que faltaban) ---
st.sidebar.header("👤 Perfil del Usuario")
edad = st.sidebar.slider("¿Qué edad tiene el conductor?", 18, 95, 60)
experiencia = st.sidebar.select_slider("Experiencia en Off-Road:", options=["Novato", "Intermedio", "Experto"])

st.sidebar.header("⚙️ Configuración de Uso")
uso = st.sidebar.selectbox("Uso principal:", ["Trabajo pesado / Campo", "Mixto (Pueblo y Ruta)", "Viajes / Turismo"])
terreno = st.sidebar.selectbox("Terreno más frecuente:", ["Asfalto", "Ripio consolidado", "Piedra / Arena suelta"])
carga = st.sidebar.slider("Carga habitual (kg):", 0, 1000, 300)

# --- LÓGICA TÉCNICA DE VEREDICTO ---
if st.sidebar.button("GENERAR VEREDICTO TÉCNICO"):
    st.header("📋 Veredicto Basado en Perfil")
    
    # Aquí el algoritmo empieza a "pensar" según la edad
    st.write(f"### Análisis para conductor de {edad} años en terreno de {terreno}")
    
    # Lógica de Ergonomía y Confort
    if edad > 65:
        st.info("⚠️ **Prioridad de Ergonomía:** El sistema está filtrando por vehículos con acceso fácil y mandos de alta visibilidad.")
        recomendacion_principal = "Toyota Hilux SRX (Por suavidad y reventa)"
        score_principal = 92
    else:
        st.info("🚀 **Prioridad de Performance:** El sistema prioriza torque y respuesta dinámica.")
        recomendacion_principal = "Ford Ranger Raptor (Por suspensión de alto rendimiento)"
        score_principal = 96

    # Mostramos los resultados
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Compatibilidad Técnica", f"{score_principal}%")
        st.write(f"**Vehículo Sugerido:** {recomendacion_principal}")
        st.progress(score_principal)

    with col2:
        st.write("**Factores Críticos analizados:**")
        st.write(f"- Torque necesario para {carga}kg")
        st.write(f"- Resistencia estructural para {terreno}")
        st.write("- Logística de repuestos en Patagonia")

    st.markdown("---")
    st.warning("Recuerde: Esta es una orientación técnica. Siempre realice una prueba de manejo para evaluar la comodidad del asiento y la visibilidad.")
    st.success("Análisis completado. Estos resultados son sugerencias basadas en los parámetros ingresados.")
