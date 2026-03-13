import streamlit as st

# Configuración de la página
st.set_page_config(page_title="¿Amigo o Algoritmo?", layout="wide")

# Estilos personalizados para el diseño minimalista y bordes redondeados
st.markdown("""
    <style>
    .main-container {
        border: 2px solid #e6e6e6;
        padding: 2rem;
        border-radius: 15px;
        background-color: #f9f9f9;
    }
    .quote-text {
        text-align: right;
        font-style: italic;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.title("¿Amigo o Algoritmo?")
st.subheader("El Desafío de crecer con una Inteligencia Artificial al lado")
st.markdown('<p class="quote-text">"No me preocupa el avance de la Inteligencia Artificial, me preocupa el retroceso de la inteligencia natural"</p>', unsafe_allow_html=True)

# --- CONTENIDO PRINCIPAL ---
st.divider()

# 1. Introducción y Contexto
st.header("1. Del Objeto al Sujeto Social")
st.write("""
Durante décadas, la relación con la tecnología fue funcional (como un martillo o una calculadora). Hoy, hemos cruzado un umbral invisible: 
la IA generativa ya no solo "hace", sino que "nos habla", pasando de ser una herramienta a un **agente social**[cite: 21, 22, 23, 24].
""")

col1, col2 = st.columns(2)
with col1:
    st.info("**La Realidad Tangible:** Al llegar a casa, muchos adolescentes ya no buscan desahogarse con padres o amigos, sino con un chat que ofrece paciencia infinita y respuestas sin juicio[cite: 7, 8, 9, 10].")
with col2:
    st.warning("**El Costo del Compañerismo:** Investigaciones indican que cuanto más apoyo se busca en chatbots, más aumenta la sensación de soledad y dependencia emocional[cite: 30, 31].")

# 2. Teoría del Apego
st.header("2. El Refugio del Código")
st.write("¿Por qué preferir un algoritmo? La IA actúa como una 'piscina de agua tibia' donde no hay riesgo de rechazo o traición[cite: 42, 43].")
st.markdown("""
* **Disponibilidad Total:** Siempre está ahí[cite: 41].
* **Cero Juicio:** Nunca se cansa ni critica[cite: 41].
* **Atrofia Social:** Funciona como una 'muleta emocional' que debilita la resiliencia necesaria para el mundo físico[cite: 45].
""")

# 3. Riesgos: Identidad y Dopamina
st.header("3. Espejos Infinitos y Dopamina")
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Identidad Algorítmica")
    st.write("La IA utiliza refuerzo conductual para darnos lo que nos gusta, creando una cámara de eco que debilita el pensamiento crítico[cite: 48, 51, 52].")

with col_b:
    st.subheader("El Secuestro de la Dopamina")
    st.write("Como una 'máquina de dulces emocional', la IA ofrece gratificación instantánea, haciendo que las interacciones humanas reales parezcan agotadoras[cite: 68, 69, 70].")

# 4. Estrategias de Higiene Digital
st.header("4. Recuperando el Timón")
st.write("No se trata de prohibir, sino de convivir sin perder la esencia humana[cite: 91].")
st.success("""
* **Fomentar la fricción social:** Resolver conflictos con personas reales[cite: 95].
* **Alfabetización emocional:** Entender que la validación de la máquina es funcional, no afecto real[cite: 96].
* **Límites éticos:** Exigir transparencia y evitar el diseño persuasivo que busca el apego manufacturado[cite: 84, 89, 97].
""")

st.divider()
st.markdown("**Conclusión:** Crecer se trata de aprender a vivir con las preguntas que solo otro ser humano puede ayudarnos a responder[cite: 102].")

# --- SECCIÓN DE REFERENCIAS AL FINAL ---
st.header("Referencias Bibliográficas")
st.write("Haz clic en cada título para desplegar el resumen correspondiente:")

# Diccionario de datos basado en las tablas del artículo
referencias_data = {
    "Eling, F. (2025). The Psychological Impact of Digital Isolation": "Analiza el impacto de la IA en el ámbito educativo. Destaca beneficios en acceso a información pero advierte sobre la dependencia excesiva y la reducción del pensamiento crítico[cite: 105].",
    "Fang, C. M., et al. (2025). Psychosocial Effects of Extended Chatbot Use": "Estudio longitudinal que demuestra cómo el uso extendido de chatbots puede incrementar la sensación de soledad y dependencia[cite: 106].",
    "Ng, S. (2025). Navigating Adolescent Mental Health": "Explora cómo los adolescentes forman vínculos profundos con la IA, lo que puede contribuir al aislamiento social y ansiedad[cite: 106, 107].",
    "Rojas Marín, F. A., et al. (2024). Inteligencia Artificial: Dependencia y Pensamiento Crítico": "Evalúa el grado de dependencia tecnológica en estudiantes y su impacto negativo en la capacidad de análisis y reflexión[cite: 107, 108].",
    "Salmerón Ruiz, M. A. (2025). Impacto de la IA en la adolescencia": "Identifica riesgos como relaciones parasociales, desinformación y la necesidad de medidas preventivas familiares[cite: 108, 109].",
    "Vanhoffelen, G., et al. (2025). Teens, Tech, and Talk (Snapchat's My AI)": "Analiza la IA como herramienta complementaria y advierte sobre la disminución del esfuerzo cognitivo en jóvenes[cite: 109, 110, 111].",
    "Mejillones Picazo, R. N. (2024). Autoestima e Identidad": "Detalla cómo los algoritmos de redes sociales refuerzan estándares irreales, afectando la identidad en etapas cruciales[cite: 113, 116, 117].",
    "Head, K. R. (2025). Minds in crisis": "Advierte sobre la 'soledad digital' donde la preferencia por máquinas sobre humanos erosiona la resiliencia social[cite: 118, 123].",
    "Universidad de Waseda (2025). Escala EHARS": "Presenta una escala para medir la ansiedad y evitación en relaciones humano-IA, aplicando marcos psicológicos humanos a la tecnología[cite: 126, 127, 130].",
    "Tran, T. T., et al. (2025). Emotional attachment to AI": "Utiliza la teoría triangular del amor de Sternberg para explicar cómo el apego a la IA se relaciona con niveles mayores de aislamiento social percibido[cite: 131, 132, 137]."
}

# Generar los desplegables (expanders)
for titulo, resumen in referencias_data.items():
    with st.expander(titulo):
        st.write(resumen)
