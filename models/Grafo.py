"""Módulo que implementa un grafo dirigido para el Sistema de Gestión de Proyectos de Software.
   Representa módulos/paquetes y sus dependencias.
"""

class Modulo:
    """Clase que representa un módulo de software"""
    
    def __init__(self, nombre, descripcion=""):
        """
        Inicializa un módulo
        
        Args:
            nombre (str): Nombre del módulo
            descripcion (str): Descripción del módulo
        """
        self.nombre = nombre
        self.descripcion = descripcion
    
    def __str__(self):
        return f"Módulo: {self.nombre}"
    
    def __eq__(self, other):
        if isinstance(other, Modulo):
            return self.nombre == other.nombre
        return False
    
    def __hash__(self):
        return hash(self.nombre)


class GrafoDependencias:
    """Clase que representa un grafo dirigido de dependencias entre módulos"""
    
    def __init__(self):
        """Inicializa el grafo vacío"""
        # Diccionario que mapea nombre de módulo -> objeto Modulo
        self.modulos = {}
        # Lista de adyacencia: modulo -> lista de módulos de los que depende
        self.dependencias = {}
    
    def agregar_modulo(self, nombre, descripcion=""):
        """
        Agrega un nuevo módulo al grafo
        
        Args:
            nombre (str): Nombre del módulo
            descripcion (str): Descripción del módulo
            
        Returns:
            bool: True si se agregó correctamente, False si ya existía
        """
        if nombre in self.modulos:
            return False
        
        modulo = Modulo(nombre, descripcion)
        self.modulos[nombre] = modulo
        self.dependencias[nombre] = []
        
        return True
    
    def agregar_dependencia(self, modulo_origen, modulo_destino):
        """
        Agrega una dependencia dirigida: modulo_origen depende de modulo_destino
        
        Args:
            modulo_origen (str): Nombre del módulo que depende
            modulo_destino (str): Nombre del módulo del que depende
            
        Returns:
            bool: True si se agregó correctamente, False en caso contrario
        """
        # Verificar que ambos módulos existan
        if modulo_origen not in self.modulos or modulo_destino not in self.modulos:
            return False
        
        # Evitar dependencias duplicadas
        if modulo_destino in self.dependencias[modulo_origen]:
            return False
        
        # Evitar auto-dependencias
        if modulo_origen == modulo_destino:
            return False
        
        self.dependencias[modulo_origen].append(modulo_destino)
        
        return True
    
    def eliminar_dependencia(self, modulo_origen, modulo_destino):
        """
        Elimina una dependencia entre dos módulos
        
        Args:
            modulo_origen (str): Nombre del módulo que depende
            modulo_destino (str): Nombre del módulo del que depende
            
        Returns:
            bool: True si se eliminó correctamente, False en caso contrario
        """
        if modulo_origen not in self.dependencias:
            return False
        
        if modulo_destino not in self.dependencias[modulo_origen]:
            return False
        
        self.dependencias[modulo_origen].remove(modulo_destino)
        
        return True
    
    def eliminar_modulo(self, nombre):
        """
        Elimina un módulo y todas sus dependencias
        
        Args:
            nombre (str): Nombre del módulo a eliminar
            
        Returns:
            bool: True si se eliminó correctamente, False si no existía
        """
        if nombre not in self.modulos:
            return False
        
        # Eliminar el módulo
        del self.modulos[nombre]
        del self.dependencias[nombre]
        
        # Eliminar todas las referencias a este módulo en otras dependencias
        for modulo in self.dependencias:
            if nombre in self.dependencias[modulo]:
                self.dependencias[modulo].remove(nombre)
        
        return True
    
    def obtener_dependencias_directas(self, nombre_modulo):
        """
        Obtiene las dependencias directas de un módulo
        
        Args:
            nombre_modulo (str): Nombre del módulo
            
        Returns:
            list: Lista de nombres de módulos de los que depende directamente
        """
        if nombre_modulo not in self.dependencias:
            return []
        
        return self.dependencias[nombre_modulo].copy()
    
    def obtener_dependientes(self, nombre_modulo):
        """
        Obtiene los módulos que dependen de este módulo
        
        Args:
            nombre_modulo (str): Nombre del módulo
            
        Returns:
            list: Lista de nombres de módulos que dependen de este
        """
        dependientes = []
        
        for modulo, deps in self.dependencias.items():
            if nombre_modulo in deps:
                dependientes.append(modulo)
        
        return dependientes
    
    def detectar_ciclos(self):
        """
        Detecta ciclos en el grafo de dependencias usando DFS
        
        Returns:
            tuple: (bool, list) - (tiene_ciclos, lista de ciclos encontrados)
        """
        visitados = set()
        en_pila = set()
        ciclos_encontrados = []
        
        def dfs(modulo, camino):
            visitados.add(modulo)
            en_pila.add(modulo)
            camino.append(modulo)
            
            for dependencia in self.dependencias.get(modulo, []):
                if dependencia not in visitados:
                    if dfs(dependencia, camino.copy()):
                        return True
                elif dependencia in en_pila:
                    # Ciclo encontrado
                    indice = camino.index(dependencia)
                    ciclo = camino[indice:] + [dependencia]
                    ciclos_encontrados.append(ciclo)
                    return True
            
            en_pila.remove(modulo)
            return False
        
        for modulo in self.modulos:
            if modulo not in visitados:
                dfs(modulo, [])
        
        return (len(ciclos_encontrados) > 0, ciclos_encontrados)
    
    def ordenamiento_topologico(self):
        """
        Realiza un ordenamiento topológico del grafo (orden de compilación)
        
        Returns:
            list: Lista ordenada de módulos, o None si hay ciclos
        """
        # Verificar que no haya ciclos
        tiene_ciclos, _ = self.detectar_ciclos()
        if tiene_ciclos:
            return None
        
        # Algoritmo de Kahn
        grados_entrada = {modulo: 0 for modulo in self.modulos}
        
        # Calcular grados de entrada
        for modulo in self.dependencias:
            for dependencia in self.dependencias[modulo]:
                grados_entrada[dependencia] += 1
        
        # Cola con módulos sin dependencias
        cola = [modulo for modulo in self.modulos if grados_entrada[modulo] == 0]
        resultado = []
        
        while cola:
            # Ordenar para tener resultados consistentes
            cola.sort()
            modulo_actual = cola.pop(0)
            resultado.append(modulo_actual)
            
            # Reducir grado de entrada de los dependientes
            dependientes = self.obtener_dependientes(modulo_actual)
            for dependiente in dependientes:
                grados_entrada[dependiente] -= 1
                if grados_entrada[dependiente] == 0:
                    cola.append(dependiente)
        
        return resultado
    
    def obtener_modulos_independientes(self):
        """
        Obtiene los módulos sin dependencias (pueden compilarse primero)
        
        Returns:
            list: Lista de nombres de módulos independientes
        """
        independientes = []
        
        for modulo in self.modulos:
            if len(self.dependencias[modulo]) == 0:
                independientes.append(modulo)
        
        return independientes
    
    def analisis_impacto(self, nombre_modulo):
        """
        Analiza qué módulos se verían afectados si se modifica un módulo
        (encuentra todas las dependencias transitivas inversas)
        
        Args:
            nombre_modulo (str): Nombre del módulo a analizar
            
        Returns:
            list: Lista de módulos afectados
        """
        if nombre_modulo not in self.modulos:
            return []
        
        afectados = set()
        
        def dfs_inverso(modulo):
            dependientes = self.obtener_dependientes(modulo)
            for dependiente in dependientes:
                if dependiente not in afectados:
                    afectados.add(dependiente)
                    dfs_inverso(dependiente)
        
        dfs_inverso(nombre_modulo)
        
        return list(afectados)
    
    def obtener_dependencias_transitivas(self, nombre_modulo):
        """
        Obtiene todas las dependencias transitivas de un módulo
        
        Args:
            nombre_modulo (str): Nombre del módulo
            
        Returns:
            list: Lista de todas las dependencias (directas e indirectas)
        """
        if nombre_modulo not in self.modulos:
            return []
        
        visitados = set()
        
        def dfs(modulo):
            for dependencia in self.dependencias.get(modulo, []):
                if dependencia not in visitados:
                    visitados.add(dependencia)
                    dfs(dependencia)
        
        dfs(nombre_modulo)
        
        return list(visitados)
    
    def obtener_estadisticas(self):
        """
        Obtiene estadísticas del grafo
        
        Returns:
            dict: Diccionario con estadísticas
        """
        total_modulos = len(self.modulos)
        total_dependencias = sum(len(deps) for deps in self.dependencias.values())
        modulos_independientes = len(self.obtener_modulos_independientes())
        tiene_ciclos, ciclos = self.detectar_ciclos()
        
        return {
            "total_modulos": total_modulos,
            "total_dependencias": total_dependencias,
            "modulos_independientes": modulos_independientes,
            "tiene_ciclos": tiene_ciclos,
            "cantidad_ciclos": len(ciclos)
        }
