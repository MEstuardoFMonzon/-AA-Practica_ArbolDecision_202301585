"""
Programa principal para la clasificación de números con árbol de decisión.

Este script implementa un árbol de decisión simple que clasifica
1000 números en 'Alto' o 'Bajo' según un umbral definido.
"""

import time
import argparse
from src.data_loader import verificar_archivo, generar_numeros, cargar_numeros
from src.decision_tree import ArbolDecision, contar_clasificaciones, mostrar_ejemplos


# Constantes
RUTA_ARCHIVO = "data/numeros_1000.txt"
UMBRAL_DEFAULT = 50
CANTIDAD_NUMEROS = 1000
RANGO_MIN = 1
RANGO_MAX = 100


def main():
    """
    Función principal del programa.

    Ejecuta el flujo completo: verificar/generar datos, clasificar
    números con el árbol de decisión, y mostrar resultados.
    """
    # Iniciar cronómetro
    tiempo_inicio = time.time()
    
    print("\n" + "="*60)
    print("ÁRBOL DE DECISIÓN - CLASIFICACIÓN DE NÚMEROS")
    print("="*60 + "\n")
    
    # Parsear argumentos (opcional)
    parser = argparse.ArgumentParser(description='Clasificador de números con árbol de decisión')
    parser.add_argument('--umbral', type=int, default=UMBRAL_DEFAULT,
                       help=f'Umbral para clasificación (default: {UMBRAL_DEFAULT})')
    args = parser.parse_args()
    
    umbral = args.umbral
    print(f"Umbral de clasificación: {umbral}")
    print(f"  • Números >= {umbral} → Alto")
    print(f"  • Números < {umbral} → Bajo\n")
    
    # Paso 1: Verificar/crear archivo de datos
    print("PASO 1: Verificación de datos")
    print("-" * 60)
    
    if not verificar_archivo(RUTA_ARCHIVO):
        print(f"✗ Archivo no encontrado: {RUTA_ARCHIVO}")
        print(f"→ Generando {CANTIDAD_NUMEROS} números aleatorios...\n")
        generar_numeros(RUTA_ARCHIVO, CANTIDAD_NUMEROS, RANGO_MIN, RANGO_MAX)
    else:
        print(f"✓ Archivo encontrado: {RUTA_ARCHIVO}")
    
    # Paso 2: Cargar números
    print("\nPASO 2: Carga de datos")
    print("-" * 60)
    numeros = cargar_numeros(RUTA_ARCHIVO)
    
    # Paso 3: Clasificar con el árbol de decisión
    print("\nPASO 3: Clasificación con árbol de decisión")
    print("-" * 60)
    
    arbol = ArbolDecision(umbral=umbral)
    resultados = arbol.clasificar_conjunto(numeros)
    
    print(f"✓ Se clasificaron {len(resultados)} números")
    
    # Paso 4: Mostrar resultados
    print("\nPASO 4: Resultados")
    print("-" * 60)
    
    # Mostrar primeros 10 ejemplos
    mostrar_ejemplos(resultados, cantidad=10)
    
# Mostrar conteos
    conteo = contar_clasificaciones(resultados)
    
    print("RESUMEN DE CLASIFICACIÓN")
    print("=" * 60)
    print(f"  Alto  : {conteo['Alto']:4d} números ({conteo['Alto']/len(resultados)*100:.1f}%)")
    print(f"  Bajo  : {conteo['Bajo']:4d} números ({conteo['Bajo']/len(resultados)*100:.1f}%)")
    print(f"  TOTAL : {len(resultados):4d} números")
    print("=" * 60)
    
    # Detener cronómetro
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    
    print(f"\n⏱  Tiempo total de ejecución: {tiempo_total:.6f} segundos")
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()