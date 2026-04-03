import streamlit as st

# Configuración de la página (título que se ve en la pestaña)
st.set_page_config(page_title="ATB - Asesor de Automóviles", page_icon="🚜")

# Título Principal
st.title("🚜 ATB: Asesor Técnico de Bolsillo")
st.subheader("Orientación basada en rigor técnico y contexto real")
st.markdown("---")

# --- BARRA LATERAL PARA INPUTS ---
st.sidebar.header("⚙️ Configuración de Uso")
terreno = st.sidebar.selectbox("Tipo de Terreno Dominante:", ["Asfalto Urbano", "Ripio / Tierra", "Off-Road Pesado"])
carga = st.sidebar.slider("Carga adicional estimada (kg):", 0, 1000, 300)
clima = st.sidebar.radio("Clima predominante:", ["Templado", "Frío Extremo (Patagonia)"])
eco = st.sidebar.toggle("Priorizar nuevas energías (Híbridos/EV)")

# --- BOTÓN DE ACCIÓN ---
if st.sidebar.button("GENERAR VEREDICTO TÉCNICO"):
    st.header("📋 Resultados del Análisis Técnico")
    
    # Aquí creamos dos columnas para mostrar opciones comparativas
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Opción A: Máxima Robustez")
        st.write("**Ford Ranger Raptor**")
        st.progress(95)
        st.info("Recomendada por su esquema de suspensión Fox y torque para el ripio.")
        
    with col2:
        st.write("### Opción B: Eficiencia Importada")
        st.write("**BYD Leopard 5**")
        st.progress(88)
        st.warning("Excelente torque instantáneo. Verificar service oficial en la zona.")

    st.success("Análisis completado. Estos resultados son sugerencias basadas en los parámetros ingresados.")
