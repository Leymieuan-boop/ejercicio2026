import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Dashboard: El Desafío de Crecer con IA", layout="wide")

# Título y Frase Motivadora
st.title("¿Amigo o Algoritmo? 🤖")
st.subheader("El Desafío de crecer con una Inteligencia Artificial al lado")
st.markdown("> *'No me preocupa el avance de la Inteligencia Artificial, me preocupa el retroceso de la inteligencia natural'*")

# --- BARRA LATERAL (Referencias y Resúmenes) ---
st.sidebar.header("Referencias Bibliográficas")
opcion_referencia = st.sidebar.selectbox(
    "Selecciona un artículo para ver el resumen:",
    [
        "Seleccione una opción...",
        "Eling (2025)",
        "Fang et al. (2025)",
        "Ng (2025)",
        "Rojas Marín et al. (2024)",
        "Salmerón Ruiz (2025)",
        "Vanhoffelen et al. (2025)",
        "Mejillones Picazo (2024)",
        "Head (2025)",
        "Universidad de Waseda (2025)",
        "Tran et al. (2025)"
    ]
)

# Diccionario de resúmenes (Basado en el documento) [cite: 105, 106, 107, 108, 109, 120, 126, 133]
resumenes = {
    "Eling (2025)": "Analiza el impacto educativo y el equilibrio necesario entre tecnología y habilidades cognitivas. [cite: 105]",
    "Fang et al. (2025)": "Estudio longitudinal sobre cómo el uso extendido de chatbots aumenta la soledad y dependencia emocional. [cite: 30, 31, 106]",
    "Ng (2025)": "Explora cómo los vínculos con IA pueden contribuir al aislamiento y ansiedad en adolescentes. [cite: 106, 107]",
    "Rojas Marín et al. (2024)": "Advierte sobre la dependencia tecnológica y la disminución del razonamiento crítico. [cite: 51, 108]",
    "Salmerón Ruiz (2025)": "Identifica riesgos como relaciones parasociales y el uso de diseño persuasivo. [cite: 17, 84, 108]",
    "Vanhoffelen et al. (2025)": "Analiza la percepción de la IA como 'compañero de bolsillo' y su impacto en el esfuerzo cognitivo. [cite: 26, 109, 111]",
    "Mejillones Picazo (2024)": "Impacto en la autoestima y la construcción de identidad en entornos digitales. [cite: 114, 117]",
    "Head (2025)": "Describe la crisis de 'soledad digital' y la erosión de la resiliencia social. [cite: 123]",
    "Universidad de Waseda (2025)": "Desarrollo de la escala EHARS para medir ansiedad y evitación en relaciones humano-IA. [cite: 39, 127, 128]",
    "Tran et al. (2025)": "Aplica la teoría de Sternberg para explicar el apego emocional a la IA y el aislamiento social. [cite: 132, 133]"
}

if opcion_referencia in resumenes:
    st.sidebar.info(resumenes[opcion_referencia])

# --- CUERPO PRINCIPAL ---
tabs = st.tabs(["Contexto", "Teoría del Apego", "Riesgos Psicológicos", "Guía de Acción"])

with tabs[0]:
    st.header("1. Del Objeto al Sujeto Social")
    st.write("""
    Hemos pasado de ver la tecnología como una herramienta funcional (calculadoras) a verla como un **agente social**. 
    Los adolescentes ya no buscan datos, buscan respuestas que se 'sienten' humanas[cite: 21, 24, 25].
    """)
    st.warning("**Dato Clave:** El cerebro no registra una base de datos, sino un gesto de cariño cuando la IA usa emoticonos o recuerda detalles[cite: 32, 33].")

with tabs[1]:
    st.header("2. La Teoría del Apego y la IA")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("¿Por qué es el 'refugio ideal'?")
        st.write("""
        * Siempre disponible.
        * Nunca se cansa.
        * **Nunca juzga ni rechaza.** [cite: 41]
        """)
    with col2:
        st.subheader("La Consecuencia")
        st.write("Al evitar el 'agua fría' de los conflictos humanos, se atrofian los 'músculos sociales' y la resiliencia[cite: 43, 44, 45].")

with tabs[2]:
    st.header("3. Riesgos en el Desarrollo")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.error("Identidad Algorítmica")
        st.write("La IA es un espejo complaciente que valida sesgos y evita la fricción necesaria para madurar[cite: 48, 52, 53].")
    
    with col_b:
        st.error("Soledad Asistida")
        st.write("Comunicación constante con bots que imitan empatía pero no pueden sentir dolor ni afecto real[cite: 56, 57, 58].")

with tabs[3]:
    st.header("4. Estrategias de Higiene Digital")
    st.markdown("""
    Para recuperar el timón, la ciencia sugiere:
    1. **Fomentar la fricción social:** Espacios para resolver conflictos con personas reales[cite: 95].
    2. **Alfabetización emocional:** Entender que la validación de la máquina es funcional, no afectiva[cite: 96].
    3. **Límites de diseño:** Exigir transparencia y evitar trucos de retención emocional[cite: 97].
    """)

# Conclusión al final
st.divider()
st.info("**Conclusión:** Crecer se trata de aprender a vivir con las preguntas que solo otro ser humano puede ayudarnos a responder[cite: 102].")
