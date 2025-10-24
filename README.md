# Análisis de Estructuras de Datos — Árboles vs Grafos

## Descripción
Ejercicio para practicar la selección y diseño de estructuras de datos (árboles vs grafos) a partir de problemas del mundo real. Incluye análisis de 5 casos, selección de casos para implementar y diseño conceptual.

## Objetivo de aprendizaje
Desarrollar la capacidad de analizar problemas y determinar la estructura de datos más apropiada (árbol o grafo) según las características y relaciones del dominio.

## Estructura del ejercicio
- Fase 1: Contextualización Teórica (20 min)  
- Fase 2: Análisis de Problemas Contextualizados (40 min)  
- Fase 3: Selección para Implementación  
- Fase 4: Diseño Conceptual (25 min)  
- Reflexión Final

---

## Fase 1 — Características clave para la decisión
### Árbol
- Relaciones jerárquicas y parentales  
- Un solo nodo raíz  
- Sin ciclos  
- Direccionalidad padre → hijo  
- Camino único entre pares de nodos

### Grafo
- Relaciones complejas y multidireccionales  
- Múltiples conexiones posibles  
- Pueden contener ciclos  
- Conexiones peer-to-peer  
- Múltiples caminos entre nodos

---

## Fase 2 — Problemas y preguntas de análisis

### Problema 1 — Sistema de Gestión Universitaria
Contexto: Rectoría → Facultades → Departamentos → Programas → Asignaturas. Asignaturas pueden tener prerrequisitos.
Preguntas:
- ¿Relaciones jerárquicas o reticulares?  
- ¿Existe un punto de origen único?  
- ¿Hay ciclos posibles?  
- ¿La información fluye en una sola dirección?  
Decisión: - [ ] Árbol  - [ ] Grafo  
Justificación técnica:

---

### Problema 2 — Plataforma de Recomendaciones de Contenido
Contexto: Usuarios siguen a otros, crean listas, califican; recomendaciones basadas en usuarios similares, contenido relacionado y tendencias.
Preguntas:
- ¿Conexiones simétricas o asimétricas?  
- ¿Es posible formar ciclos de recomendación?  
- ¿Se parece a una jerarquía o a una red?  
- ¿Se necesitan múltiples tipos de relaciones?  
Decisión: - [ ] Árbol  - [ ] Grafo  
Justificación técnica:

---

### Problema 3 — Sistema de Gestión de Proyectos de Software
Contexto: Módulos con dependencias entre sí; pueden existir dependencias circulares; identificar paquetes independientes para paralelizar trabajo.
Preguntas:
- ¿Las dependencias son jerárquicas?  
- ¿Es crítico detectar dependencias circulares?  
- ¿La relación es "contiene" o "depende de"?  
- ¿Se necesita detectar componentes inconexos?  
Decisión: - [ ] Árbol  - [ ] Grafo  
Justificación técnica:

---

### Problema 4 — Sistema de Tomografía Computarizada
Contexto: Vóxeles 3D con vecindad en seis direcciones; identificar regiones conectadas de tejido similar.
Preguntas:
- ¿Conexiones uniformes en todas direcciones?  
- ¿Existe un punto central único?  
- ¿Relaciones de adyacencia espacial o jerarquía?  
- ¿Se necesitan encontrar caminos entre puntos arbitrarios?  
Decisión: - [ ] Árbol  - [ ] Grafo  
Justificación técnica:

---

### Problema 5 — Sistema de Comercio Electrónico con Inventario
Contexto: Bodegas con categorías, subcategorías y productos; productos pueden pertenecer a múltiples categorías; transferencias entre bodegas.
Preguntas:
- ¿La organización es estrictamente jerárquica?  
- ¿Existen relaciones cruzadas entre categorías?  
- ¿Las transferencias crean conexiones complejas?  
- ¿La estructura es de contención o interconexión?  
Decisión: - [ ] Árbol  - [ ] Grafo  
Justificación técnica:

---

## Fase 3 — Selección para implementación
Selecciona DOS problemas:
- Uno para implementar con Árbol  
- Uno para implementar con Grafo

Mi selección:
- Problema para implementar con Árbol: _______  
    - Razones principales:
- Problema para implementar con Grafo: _______  
    - Razones principales:

---

## Fase 4 — Diseño conceptual

### Para el problema seleccionado con Árbol
- Nodo raíz:  
- Relaciones padre-hijo:  
- Tipo de árbol (binario, n-ario, etc.):  
- Operaciones principales (insertar, buscar, recorrido, eliminar, etc.):

### Para el problema seleccionado con Grafo
- Tipos de nodos:  
- Tipos de aristas / conexiones:  
- ¿Dirigido o no dirigido?:  
- ¿Con peso en las aristas?:  
- Operaciones principales (búsqueda, detección de ciclos, caminos más cortos, componentes conectados, etc.):

---

## Reflexión final
- ¿Qué patrones te ayudaron a distinguir entre árboles y grafos?  
- ¿En qué problemas fue más difícil decidir y por qué?

---

Tiempo estimado total: ~1.5 horas