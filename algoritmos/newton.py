# Método de Newton

def newton_method(x0, f, f_prime, tolerance, max_iterations):
    """
    Implementación del Método de Newton para encontrar una raíz de una ecuación no lineal.
    
    Parámetros:
        - x0: Punto inicial de la iteración.
        - f: Función que representa la ecuación no lineal.
        - f_prime: Función que representa la derivada de la ecuación no lineal.
        - tolerance: Tolerancia para determinar la convergencia.
        - max_iterations: Número máximo de iteraciones permitidas.
    
    Retorna:
        - root: Raíz encontrada por el método de Newton.
    """
    iteration = 0
    x = x0
    
    while abs(f(x)) > tolerance and iteration < max_iterations:
        x = x - f(x) / f_prime(x)
        iteration += 1
    
    return x
