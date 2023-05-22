import streamlit as st
from algoritmos.newton import newton_method
from algoritmos.cuasi_newton import cuasi_newton_method

# Definiciones

def mostrar_definiciones():
    st.header("Definiciones")
    
    st.subheader("Método de Newton")
    st.write("El Método de Newton es un algoritmo de optimización numérica utilizado para encontrar raíces o soluciones de ecuaciones no lineales. \nEl método de Newton, también conocido como método de Newton-Raphson, es un algoritmo utilizado para encontrar aproximaciones sucesivas de las raíces de una función real. Fue desarrollado por el matemático Isaac Newton y, posteriormente, mejorado por Joseph Raphson.\nEl método de Newton se basa en la idea de que una función se puede aproximar mediante una recta tangente a su curva en un punto dado. La idea principal es comenzar con una suposición inicial cercana a la raíz buscada y, luego, utilizar la recta tangente para encontrar una mejor aproximación. Este proceso se repite iterativamente hasta que se obtenga una aproximación suficientemente precisa.")
    # Agrega aquí más información sobre el Método de Newton
    
    st.subheader("Método Cuasi-Newton")
    st.write("El Método Cuasi-Newton es un método de optimización iterativo utilizado para resolver problemas de optimización no lineales.\nEl método de cuasi-Newton es un algoritmo utilizado para encontrar aproximaciones de las raíces de una función, al igual que el método de Newton. Sin embargo, a diferencia del método de Newton, el método de cuasi-Newton no requiere calcular explícitamente la derivada de la función. En su lugar, utiliza una aproximación de la matriz Hessiana de la función para guiar la convergencia hacia la raíz.\nEl método de cuasi-Newton se basa en la idea de que la información proporcionada por las iteraciones anteriores se puede utilizar para construir una matriz que se aproxime a la matriz Hessiana de la función. La matriz Hessiana es una matriz de segundas derivadas parciales de la función y proporciona información sobre la curvatura de la función en cada punto.")
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

# Main

def main():
    st.title("Métodos Numéricos: Newton y Cuasi-Newton")
    
    st.sidebar.title("Menú")
    seleccion = st.sidebar.selectbox("Seleccione una opción", ["Definiciones", "Aplicaciones", "Ejemplos"])
    
    if seleccion == "Definiciones":
        mostrar_definiciones()
    elif seleccion == "Aplicaciones":
        mostrar_aplicaciones()
    elif seleccion == "Ejemplos":
        mostrar_ejemplos()

if __name__ == "__main__":
    main()
