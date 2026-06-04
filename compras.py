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
    /* Estilo para el botón principal */
    .stButton button {
        width: 100%;
        background-color: #4CAF50 !important;
        color: white !important;
        font-size: 1.1rem !important;
        padding: 10px !important;
    }
    /* Reducir espacio entre elementos para que quepa más en la pantalla */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
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
        
        # Si la cantidad es mayor que 0, lo añadimos a la lista final (sin el guion "-")
        if cantidad > 0:
            if cantidad == 1:
                productos_seleccionados.append(f"{producto}")
            else:
                productos_seleccionados.append(f"{producto} ({cantidad}x)")

st.write("---")

# 3. Generar el bloque de texto para copiar
if productos_seleccionados:
    st.subheader("📝 Tu Lista Generada")
    
    texto_final = "\n".join(productos_seleccionados)
    
    st.text_area("Toca dentro, selecciona todo y copia:", value=texto_final, height=180)
    st.info("💡 ¡Listo! Ahora solo tienes que pegar este texto en tu nota de Google Keep.")
else:
    st.info("💡 Incrementa la cantidad de los productos que te falten en casa para generar la lista.")
