"""Módulo que implementa un árbol n-ario para el Sistema de Gestión Universitaria.
   Representa la jerarquía: Rectoría → Facultades → Departamentos → Programas → Asignaturas
"""

class NodoArbol:
    """Clase que representa un nodo del árbol n-ario"""
    
    def __init__(self, nombre, tipo, descripcion=""):
        """
        Inicializa un nodo del árbol
        
        Args:
            nombre (str): Nombre de la entidad (ej: "Facultad de Ingeniería")
            tipo (str): Tipo de entidad ("Rectoría", "Facultad", "Departamento", "Programa", "Asignatura")
            descripcion (str): Descripción adicional de la entidad
        """
        self.nombre = nombre
        self.tipo = tipo
        self.descripcion = descripcion
        self.hijos = []  # Lista de nodos hijos
        self.padre = None  # Referencia al nodo padre
    
    def agregar_hijo(self, hijo):
        """Agrega un nodo hijo a este nodo"""
        hijo.padre = self
        self.hijos.append(hijo)
    
    def eliminar_hijo(self, nombre_hijo):
        """Elimina un nodo hijo por su nombre"""
        self.hijos = [hijo for hijo in self.hijos if hijo.nombre != nombre_hijo]
    
    def __str__(self):
        """Representación en string del nodo"""
        return f"{self.tipo}: {self.nombre}"


class ArbolUniversitario:
    """Clase que representa el árbol jerárquico del sistema universitario"""
    
    # Definición de niveles jerárquicos permitidos
    NIVELES = {
        "Rectoría": 0,
        "Facultad": 1,
        "Departamento": 2,
        "Programa": 3,
        "Asignatura": 4
    }
    
    # Mapeo de relaciones padre-hijo permitidas
    RELACIONES_PERMITIDAS = {
        "Rectoría": "Facultad",
        "Facultad": "Departamento",
        "Departamento": "Programa",
        "Programa": "Asignatura"
    }
    
    def __init__(self, nombre_rectoria="Rectoría Central"):
        """Inicializa el árbol con el nodo raíz (Rectoría)"""
        self.raiz = NodoArbol(nombre_rectoria, "Rectoría", "Máxima autoridad universitaria")
    
    def insertar(self, nombre_padre, nombre_nuevo, tipo_nuevo, descripcion=""):
        """
        Inserta un nuevo nodo en el árbol bajo un nodo padre específico
        
        Args:
            nombre_padre (str): Nombre del nodo padre donde se insertará el nuevo nodo
            nombre_nuevo (str): Nombre del nuevo nodo a insertar
            tipo_nuevo (str): Tipo del nuevo nodo
            descripcion (str): Descripción del nuevo nodo
            
        Returns:
            bool: True si se insertó correctamente, False en caso contrario
        """
        # Buscar el nodo padre
        nodo_padre = self._buscar_nodo(self.raiz, nombre_padre)
        
        if nodo_padre is None:
            return False
        
        # Validar que la relación padre-hijo sea permitida
        tipo_hijo_esperado = self.RELACIONES_PERMITIDAS.get(nodo_padre.tipo)
        
        if tipo_hijo_esperado != tipo_nuevo:
            return False
        
        # Verificar que no exista un hijo con el mismo nombre
        for hijo in nodo_padre.hijos:
            if hijo.nombre == nombre_nuevo:
                return False
        
        # Crear y agregar el nuevo nodo
        nuevo_nodo = NodoArbol(nombre_nuevo, tipo_nuevo, descripcion)
        nodo_padre.agregar_hijo(nuevo_nodo)
        
        return True
    
    def buscar(self, nombre):
        """
        Busca un nodo por su nombre
        
        Args:
            nombre (str): Nombre del nodo a buscar
            
        Returns:
            NodoArbol: El nodo encontrado o None si no existe
        """
        return self._buscar_nodo(self.raiz, nombre)
    
    def _buscar_nodo(self, nodo_actual, nombre):
        """Método auxiliar recursivo para buscar un nodo por nombre (DFS)"""
        if nodo_actual is None:
            return None
        
        if nodo_actual.nombre == nombre:
            return nodo_actual
        
        # Buscar en los hijos
        for hijo in nodo_actual.hijos:
            resultado = self._buscar_nodo(hijo, nombre)
            if resultado is not None:
                return resultado
        
        return None
    
    def eliminar(self, nombre):
        """
        Elimina un nodo y todos sus descendientes
        
        Args:
            nombre (str): Nombre del nodo a eliminar
            
        Returns:
            bool: True si se eliminó correctamente, False en caso contrario
        """
        # No se puede eliminar la raíz
        if nombre == self.raiz.nombre:
            return False
        
        # Buscar el nodo a eliminar
        nodo = self._buscar_nodo(self.raiz, nombre)
        
        if nodo is None or nodo.padre is None:
            return False
        
        # Eliminar el nodo de la lista de hijos de su padre
        nodo.padre.eliminar_hijo(nombre)
        
        return True
    
    def listar_hijos(self, nombre_padre):
        """
        Lista todos los hijos directos de un nodo
        
        Args:
            nombre_padre (str): Nombre del nodo padre
            
        Returns:
            list: Lista de nodos hijos o lista vacía si no existe el padre
        """
        nodo = self._buscar_nodo(self.raiz, nombre_padre)
        
        if nodo is None:
            return []
        
        return nodo.hijos
    
    def obtener_ruta(self, nombre):
        """
        Obtiene la ruta completa desde la raíz hasta un nodo
        
        Args:
            nombre (str): Nombre del nodo destino
            
        Returns:
            list: Lista de nodos desde la raíz hasta el nodo destino
        """
        nodo = self._buscar_nodo(self.raiz, nombre)
        
        if nodo is None:
            return []
        
        ruta = []
        nodo_actual = nodo
        
        # Recorrer hacia arriba hasta la raíz
        while nodo_actual is not None:
            ruta.insert(0, nodo_actual)
            nodo_actual = nodo_actual.padre
        
        return ruta
    
    def recorrido_por_niveles(self):
        """
        Realiza un recorrido por niveles (BFS) del árbol
        
        Returns:
            list: Lista de listas, donde cada sublista contiene los nodos de un nivel
        """
        if self.raiz is None:
            return []
        
        resultado = []
        cola = [self.raiz]
        
        while cola:
            nivel_actual = []
            siguiente_nivel = []
            
            for nodo in cola:
                nivel_actual.append(nodo)
                siguiente_nivel.extend(nodo.hijos)
            
            resultado.append(nivel_actual)
            cola = siguiente_nivel
        
        return resultado
    
    def recorrido_profundidad(self, nodo=None, resultado=None):
        """
        Realiza un recorrido en profundidad (DFS) del árbol
        
        Args:
            nodo (NodoArbol): Nodo desde donde iniciar (por defecto la raíz)
            resultado (list): Lista acumulativa de nodos visitados
            
        Returns:
            list: Lista de nodos en orden de recorrido DFS
        """
        if resultado is None:
            resultado = []
        
        if nodo is None:
            nodo = self.raiz
        
        resultado.append(nodo)
        
        for hijo in nodo.hijos:
            self.recorrido_profundidad(hijo, resultado)
        
        return resultado
    
    def obtener_estadisticas(self):
        """
        Obtiene estadísticas del árbol
        
        Returns:
            dict: Diccionario con contadores por tipo de entidad
        """
        estadisticas = {
            "Rectoría": 0,
            "Facultad": 0,
            "Departamento": 0,
            "Programa": 0,
            "Asignatura": 0
        }
        
        nodos = self.recorrido_profundidad()
        
        for nodo in nodos:
            if nodo.tipo in estadisticas:
                estadisticas[nodo.tipo] += 1
        
        return estadisticas
