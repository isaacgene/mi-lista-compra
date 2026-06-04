import streamlit as st

# Configuración de la página para móviles
st.set_page_config(page_title="Lista Compra", page_icon="🛒", layout="centered")

# Estilos CSS para optimizar el diseño en la pantalla del iPhone
st.markdown("""
    <style>
    /* Estilo para los nombres de los productos */
    .producto-label {
        font-size: 1.1rem !important;
        font-weight: 500;
        display: flex;
        align-items: center;
        height: 100%;
    }
    /* Reducir espacio entre elementos para que quepa más en la pantalla */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    /* Estilo para nuestro nuevo botón real de copiar */
    .boton-copiar {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 12px;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    }
    .boton-copiar:active {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Tu lista de compras organizada por categorías
PRODUCTOS_POR_CATEGORIA = {
    "🥩 Frescos, Carne y Huevos": [
        "Huevos", "Pechuga de pollo", "Pavo lonchas", "Mantequilla", "Keffir"
    ],
    "🧀 Quesos y Lácteos": [
        "Queso lonchas cremoso", "Cuatro quesos", "Queso roquefort", "Queso de cabra",
        "Yogur stracciatella", "Yogur griego", "Nata Cocinar"
    ],
    "🥬 Frutería y Verduras": [
        "Cebollas", "Tomate ensalada", "Lechuga"
    ],
    "🧊 Congelados y Platos Preparados": [
        "Cebolla congelada", "Patatas congeladas", "Patatas conill", "Pure de verduras", 
        "Ensalada de pasta", "Pizzas", "Figuras merluza"
    ],
    "🥫 Despensa y Pasta": [
        "Pan de molde", "Bagels", "Puré patata", "Tomate frito", "Tomate pasta", 
        "Macarrones", "Espaguetis", "Pasta estrella", "Mayonesa", "Ketchup", 
        "Paté finas hierbas"
    ],
    "🍫 Snacks y Postres": [
        "Crema Catalana", "Natillas", "Tableta chocolate", "Patatas bolsa", "Palomitas"
    ],
    "🥤 Bebidas": [
        "Zumos", "Botellas de agua pequeñas", "Garrafas de agua", "CocaCola Zero", "Tónica", "Cerveza"
    ],
    "🧼 Higiene y Limpieza": [
        "Salvaslips", "Papel higiénico", "Papel cocina", "Desodorante", "Toallitas desmaquillantes",
        "Lavavajillas", "Toallitas antitransferencia", "Toallitas WC", "Toallitas húmedas"
    ]
}

st.title("🛒 Mi Lista de la Compra")
st.write("Indica la cantidad de lo que necesites (deja en 0 lo que no quieras):")

# 2. Renderizar la interfaz
productos_seleccionados = []

for categoria, productos in PRODUCTOS_POR_CATEGORIA.items():
    st.write(f"### {categoria}")
    
    for producto in productos:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"<div class='producto-label'>{producto}</div>", unsafe_allow_html=True)
            
        with col2:
            cantidad = st.number_input(
                label=f"Cantidad para {producto}",
                min_value=0,
                max_value=20,
                value=0,
                step=1,
                key=f"cant_{producto}",
                label_visibility="collapsed"
            )
        
        if cantidad > 0:
            if cantidad == 1:
                productos_seleccionados.append(f"{producto}")
            else:
                productos_seleccionados.append(f"{producto} ({cantidad}x)")

st.write("---")

# 3. Generar el bloque de texto y el botón de copiar real
if productos_seleccionados:
    st.subheader("📝 Tu Lista Generada")
    
    texto_final = "\n".join(productos_seleccionados)
    
    # Mostramos la lista en un cuadro de texto normal para que la veas
    st.text_area("Tu lista actual:", value=texto_final, height=150, disabled=True)
    
    # TRUCO: Inyectamos un botón nativo de HTML/JavaScript. 
    # Este código se ejecuta 100% en tu iPhone y SÍ tiene permiso para copiar al portapapeles.
    componente_copiar_html = f"""
    <input type="hidden" id="textoParaCopiar" value="{texto_final}">
    <button class="boton-copiar" onclick="copiarAlPortapapeles()">📋 COPIAR LISTA COMPLETA</button>

    <script>
    function copiarAlPortapapeles() {{
        var text = document.getElementById("textoParaCopiar").value;
        
        // Intento con la API moderna de portapapeles
        if (navigator.clipboard && navigator.clipboard.writeText) {{
            navigator.clipboard.writeText(text).then(function() {{
                alert("✨ ¡Lista copiada al portapapeles! Ya puedes ir a Google Keep y pegar.");
            }}).catch(function(err) {{
                alert("Error al copiar de forma automática. Intenta seleccionar el texto manualmente.");
            }});
        }} else {{
            // Método antiguo de emergencia por si falla en navegadores viejos
            var textArea = document.createElement("textarea");
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            try {{
                document.execCommand('copy');
                alert("✨ ¡Lista copiada al portapapeles! Ya puedes ir a Google Keep y pegar.");
            }} catch (err) {{
                alert("No se pudo copiar.");
            }}
            document.body.removeChild(textArea);
        }}
    }}
    </script>
    """
    
    # Renderizamos el botón nativo en la app
    st.components.v1.html(componente_copiar_html, height=70)
    
else:
    st.info("💡 Incrementa la cantidad de los productos que te falten en casa para generar la lista.")
