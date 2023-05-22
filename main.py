"""
Método de Newton

En este archivo se explicará brevemente el método de Newton, su definición, aplicaciones y se proporcionará un ejemplo de uso.

1. Método de Newton:
El método de Newton es un algoritmo de optimización numérica utilizado para encontrar raíces o soluciones de
ecuaciones no lineales. Utiliza el concepto de la derivada para aproximar la solución iterativamente.

Definición:
Dada una función f(x), el método de Newton busca encontrar el valor de x para el cual f(x) es igual a cero.
El método utiliza la aproximación lineal de la función alrededor de un punto inicial x0 para calcular una nueva
estimación de la raíz.

Aplicaciones:
- Encontrar raíces de ecuaciones no lineales.
- Optimización numérica.
- Resolución de sistemas de ecuaciones no lineales.

Ejemplo:

Supongamos que queremos encontrar la raíz de la función f(x) = x^2 - 4. Podemos utilizar el método de Newton para esto.

Pasos del método de Newton:

1. Elegir un punto inicial x0.
2. Calcular la derivada de la función f(x).
3. Calcular la nueva estimación de la raíz utilizando la fórmula: x1 = x0 - f(x0) / f'(x0), donde f'(x0) es la derivada de f(x) evaluada en x0.
4. Repetir el paso 3 hasta que se alcance una precisión deseada o se obtenga una estimación suficientemente cercana a la raíz.

Código de ejemplo:

def newton_method(f, f_prime, x0, epsilon=1e-6, max_iterations=100):
    """
    Implementación del método de Newton para encontrar una raíz de la función f(x).
    f: función original.
    f_prime: derivada de la función f(x).
    x0: punto inicial.
    epsilon: precisión deseada.
    max_iterations: número máximo de iteraciones permitidas.
    """
    x = x0
    iterations = 0

    while abs(f(x)) > epsilon and iterations < max_iterations:
        x = x - f(x) / f_prime(x)
        iterations += 1

    if abs(f(x)) <= epsilon:
        return x  # Se encontró una raíz dentro de la precisión deseada
    else:
        return None  # No se encontró una raíz en el número máximo de iteraciones permitidas

# Definición de la función y su derivada
def f(x):
    return x**2 - 4

def f_prime(x):
    return 2*x

# Uso del método de Newton para encontrar una raíz
root = newton_method(f, f_prime, x0=2)

if root is not None:
    print("La raíz encontrada es:", root)
else:
    print("No se encontró una raíz en el número máximo de iteraciones permitidas.")

