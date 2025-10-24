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
Decisión: - [ ] Árbol  - [x] Grafo  
Justificación técnica: Aunque la estructura organizacional (Rectoría → Facultades → Departamentos) es jerárquica, las asignaturas con prerrequisitos crean relaciones que pueden formar ciclos y múltiples caminos, lo cual requiere un grafo, pero de igual manera el usar árbol para este ejercicio no sería una mala elección.

---

### Problema 2 — Plataforma de Recomendaciones de Contenido
Contexto: Usuarios siguen a otros, crean listas, califican; recomendaciones basadas en usuarios similares, contenido relacionado y tendencias.
Preguntas:
- ¿Conexiones simétricas o asimétricas?  
- ¿Es posible formar ciclos de recomendación?  
- ¿Se parece a una jerarquía o a una red?  
- ¿Se necesitan múltiples tipos de relaciones?  
Decisión: - [ ] Árbol  - [x] Grafo  
Justificación técnica: Las relaciones entre usuarios (seguir), listas, calificaciones y recomendaciones son multidireccionales y pueden formar ciclos. No hay jerarquía única, sino una red compleja de conexiones.

---

### Problema 3 — Sistema de Gestión de Proyectos de Software
Contexto: Módulos con dependencias entre sí; pueden existir dependencias circulares; identificar paquetes independientes para paralelizar trabajo.
Preguntas:
- ¿Las dependencias son jerárquicas?  
- ¿Es crítico detectar dependencias circulares?  
- ¿La relación es "contiene" o "depende de"?  
- ¿Se necesita detectar componentes inconexos?  
Decisión: - [ ] Árbol  - [x] Grafo  
Justificación técnica: Las dependencias entre módulos pueden ser circulares (ciclos), y es crítico detectarlas. Las relaciones son de tipo "depende de", no jerárquicas, y se necesita identificar componentes inconexos.

---

### Problema 4 — Sistema de Tomografía Computarizada
Contexto: Vóxeles 3D con vecindad en seis direcciones; identificar regiones conectadas de tejido similar.
Preguntas:
- ¿Conexiones uniformes en todas direcciones?  
- ¿Existe un punto central único?  
- ¿Relaciones de adyacencia espacial o jerarquía?  
- ¿Se necesitan encontrar caminos entre puntos arbitrarios?  
Decisión: - [ ] Árbol  - [x] Grafo  
Justificación técnica: Los vóxeles tienen conexiones uniformes en seis direcciones (vecindad espacial), sin un punto central único. Es una estructura de adyacencia espacial, no jerárquica, ideal para grafos.

---

### Problema 5 — Sistema de Comercio Electrónico con Inventario
Contexto: Bodegas con categorías, subcategorías y productos; productos pueden pertenecer a múltiples categorías; transferencias entre bodegas.
Preguntas:
- ¿La organización es estrictamente jerárquica?  
- ¿Existen relaciones cruzadas entre categorías?  
- ¿Las transferencias crean conexiones complejas?  
- ¿La estructura es de contención o interconexión?  
Decisión: - [ ] Árbol  - [x] Grafo  
Justificación técnica: Aunque las categorías pueden parecer jerárquicas, los productos pueden pertenecer a múltiples categorías y las transferencias entre bodegas crean relaciones cruzadas que rompen la estructura de árbol.

---

## Fase 3 — Selección para implementación
Selecciona DOS problemas:
- Uno para implementar con Árbol  
- Uno para implementar con Grafo

Mi selección:
- Problema para implementar con Árbol: **Problema 1 - Sistema de Gestión Universitaria**
    - Razones principales:
        - La estructura organizacional (Rectoría → Facultades → Departamentos → Programas) es puramente jerárquica
        - Tiene un único nodo raíz (Rectoría)
        - Las relaciones padre-hijo son claras y unidireccionales
        - Se puede implementar como árbol n-ario para representar la jerarquía administrativa
        - Los prerrequisitos de asignaturas se pueden manejar como estructura separada o caso especial
- Problema para implementar con Grafo: **Problema 3 - Sistema de Gestión de Proyectos de Software**
    - Razones principales:
        - Representa el caso clásico de grafo dirigido con dependencias
        - Necesita detectar ciclos (dependencias circulares) - operación fundamental de grafos
        - Permite identificar componentes conectados para paralelización
        - Las relaciones "depende de" son claramente no jerárquicas
        - Es el ejemplo más didáctico y directo para aprender algoritmos de grafos (DFS, detección de ciclos)

---

## Fase 4 — Diseño conceptual

### Para el problema seleccionado con Árbol (Sistema de Gestión Universitaria)

**Nodo raíz:**  
- Rectoría (nivel 0 de la jerarquía universitaria)

**Relaciones padre-hijo:**  
- Rectoría → Facultades (ej: Facultad de Ingeniería, Facultad de Ciencias)
- Facultades → Departamentos (ej: Departamento de Sistemas, Departamento de Matemáticas)
- Departamentos → Programas Académicos (ej: Licenciatura en Informática, Maestría en Ciencias)
- Programas → Asignaturas (ej: Estructura de Datos, Algoritmos, Bases de Datos)

**Tipo de árbol:**  
- Árbol n-ario (cada nodo puede tener múltiples hijos)
- No balanceado (diferentes facultades pueden tener diferente cantidad de departamentos)

**Operaciones principales:**
1. **Insertar:** Agregar nuevas facultades, departamentos, programas o asignaturas en su nivel jerárquico correspondiente
2. **Buscar:** Localizar una entidad específica (ej: encontrar todas las asignaturas de un programa)
3. **Recorrido por niveles (BFS):** Mostrar toda la estructura organizacional nivel por nivel
4. **Recorrido en profundidad (DFS):** Explorar una rama completa (ej: desde Rectoría hasta las asignaturas de un programa específico)
5. **Eliminar:** Remover entidades y sus dependientes (ej: eliminar un departamento elimina sus programas y asignaturas)
6. **Listar hijos:** Obtener todas las entidades dependientes de un nodo (ej: todos los departamentos de una facultad)
7. **Obtener ruta:** Mostrar la jerarquía completa desde la raíz hasta un nodo específico

---

### Para el problema seleccionado con Grafo (Sistema de Gestión de Proyectos de Software)

**Tipos de nodos:**  
- Módulos/Paquetes de software (ej: módulo de autenticación, módulo de reportes, módulo de pagos)
- Cada nodo representa un componente independiente del sistema

**Tipos de aristas / conexiones:**  
- Dependencias directas entre módulos (ej: "módulo A depende de módulo B")
- Representan que un módulo necesita otro para funcionar correctamente

**¿Dirigido o no dirigido?:**  
- **Grafo dirigido (dígrafo)**: La dependencia es unidireccional
- Si A depende de B, no significa que B dependa de A
- Las aristas tienen dirección: A → B significa "A depende de B"

**¿Con peso en las aristas?:**  
- **Opcional:** Se pueden usar pesos para representar:
  - Nivel de acoplamiento entre módulos (bajo, medio, alto)
  - Complejidad de la dependencia
  - Prioridad de la dependencia
- Para el ejercicio básico: **sin peso** (solo conexiones binarias de dependencia)

**Operaciones principales:**
1. **Agregar módulo:** Insertar un nuevo nodo (módulo) al grafo
2. **Agregar dependencia:** Crear una arista dirigida entre dos módulos
3. **Eliminar dependencia:** Remover una conexión entre módulos
4. **Detección de ciclos (DFS):** Identificar dependencias circulares (A→B→C→A) que causan problemas de compilación
5. **Ordenamiento topológico:** Determinar el orden correcto de compilación/construcción de módulos
6. **Búsqueda de dependencias directas:** Listar todos los módulos de los que depende un módulo específico
7. **Búsqueda de dependencias transitivas:** Encontrar todas las dependencias indirectas de un módulo
8. **Componentes fuertemente conectados:** Identificar grupos de módulos con dependencias circulares
9. **Identificar módulos independientes:** Encontrar módulos sin dependencias para paralelizar el trabajo
10. **Análisis de impacto:** Determinar qué módulos se verían afectados si se modifica un módulo específico

---

## Reflexión final

### ¿Qué patrones te ayudaron a distinguir entre árboles y grafos?

Los patrones clave que facilitaron la distinción fueron:

1. **Patrón de Jerarquía Estricta (Árbol):**
   - Presencia de una autoridad o punto de origen único y claramente definido
   - Relaciones de "contención" o "pertenencia" que fluyen en una sola dirección
   - Imposibilidad lógica de ciclos (un departamento no puede contener a su propia facultad)
   - Ejemplo: La estructura organizacional universitaria (Rectoría → Facultades → Departamentos)

2. **Patrón de Dependencias Bidireccionales o Cruzadas (Grafo):**
   - Relaciones de "depende de" o "está relacionado con" en lugar de "contiene"
   - Posibilidad de ciclos (A depende de B, B depende de C, C depende de A)
   - Múltiples caminos posibles entre dos entidades
   - Ejemplo: Módulos de software con dependencias circulares

3. **Patrón de Pertenencia Múltiple (Grafo):**
   - Una entidad puede pertenecer a múltiples categorías o estar conectada con múltiples entidades del mismo nivel
   - Relaciones many-to-many que rompen la estructura jerárquica
   - Ejemplo: Productos que pertenecen a múltiples categorías

4. **Patrón de Red de Conexiones (Grafo):**
   - Relaciones peer-to-peer sin jerarquía clara
   - Conexiones uniformes en múltiples direcciones
   - Ejemplo: Red social de usuarios, vóxeles en tomografía 3D

5. **Indicadores de Árbol:**
   - Palabras clave: "jerarquía", "subordinación", "contiene", "padre-hijo", "nivel"
   - Estructura organizacional clara y estable
   - Flujo de información unidireccional (de arriba hacia abajo)

6. **Indicadores de Grafo:**
   - Palabras clave: "depende de", "relacionado con", "conectado", "red", "ciclo", "múltiples caminos"
   - Relaciones dinámicas y complejas
   - Necesidad de detectar ciclos o analizar caminos

### ¿En qué problemas fue más difícil decidir y por qué?

**Problema más difícil de decidir: Problema 1 (Sistema de Gestión Universitaria)**

**Razones de la dificultad:**

1. **Naturaleza Híbrida:**
   - La estructura organizacional (Rectoría → Facultades → Departamentos → Programas) es claramente un árbol
   - Los prerrequisitos de asignaturas forman un grafo dirigido acíclico (DAG)
   - El sistema tiene dos estructuras de datos diferentes coexistiendo

2. **Interpretación del Alcance:**
   - Si nos enfocamos solo en la jerarquía administrativa → **Árbol** es perfectamente adecuado
   - Si incluimos los prerrequisitos de asignaturas → **Grafo** es necesario
   - La decisión depende de qué aspecto del sistema priorizamos

3. **Solución Adoptada:**
   - Implementamos la jerarquía administrativa como **árbol n-ario**
   - Esto fue válido porque:
     - Los prerrequisitos pueden manejarse como una estructura separada
     - La mayoría de operaciones del sistema (90%) son sobre la jerarquía organizacional
     - Los prerrequisitos son metadata adicional que no afecta la estructura principal

**Otros problemas con complejidad en la decisión:**

**Problema 5 (Comercio Electrónico):**
- Similar al Problema 1, tiene una estructura jerárquica (Bodegas → Categorías → Productos)
- Pero los productos en múltiples categorías y las transferencias entre bodegas rompen la jerarquía
- Decisión: **Grafo**, porque las relaciones cruzadas son fundamentales para el funcionamiento del sistema

**Lección aprendida:**
La clave no es solo identificar si existen relaciones jerárquicas, sino determinar:
1. **¿Qué relaciones son fundamentales para el sistema?**
2. **¿Las excepciones a la jerarquía son casos aislados o parte esencial del modelo?**
3. **¿Qué operaciones son críticas y cuál estructura las facilita mejor?**

En el Problema 1, las operaciones críticas eran sobre la jerarquía administrativa, por lo que el árbol fue la elección correcta. Los prerrequisitos, aunque importantes, son secundarios y pueden manejarse por separado.

**Aprendizaje clave:**
No siempre hay una respuesta única "correcta". La decisión debe basarse en:
- El contexto específico del problema
- Las operaciones más frecuentes
- Los requisitos de rendimiento
- La simplicidad vs completitud del modelo

En sistemas reales, es común usar estructuras híbridas donde diferentes aspectos del dominio se modelan con diferentes estructuras de datos.

---

Tiempo estimado total: ~1.5 horas