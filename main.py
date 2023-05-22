import streamlit as st
from algoritmos.newton import newton_method
from algoritmos.cuasi_newton import cuasi_newton_method

# Definiciones

def mostrar_definiciones():
    st.header("Definiciones")
    
    st.subheader("Método de Newton")
    st.write("El método de Newton, también conocido como método de Newton-Raphson, es un algoritmo utilizado para encontrar aproximaciones sucesivas de las raíces de una función real. Fue desarrollado por el matemático Isaac Newton y, posteriormente, mejorado por Joseph Raphson.\n\nEl método de Newton se basa en la idea de que una función se puede aproximar mediante una recta tangente a su curva en un punto dado. La idea principal es comenzar con una suposición inicial cercana a la raíz buscada y, luego, utilizar la recta tangente para encontrar una mejor aproximación. Este proceso se repite iterativamente hasta que se obtenga una aproximación suficientemente precisa.")
    # Agrega aquí más información sobre el Método de Newton
    
    st.subheader("Método Cuasi-Newton")
    st.write("El método de cuasi-Newton es un algoritmo utilizado para encontrar aproximaciones de las raíces de una función, al igual que el método de Newton. Sin embargo, a diferencia del método de Newton, el método de cuasi-Newton no requiere calcular explícitamente la derivada de la función. En su lugar, utiliza una aproximación de la matriz Hessiana de la función para guiar la convergencia hacia la raíz.\n\nEl método de cuasi-Newton se basa en la idea de que la información proporcionada por las iteraciones anteriores se puede utilizar para construir una matriz que se aproxime a la matriz Hessiana de la función. La matriz Hessiana es una matriz de segundas derivadas parciales de la función y proporciona información sobre la curvatura de la función en cada punto.")
    # Agrega aquí más información sobre el Método Cuasi-Newton

# Aplicaciones

def mostrar_aplicaciones():
    st.header("Aplicaciones")
    
    st.subheader("Método de Newton")
    st.write("El método de Newton tiene numerosas aplicaciones en diversas áreas de la vida real debido a su capacidad para encontrar raíces de funciones. Aquí hay algunas aplicaciones comunes del método de Newton:\n\nOptimización: El método de Newton se puede utilizar para encontrar mínimos o máximos de funciones al encontrar las raíces de la derivada de la función objetivo. Esto es útil en problemas de optimización en campos como la ingeniería, economía, ciencias de la computación, entre otros.\n\nModelado y simulación: En ciencias e ingeniería, a menudo se necesita encontrar raíces de ecuaciones no lineales que representan sistemas físicos o fenómenos naturales. El método de Newton es ampliamente utilizado para resolver estas ecuaciones y obtener soluciones numéricas.\n\nCiencias físicas: En la física teórica y aplicada, el método de Newton se aplica para encontrar soluciones a ecuaciones diferenciales no lineales que describen fenómenos físicos. Por ejemplo, en mecánica clásica, se utiliza para resolver problemas de movimiento de partículas sujetas a fuerzas no lineales.\n\nFinanzas: En el campo de las finanzas, el método de Newton se utiliza en la valoración de derivados financieros y la resolución de ecuaciones relacionadas con los modelos de precios de opciones. También se aplica en la determinación de tasas de interés y en la gestión de riesgos financieros.\n\nProcesamiento de imágenes: En el procesamiento de imágenes y visión por computadora, el método de Newton se emplea para ajustar modelos matemáticos a datos de imágenes, como el ajuste de curvas y superficies a puntos de píxeles.\n\nAprendizaje automático: En el campo del aprendizaje automático, el método de Newton se utiliza en algoritmos de optimización, como la regresión logística o el entrenamiento de redes neuronales, para ajustar los parámetros del modelo a los datos observados.")
    # Agrega aquí más aplicaciones del Método de Newton
    
    st.subheader("Método Cuasi-Newton")
    st.write("El método de cuasi-Newton también tiene varias aplicaciones en la vida real. Algunas de ellas son:\n\nOptimización sin derivadas: A diferencia del método de Newton, el método de cuasi-Newton no requiere calcular derivadas de la función objetivo. Esto lo hace especialmente útil en problemas de optimización donde calcular las derivadas puede ser costoso o difícil. El método de cuasi-Newton se utiliza en algoritmos de optimización sin derivadas para encontrar mínimos o máximos de funciones en áreas como la ingeniería, economía y ciencias de la computación.\n\nAjuste de curvas y superficies: En disciplinas como la estadística y la ciencia de los datos, el método de cuasi-Newton se utiliza para ajustar modelos matemáticos a datos observados. Puede emplearse para ajustar curvas y superficies a puntos de datos, lo que permite obtener modelos que se ajusten de manera óptima a los datos disponibles.\n\nReconstrucción de imágenes médicas: En el campo de la imagen médica, el método de cuasi-Newton se utiliza para reconstruir imágenes a partir de datos de imágenes incompletos o ruidosos. Permite mejorar la calidad de las imágenes y obtener imágenes más claras y precisas en aplicaciones como la tomografía computarizada (TC) y la resonancia magnética (RM).\n\nAprendizaje automático y minería de datos: En el campo del aprendizaje automático y la minería de datos, el método de cuasi-Newton se utiliza en algoritmos de optimización para entrenar modelos de aprendizaje automático, como regresión logística y máquinas de vectores de soporte. Ayuda a ajustar los parámetros del modelo a los datos de entrenamiento y mejorar el rendimiento y la precisión de los modelos predictivos.\n\nAnálisis de redes y optimización de rutas: En aplicaciones de redes, como el enrutamiento de tráfico o la logística de transporte, el método de cuasi-Newton se aplica para optimizar rutas y asignar recursos de manera eficiente. Permite encontrar soluciones óptimas para problemas de planificación y asignación en redes complejas.")
    # Agrega aquí más aplicaciones del Método Cuasi-Newton

# Ejemplos

def mostrar_ejemplos():
    st.header("Ejemplos")
    
    st.subheader("Método de Newton")
    st.write("Supongamos que queremos encontrar una aproximación de la raíz cuadrada de un número dado, por ejemplo, la raíz cuadrada de 9. Queremos calcular esto utilizando el método de Newton.\n\nPasos del método de Newton:\n\n1. Elija una suposición inicial cercana a la raíz buscada. Podemos comenzar con x_0 = 2.\n\n2. Calcule el valor de la función en el punto x_0. En este caso, la función es f(x) = x^2 - 9. Por lo tanto, f(x_0) = (2)^2 - 9 = 4 - 9 = -5.\n\n3. Calcule la derivada de la función en el punto x_0. La derivada de f(x) = x^2 - 9 es f'(x) = 2x. Por lo tanto, f'(x_0) = 2(2) = 4.\n\n4. Utilice la fórmula de la recta tangente para encontrar la intersección de la recta tangente con el eje x:\n\nx_1 = x_0 - f(x_0) / f'(x_0) = 2 - (-5) / 4 = 2 + 5/4 = 2.25.\n\n5. Repita los pasos 2, 3 y 4 utilizando x_1 como el nuevo punto:\n\nf(x_1) = (2.25)^2 - 9 = 5.0625 - 9 = -3.9375.\n\nf'(x_1) = 2(2.25) = 4.5.\n\nx_2 = x_1 - f(x_1) / f'(x_1) = 2.25 - (-3.9375) / 4.5 = 2.25 + 3.9375 / 4.5 = 2.2361.\n\n6. Continúe este proceso iterativo hasta alcanzar la precisión deseada. En cada iteración, el valor de x se acerca más a la raíz cuadrada de 9.\n\nSiguientes iteraciones\n\nx_3 = 2.2361\n\nx_4 = 2.2361.\n\nx_5 = 2.2361.\n\n...\n\nCon cada iteración, el valor de x se mantiene en 2.2361. A medida que se realizan más iteraciones, el valor converge a la raíz cuadrada exacta de 9, que es 3.\n\nEste ejemplo ilustra cómo el método de Newton se utiliza para encontrar una aproximación de la raíz cuadrada de un número utilizando iteraciones sucesivas y la fórmula de la recta tangente.")
    # Agrega aquí un ejemplo de uso del Método de Newton
    
    st.subheader("Método Cuasi-Newton")
    st.write("Supongamos que queremos encontrar una aproximación de la raíz de la función f(x) = x^3 - 2x^2 - 5. Queremos calcular esto utilizando el método de cuasi-Newton utilizando la fórmula de actualización de Broyden-Fletcher-Goldfarb-Shanno (BFGS).\n\nPasos del método de cuasi-Newton:\n\n1. Elija una suposición inicial cercana a la raíz buscada. Podemos comenzar con x_0 = 2.\n\n2. Calcule el valor de la función en el punto x_0. En este caso, f(x_0) = (2)^3 - 2(2)^2 - 5 = 8 - 8 - 5 = -5.\n\n3. Inicialice una aproximación de la matriz Hessiana, H_0. Para este ejemplo, podemos comenzar con la matriz identidad de 2x2:\n\nH_0 = [[1, 0],\n\n[0, 1]]\n\n4. Calcule la dirección de búsqueda como el producto de la matriz aproximada Hessiana H_k y el gradiente de la función en el punto x_k:\n\n∇f(x_k) = [df/dx, df/dy]^T, donde df/dx es la derivada parcial de f con respecto a x y df/dy es la derivada parcial de f con respecto a y.\n\nPara nuestro ejemplo, ∇f(x_k) = [3x^2 - 4x, 0].\n\nd_k = -H_k * ∇f(x_k)\n\nd_0 = -H_0 * ∇f(x_0) = -[[1, 0], [0, 1]] * [3(2)^2 - 4(2), 0] = [-8, 0]\n\n5. Utilice alguna técnica de línea para determinar el tamaño del paso en la dirección de búsqueda. Supongamos que encontramos que α_k = 0.5.\n\nx_1 = x_0 + α_k * d_k = 2 + 0.5 * (-8) = -2.\n\n6. Calcule el valor de la función en el punto x_1:\n\nf(x_1) = (-2)^3 - 2(-2)^2 - 5 = -8 - 8 - 5 = -21.\n\n7. Actualice la matriz aproximada Hessiana utilizando la fórmula de actualización de BFGS:\n\nH_{k+1} = H_k + ((∇f(x_{k+1}) - ∇f(x_k)) * (∇f(x_{k+1}) - ∇f(x_k))^T) / ((∇f(x_{k+1}) - ∇f(x_k))^T * d_k)\n\n8. Repita los pasos 4, 5, 6 y 7 hasta que se alcance la precisión deseada o hasta que se cumpla algún criterio de parada predefinido.\n\nCon cada iteración, el valor de x se acerca más a la raíz de la función f(x). El método de cuasi-Newton utiliza la aproximación de la matriz Hessiana para mejorar las iteraciones y converger hacia la solución deseada.\n\nEste ejemplo ilustra cómo el método de cuasi-Newton, utilizando la fórmula de actualización de BFGS, se utiliza para encontrar una aproximación de la raíz de una función mediante iteraciones sucesivas y la actualización de la matriz Hessiana.")
    # Agrega aquí un ejemplo de uso del Método Cuasi-Newton

# Main

def main():
    url = 'https://github.com/KillTax/ProyectoMetodosNumericos2/tree/main/algoritmos'
    st.title("Métodos Numéricos: Newton y Cuasi-Newton")
    
    st.sidebar.title("Menú")
    seleccion = st.sidebar.selectbox("Seleccione una opción", ["Definiciones", "Aplicaciones", "Ejemplos"])
    
    if seleccion == "Definiciones":
        mostrar_definiciones()
    elif seleccion == "Aplicaciones":
        mostrar_aplicaciones()
    elif seleccion == "Ejemplos":
        mostrar_ejemplos()

    st.markdown(f'Para ver los codigos ir a [esta página]({url}')

if __name__ == "__main__":
    main()
