"""
Módulo para cargar y generar datos de números.

Este módulo contiene funciones para verificar la existencia del archivo
de números, generarlo si no existe, y cargarlo en memoria.
"""

import os
import random
from pathlib import Path


def verificar_archivo(ruta_archivo):
    """
    Verifica si existe el archivo en la ruta especificada.

    Args:
        ruta_archivo (str): Ruta del archivo a verificar.

    Returns:
        bool: True si el archivo existe, False en caso contrario.
    """
    return os.path.exists(ruta_archivo)


def generar_numeros(ruta_archivo, cantidad=1000, rango_min=1, rango_max=100):
    """
    Genera un archivo con números aleatorios.

    Crea un archivo de texto con la cantidad especificada de números
    aleatorios dentro del rango dado. Muestra la semilla utilizada.

    Args:
        ruta_archivo (str): Ruta donde se guardará el archivo.
        cantidad (int): Cantidad de números a generar (por defecto 1000).
        rango_min (int): Valor mínimo del rango (por defecto 1).
        rango_max (int): Valor máximo del rango (por defecto 100).

    Returns:
        int: La semilla utilizada para la generación.
    """
    # Crear directorio si no existe
    Path(ruta_archivo).parent.mkdir(parents=True, exist_ok=True)
    
    # Generar semilla aleatoria
    semilla = random.randint(1, 1000000)
    random.seed(semilla)
    
    # Generar números y escribir en archivo
    with open(ruta_archivo, 'w') as archivo:
        for _ in range(cantidad):
            numero = random.randint(rango_min, rango_max)
            archivo.write(f"{numero}\n")
    
    print(f"✓ Archivo generado: {ruta_archivo}")
    print(f"✓ Semilla utilizada: {semilla}")
    
    return semilla


def cargar_numeros(ruta_archivo):
    """
    Carga los números desde un archivo de texto.

    Lee un archivo de texto donde cada línea contiene un número
    y retorna una lista con todos los números.

    Args:
        ruta_archivo (str): Ruta del archivo a leer.

    Returns:
        list: Lista de enteros leídos del archivo.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si hay líneas que no pueden convertirse a entero.
    """
    numeros = []
    
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:  # Ignorar líneas vacías
                numeros.append(int(linea))
    
    print(f"✓ Se cargaron {len(numeros)} números desde {ruta_archivo}")
    
    return numeros