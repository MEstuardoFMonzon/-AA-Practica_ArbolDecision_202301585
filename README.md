# PRÁCTICA 3: Árbol de Decisión

**Universidad Da Vinci de Guatemala**  
**Facultad de Ingeniería Industria y Tecnología**  
**Análisis de Algoritmos**  
**Ing. César Sazo**

---

## 📋 Información del Estudiante

- **Nombre:** Juan Carlos Pérez
- **Carné:** 202301585
- **Fecha:** 15/11/2025

---

## 🎯 Objetivo General

Construir y ejecutar un árbol de decisión simple en Python (sin librerías externas) para clasificar números como "Alto" o "Bajo" a partir de un umbral, aplicando de forma rigurosa el flujo de trabajo Gitflow.

---

## 🎯 Objetivos Específicos

1. Implementar un árbol de decisión minimalista con 1 solo nodo de decisión (umbral) y 2 hojas ("Bajo" / "Alto")
2. Leer un archivo TXT con 1000 números y clasificarlos
3. Generar salidas claras en consola
4. Aplicar Gitflow con ramas feature/_, hotfix/_, commits significativos, PRs y merge hacia develop y main
5. Documentar con docstrings (PEP-257) y README.md claro

---

## 📖 Descripción del Árbol de Decisión

Este proyecto implementa un **árbol de decisión simple** con las siguientes características:

### Estructura del Árbol

- **1 nodo de decisión:** Evalúa si un número es mayor o igual al umbral
- **2 hojas (resultados):**
  - `"Alto"`: cuando `número >= UMBRAL`
  - `"Bajo"`: cuando `número < UMBRAL`

### Parámetros

- **Umbral por defecto:** 50
- **Configurable:** Se puede cambiar mediante argumento `--umbral`

### Diagrama del Árbol

```
            [número >= 50?]
               /        \
             SI          NO
             /            \
        "Alto"          "Bajo"
```

---

## 🛠️ Metodología

### Estructura del Proyecto

```
practica_arbol_decision/
├── README.md
├── main.py
├── src/
│   ├── __init__.py
│   ├── data_loader.py      # Leer/generar TXT
│   └── decision_tree.py    # Lógica del árbol (umbral)
├── data/
│   └── numeros_1000.txt    # Se genera si no existe
└── docs/
    └── evidencias/         # Capturas de Git y ejecución
```

### Flujo del Programa

1. **Verificación de datos:** Verifica si existe `data/numeros_1000.txt`

   - Si no existe, lo genera con 1000 números aleatorios (1-100)
   - Muestra la semilla utilizada para reproducibilidad

2. **Carga de datos:** Lee los 1000 números del archivo

3. **Clasificación:** Aplica el árbol de decisión

   - Compara cada número con el umbral
   - Asigna clasificación "Alto" o "Bajo"

4. **Resultados:** Imprime en consola
   - Primeros 10 ejemplos de clasificación
   - Conteo total de "Alto" y "Bajo"
   - Porcentajes
   - Tiempo de ejecución

### Flujo Gitflow Aplicado

#### Ramas Creadas

1. **`main`:** Rama de producción
2. **`develop`:** Rama de desarrollo
3. **`feature/implementacion_arbol`:** Implementación del código
4. **`hotfix/cambio_nombre`:** Corrección en README

#### Commits Realizados

1. `[feature] Generación de numeros_1000.txt`
2. `[feature] Implementación árbol (umbral) y clasificación`
3. `[feature] Programa principal con flujo completo`
4. `[feature] Datos generados y evidencias de ejecución`

#### Pull Requests

1. **PR #1:** `feature/implementacion_arbol` → `develop`
2. **PR #2:** `develop` → `main` (con tag v1.0.0)

---

## 📊 Resultados

### Ejemplo de Ejecución

```
============================================================
ÁRBOL DE DECISIÓN - CLASIFICACIÓN DE NÚMEROS
============================================================

Umbral de clasificación: 50
  • Números >= 50 → Alto
  • Números < 50 → Bajo

PASO 1: Verificación de datos
------------------------------------------------------------
✓ Archivo generado: data/numeros_1000.txt
✓ Semilla utilizada: 995063

PASO 2: Carga de datos
------------------------------------------------------------
✓ Se cargaron 1000 números desde data/numeros_1000.txt

PASO 3: Clasificación con árbol de decisión
------------------------------------------------------------
✓ Se clasificaron 1000 números

PASO 4: Resultados
------------------------------------------------------------

==================================================
PRIMEROS 10 RESULTADOS DE CLASIFICACIÓN
==================================================
11 → Bajo
41 → Bajo
61 → Alto
31 → Bajo
40 → Bajo
47 → Bajo
26 → Bajo
99 → Alto
56 → Alto
80 → Alto
==================================================

RESUMEN DE CLASIFICACIÓN
============================================================
  Alto  :  470 números (47.0%)
  Bajo  :  530 números (53.0%)
  TOTAL : 1000 números
============================================================

⏱ Tiempo total de ejecución: 0.048517 segundos
```

### Estadísticas

- **Total de números:** 1000
- **Clasificados como "Alto":** ~470-530 (varía según semilla)
- **Clasificados como "Bajo":** ~470-530 (varía según semilla)
- **Tiempo de ejecución:** ~0.05 segundos

---

## 📸 Evidencias

Las evidencias del proyecto se encuentran en `docs/evidencias/`:

1. **`branches.png`** - Captura de `git branch -a`
2. **`git_log.png`** - Captura de `git log --oneline --decorate --graph`
3. **`pr_feature_develop.png`** - Pull Request de feature a develop
4. **`pr_develop_main.png`** - Pull Request de develop a main
5. **`ejecucion.png`** - Ejecución del programa en consola

---

## 🚀 Uso del Programa

### Ejecución básica

```bash
python main.py
```

### Con umbral personalizado

```bash
python main.py --umbral 75
```

---

## 📚 Documentación del Código

Todo el código incluye **docstrings** siguiendo el estándar **PEP-257**:

- `src/data_loader.py`: Funciones para generar y cargar datos
- `src/decision_tree.py`: Clase ArbolDecision y funciones auxiliares
- `main.py`: Función principal con flujo completo

---

## 🎓 Conclusiones

### Aprendizajes sobre Gitflow

1. **Organización del trabajo:** Gitflow permite separar el desarrollo (develop) de la producción (main)
2. **Ramas feature:** Facilitan el desarrollo de funcionalidades de forma aislada
3. **Ramas hotfix:** Permiten correcciones rápidas sin interrumpir el desarrollo
4. **Pull Requests:** Mejoran la revisión de código antes de integrar cambios
5. **Versionado semántico:** El tag v1.0.0 marca claramente la primera versión estable

### Aprendizajes sobre el Árbol de Decisión Simple

1. **Simplicidad efectiva:** Un árbol con un solo nodo puede ser suficiente para clasificaciones binarias básicas
2. **Rendimiento:** La clasificación de 1000 números es extremadamente rápida (~0.05s)
3. **Escalabilidad del concepto:** Este árbol simple sienta las bases para árboles más complejos
4. **Importancia del umbral:** La elección del umbral (50) determina completamente los resultados
5. **Código limpio:** La separación en módulos facilita el mantenimiento y testing

---

## 👥 Colaboradores

- **cesarsazo** - Instructor del curso

---

## 📄 Licencia

Proyecto académico - Universidad Da Vinci de Guatemala © 2024
