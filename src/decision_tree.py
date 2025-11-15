"""
Módulo del árbol de decisión simple.

Implementa un árbol de decisión con un solo nodo que clasifica
números en 'Alto' o 'Bajo' según un umbral.
"""


class ArbolDecision:
    """
    Árbol de decisión simple con un solo nodo de decisión.

    Este árbol clasifica números en dos categorías ('Alto' o 'Bajo')
    basándose en un umbral numérico.

    Attributes:
        umbral (int): Valor umbral para la clasificación.
    """

    def __init__(self, umbral=50):
        """
        Inicializa el árbol de decisión con un umbral.

        Args:
            umbral (int): Valor umbral para clasificar (por defecto 50).
        """
        self.umbral = umbral

    def clasificar(self, numero):
        """
        Clasifica un número como 'Alto' o 'Bajo'.

        Args:
            numero (int/float): Número a clasificar.

        Returns:
            str: 'Alto' si el número es mayor o igual al umbral,
                 'Bajo' si es menor.
        """
        if numero >= self.umbral:
            return "Alto"
        else:
            return "Bajo"

    def clasificar_conjunto(self, numeros):
        """
        Clasifica un conjunto de números.

        Args:
            numeros (list): Lista de números a clasificar.

        Returns:
            list: Lista de tuplas (numero, clasificacion).
        """
        resultados = []
        for numero in numeros:
            clasificacion = self.clasificar(numero)
            resultados.append((numero, clasificacion))
        return resultados


def contar_clasificaciones(resultados):
    """
    Cuenta cuántos elementos hay de cada clasificación.

    Args:
        resultados (list): Lista de tuplas (numero, clasificacion).

    Returns:
        dict: Diccionario con conteos {'Alto': n, 'Bajo': m}.
    """
    conteo = {"Alto": 0, "Bajo": 0}
    
    for _, clasificacion in resultados:
        conteo[clasificacion] += 1
    
    return conteo


def mostrar_ejemplos(resultados, cantidad=10):
    """
    Muestra ejemplos de clasificaciones.

    Args:
        resultados (list): Lista de tuplas (numero, clasificacion).
        cantidad (int): Cantidad de ejemplos a mostrar (por defecto 10).
    """
    print(f"\n{'='*50}")
    print(f"PRIMEROS {cantidad} RESULTADOS DE CLASIFICACIÓN")
    print(f"{'='*50}")
    
    for i, (numero, clasificacion) in enumerate(resultados[:cantidad]):
        print(f"{numero} → {clasificacion}")
    
    print(f"{'='*50}\n")