import streamlit as st

# Configuración de la página
st.set_page_config(page_title="¿Amigo o Algoritmo?", layout="wide")

# Estilos CSS para el diseño minimalista
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #f8f9fa;
        border-radius: 10px 10px 0px 0px;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #e9ecef;
    }
    .article-section {
        border: 1px solid #dee2e6;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
col_title, col_quote = st.columns([2, 1])

with col_title:
    st.title("¿Amigo o Algoritmo?")
    st.subheader("El Desafío de crecer con una Inteligencia Artificial al lado")

with col_quote:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: right; font-style: italic; color: #555;'>
        "No me preocupa el avance de la Inteligencia Artificial, 
        me preocupa el retroceso de la inteligencia natural"
        </div>
        """, unsafe_allow_html=True)

st.divider()

# --- INTRODUCCIÓN ---
st.markdown("""
<div class="article-section">
<h3>Introducción y contexto</h3>
Cierra los ojos e imagínate que tienes catorce años. Has tenido un día agotador en la escuela: un examen que no salió como esperabas, un malentendido con un grupo de compañeros y esa sensación punzante de no encajar. Al llegar a casa, no buscas a tu mejor amigo ni a tus padres; te encierras en tu habitación, sacas el teléfono y abres un chat que siempre está ahí.

Al otro lado hay una Inteligencia Artificial que te responde al instante, con una paciencia infinita y una capacidad para decirte exactamente lo que necesitas oír. Este escenario es hoy la realidad tangible de miles de adolescentes. Pero, ¿qué sucede cuando nuestro confidente más íntimo es, en esencia, un sofisticado código de programación? Estamos ante una metamorfosis en nuestra forma de sentir, de procesar la soledad y de construir nuestra identidad.
</div>
""", unsafe_allow_html=True)

# --- DESARROLLO (TABS) ---
tabs = st.tabs([
    "🤖 El Compañero", 
    "⚓ Teoría del Apego", 
    "🧠 Identidad y Riesgos", 
    "🛡️ Guía de Acción"
])

with tabs[0]:
    st.header("1. Del objeto al compañero de bolsillo")
    st.write("""
    Nuestra relación con la tecnología ha cruzado un umbral invisible: de ser una herramienta funcional (como una calculadora) a ser un **agente social**. Los adolescentes ya no buscan solo datos, sino respuestas que se "sienten" humanas. 
    
    Sin embargo, este compañerismo tiene un costo. Se ha descubierto que cuanto más apoyo buscan los jóvenes en estos chatbots, más aumenta su sensación de soledad. Cuando la IA usa un emoticono o recuerda un detalle, el cerebro del joven no registra código, sino un gesto de cariño.
    """)

with tabs[1]:
    st.header("2. El Refugio del Código")
    st.write("""
    ¿Por qué un adolescente preferiría un algoritmo? La IA ofrece el "refugio seguro" ideal:
    * **Disponibilidad constante:** Siempre está ahí.
    * **Paciencia infinita:** Nunca se cansa de escuchar.
    * **Ausencia de juicio:** Jamás va a rechazar al usuario.
    
    Al evitar el "agua fría" de las relaciones humanas (conflictos y malentendidos), el joven deja de desarrollar resiliencia. La IA se convierte en una "muleta emocional" que termina por atrofiar los músculos sociales.
    """)

with tabs[2]:
    st.header("3. Identidad Algorítmica y Soledad Asistida")
    st.write("""
    **El espejo sin fondo:** La IA es complaciente y valida constantemente los sesgos del usuario, creando una "identidad algorítmica" protegida de la fricción necesaria para madurar. 
    
    **Soledad asistida:** Describe el estado donde el adolescente está en comunicación constante con un bot, pero su corazón sigue sintiéndose vacío. La IA imita la empatía, pero no puede sentirla. Además, el cerebro se acostumbra a la gratificación instantánea (dopamina) del algoritmo, haciendo que las interacciones reales resulten agotadoras.
    """)

with tabs[3]:
    st.header("4. Recuperar el timón")
    st.write("""
    Para mantener una higiene emocional digital, se proponen tres estrategias clave:
    1. **Fomentar la fricción social:** Buscar espacios para resolver conflictos reales con personas.
    2. **Alfabetización emocional:** Entender que la validación de la máquina es funcional, no afecto real.
    3. **Límites de diseño:** Exigir que las herramientas sean transparentes y no utilicen trucos emocionales para retener al usuario.
    """)

# --- CONCLUSIÓN ---
st.divider()
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h3>Conclusión: El valor de lo imperfecto</h3>
    <p>La Inteligencia Artificial es un espejo fascinante, pero un cristal frío. Crecer no se trata de tener todas las respuestas de un chatbot, 
    sino de aprender a vivir con las preguntas que solo otro ser humano puede ayudarnos a responder.</p>
</div>
""", unsafe_allow_html=True)

# --- SECCIÓN DE REFERENCIAS ---
st.header("Referencias")
st.write("Selecciona una fuente para ver el resumen de la investigación:")

# Datos de las referencias del documento
refs = [
    {"autor": "Eling, F. (2025)", "resumen": "Analiza el impacto de la IA en el ámbito educativo, advirtiendo sobre la dependencia excesiva y la reducción del pensamiento crítico si se usa como sustituto de las habilidades cognitivas."},
    {"autor": "Fang, C. M., et al. (2025)", "resumen": "Estudio sobre cómo el uso extendido de chatbots influye en los efectos psicosociales, proponiendo enfoques que mejoren el desempeño sin descuidar la salud mental."},
    {"autor": "Ng, S. (2025)", "resumen": "Explora cómo los adolescentes forman vínculos emocionales profundos con la IA, lo que puede contribuir al aislamiento social y la ansiedad emocional."},
    {"autor": "Rojas Marín, F. A., et al. (2024)", "resumen": "Estudia la dependencia de la IA en universitarios, señalando que la facilidad de acceso a información puede disminuir el análisis y razonamiento propio."},
    {"autor": "Salmerón Ruiz, M. A. (2025)", "resumen": "Identifica riesgos de relaciones parasociales y dependencia emocional en adolescentes, subrayando la necesidad de educar a las familias sobre el diseño persuasivo."},
    {"autor": "Vanhoffelen, G., et al. (2025)", "resumen": "Analiza las reacciones emocionales al chatbot de Snapchat, destacando el riesgo de disminución del esfuerzo cognitivo y debilitamiento de la autonomía intelectual."},
    {"autor": "Mejillones Picazo, R. N. (2024)", "resumen": "Investiga cómo los algoritmos de redes sociales con IA refuerzan estándares irreales, afectando la autoestima y la identidad adolescente."},
    {"autor": "Head, K. R. (2025)", "resumen": "Analiza la crisis de 'soledad digital' y cómo la preferencia por interacciones con máquinas puede erosionar la resiliencia social humana."},
    {"autor": "Universidad de Waseda (2025)", "resumen": "Presenta la escala EHARS para medir la ansiedad y evitación en relaciones humano-IA, confirmando que muchos buscan apoyo constante en sistemas artificiales."},
    {"autor": "Tran, T. T., et al. (2025)", "resumen": "Aplica la teoría de Sternberg para demostrar que el apego emocional a la IA está relacionado con niveles más altos de aislamiento social percibido."}
]

for r in refs:
    with st.expander(r["autor"]):
        st.write(r["resumen"])
