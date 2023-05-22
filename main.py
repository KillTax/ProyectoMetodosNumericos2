import streamlit as st
import os

# Definiciones

def mostrar_definiciones():
    st.header("Definiciones")
    
    st.subheader("Método de Newton")
    st.write("El Método de Newton es un algoritmo de optimización numérica utilizado para encontrar raíces o soluciones de ecuaciones no lineales.")
    # Agrega aquí más información sobre el Método de Newton
    
    st.subheader("Método Cuasi-Newton")
    st.write("El Método Cuasi-Newton es un método de optimización iterativo utilizado para resolver problemas de optimización no lineales.")
    # Agrega aquí más información sobre el Método Cuasi-Newton

# Aplicaciones

def mostrar_aplicaciones():
    st.header("Aplicaciones")
    
    st.subheader("Método de Newton")
    st.write("El Método de Newton tiene diversas aplicaciones en áreas como la física, ingeniería y ciencias computacionales.")
    # Agrega aquí más aplicaciones del Método de Newton
    
    st.subheader("Método Cuasi-Newton")
    st.write("El Método Cuasi-Newton se utiliza en problemas de optimización no lineales en campos como la economía, la física y la ingeniería.")
    # Agrega aquí más aplicaciones del Método Cuasi-Newton

# Ejemplos

def mostrar_ejemplos():
    st.header("Ejemplos")
    
    st.subheader("Método de Newton")
    # Agrega aquí un ejemplo de uso del Método de Newton
    
    st.subheader("Método Cuasi-Newton")
    # Agrega aquí un ejemplo de uso del Método Cuasi-Newton

# Código de los algoritmos

def mostrar_codigo_algoritmo(algoritmo):
    codigo_path = os.path.join("algoritmos", algoritmo + ".py")
    
    with open(codigo_path, "r") as file:
        codigo = file.read()
    
    st.code(codigo)

# Main

def main():
    st.title("Métodos Numéricos: Newton y Cuasi-Newton")
    
    st.sidebar.title("Menú")
    seleccion = st.sidebar.selectbox("Seleccione una opción", ["Definiciones", "Aplicaciones", "Ejemplos", "Códigos"])
    
    if seleccion == "Definiciones":
        mostrar_definiciones()
    elif seleccion == "Aplicaciones":
        mostrar_aplicaciones()
    elif seleccion == "Ejemplos":
        mostrar_ejemplos()
    elif seleccion == "Códigos":
        st.header("Códigos de los algoritmos")
        algoritmos = os.listdir("algoritmos")
        algoritmo_seleccionado = st.selectbox("Seleccione un algoritmo", algoritmos)
        mostrar_codigo_algoritmo(algoritmo_seleccionado)

if __name__ == "__main__":
    main()
