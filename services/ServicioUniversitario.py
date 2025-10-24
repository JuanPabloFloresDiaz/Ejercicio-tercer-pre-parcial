"""Servicio para gestionar el Sistema de Gestión Universitaria usando árbol n-ario"""

from models.Arbol import ArbolUniversitario
from utils.Teclado import Teclado


class ServicioUniversitario:
    """Servicio que gestiona las operaciones del sistema universitario"""
    
    def __init__(self):
        """Inicializa el servicio con un árbol universitario vacío"""
        self.arbol = None
    
    def inicializar_sistema(self):
        """Inicializa el sistema con datos de ejemplo o nuevo"""
        print("\n" + "="*60)
        print("INICIALIZACIÓN DEL SISTEMA UNIVERSITARIO")
        print("="*60)
        
        nombre_rectoria = Teclado.read_text(
            "Ingrese el nombre de la Rectoría:",
            min_length=3,
            max_length=100
        )
        
        self.arbol = ArbolUniversitario(nombre_rectoria)
        print(f"\n Sistema inicializado con '{nombre_rectoria}' como raíz")
    
    def insertar_entidad(self):
        """Inserta una nueva entidad en el árbol"""
        print("\n" + "="*60)
        print("INSERTAR NUEVA ENTIDAD")
        print("="*60)
        
        if self.arbol is None:
            print(" Debe inicializar el sistema primero")
            return
        
        # Mostrar estructura actual
        print("\nEstructura actual:")
        self._mostrar_arbol_simple()
        
        print("\nTipos de entidades disponibles:")
        print("1. Facultad (bajo Rectoría)")
        print("2. Departamento (bajo Facultad)")
        print("3. Programa (bajo Departamento)")
        print("4. Asignatura (bajo Programa)")
        
        tipo_opcion = Teclado.read_integer("\nSeleccione el tipo de entidad:", min_value=1, max_value=4)
        
        tipos = {
            1: "Facultad",
            2: "Departamento",
            3: "Programa",
            4: "Asignatura"
        }
        
        tipo_nuevo = tipos[tipo_opcion]
        
        nombre_padre = Teclado.read_text(
            f"Ingrese el nombre de la entidad padre:",
            min_length=3,
            max_length=100
        )
        
        nombre_nuevo = Teclado.read_text(
            f"Ingrese el nombre de la nueva {tipo_nuevo}:",
            min_length=3,
            max_length=100
        )
        
        descripcion = Teclado.read_text(
            "Ingrese una descripción (opcional, presione Enter para omitir):",
            min_length=0,
            max_length=200
        ) if input("¿Desea agregar descripción? (s/n): ").lower() == 's' else ""
        
        if self.arbol.insertar(nombre_padre, nombre_nuevo, tipo_nuevo, descripcion):
            print(f"\n {tipo_nuevo} '{nombre_nuevo}' insertada correctamente bajo '{nombre_padre}'")
        else:
            print(f"\n Error: No se pudo insertar. Verifique que:")
            print(f"   - La entidad padre '{nombre_padre}' exista")
            print(f"   - La relación sea válida (jerarquía correcta)")
            print(f"   - No exista ya una entidad con ese nombre en ese nivel")
    
    def buscar_entidad(self):
        """Busca y muestra información de una entidad"""
        print("\n" + "="*60)
        print("BUSCAR ENTIDAD")
        print("="*60)
        
        if self.arbol is None:
            print(" Debe inicializar el sistema primero")
            return
        
        nombre = Teclado.read_text(
            "Ingrese el nombre de la entidad a buscar:",
            min_length=1,
            max_length=100
        )
        
        nodo = self.arbol.buscar(nombre)
        
        if nodo:
            print(f"\n Entidad encontrada:")
            print(f"   Nombre: {nodo.nombre}")
            print(f"   Tipo: {nodo.tipo}")
            print(f"   Descripción: {nodo.descripcion if nodo.descripcion else 'Sin descripción'}")
            print(f"   Cantidad de hijos: {len(nodo.hijos)}")
            
            if nodo.hijos:
                print(f"   Hijos directos:")
                for hijo in nodo.hijos:
                    print(f"      - {hijo.nombre} ({hijo.tipo})")
        else:
            print(f"\n No se encontró la entidad '{nombre}'")
    
    def eliminar_entidad(self):
        """Elimina una entidad y sus descendientes"""
        print("\n" + "="*60)
        print("ELIMINAR ENTIDAD")
        print("="*60)
        
        if self.arbol is None:
            print(" Debe inicializar el sistema primero")
            return
        
        # Mostrar estructura actual
        print("\nEstructura actual:")
        self._mostrar_arbol_simple()
        
        nombre = Teclado.read_text(
            "\nIngrese el nombre de la entidad a eliminar:",
            min_length=1,
            max_length=100
        )
        
        # Verificar que existe
        nodo = self.arbol.buscar(nombre)
        if not nodo:
            print(f"\n No se encontró la entidad '{nombre}'")
            return
        
        # Advertencia sobre eliminación en cascada
        if nodo.hijos:
            print(f"\n  ADVERTENCIA: Esta entidad tiene {len(nodo.hijos)} hijo(s)")
            print("   Se eliminarán también todos sus descendientes")
            confirmar = input("¿Está seguro? (s/n): ").lower()
            if confirmar != 's':
                print("Operación cancelada")
                return
        
        if self.arbol.eliminar(nombre):
            print(f"\n Entidad '{nombre}' eliminada correctamente")
        else:
            print(f"\n No se pudo eliminar '{nombre}' (no se puede eliminar la Rectoría)")
    
    def listar_hijos(self):
        """Lista los hijos directos de una entidad"""
        print("\n" + "="*60)
        print("LISTAR HIJOS DE UNA ENTIDAD")
        print("="*60)
        
        if self.arbol is None:
            print(" Debe inicializar el sistema primero")
            return
        
        nombre = Teclado.read_text(
            "Ingrese el nombre de la entidad:",
            min_length=1,
            max_length=100
        )
        
        hijos = self.arbol.listar_hijos(nombre)
        
        if hijos is None:
            print(f"\n No se encontró la entidad '{nombre}'")
        elif len(hijos) == 0:
            print(f"\n La entidad '{nombre}' no tiene hijos")
        else:
            print(f"\n Hijos de '{nombre}' ({len(hijos)} encontrados):")
            for i, hijo in enumerate(hijos, 1):
                print(f"   {i}. {hijo.nombre} ({hijo.tipo})")
                if hijo.descripcion:
                    print(f"      Descripción: {hijo.descripcion}")
    
    def mostrar_ruta(self):
        """Muestra la ruta jerárquica completa hasta una entidad"""
        print("\n" + "="*60)
        print("MOSTRAR RUTA JERÁRQUICA")
        print("="*60)
        
        if self.arbol is None:
            print(" Debe inicializar el sistema primero")
            return
        
        nombre = Teclado.read_text(
            "Ingrese el nombre de la entidad:",
            min_length=1,
            max_length=100
        )
        
        ruta = self.arbol.obtener_ruta(nombre)
        
        if not ruta:
            print(f"\n No se encontró la entidad '{nombre}'")
        else:
            print(f"\n Ruta jerárquica hasta '{nombre}':")
            for i, nodo in enumerate(ruta):
                indentacion = "   " * i
                flecha = "└─ " if i > 0 else ""
                print(f"{indentacion}{flecha}{nodo.nombre} ({nodo.tipo})")
    
    def mostrar_por_niveles(self):
        """Muestra el árbol organizado por niveles (BFS)"""
        print("\n" + "="*60)
        print("ESTRUCTURA POR NIVELES (BFS)")
        print("="*60)
        
        if self.arbol is None:
            print(" Debe inicializar el sistema primero")
            return
        
        niveles = self.arbol.recorrido_por_niveles()
        
        nombres_niveles = ["Nivel 0 - Rectoría", "Nivel 1 - Facultades", 
                          "Nivel 2 - Departamentos", "Nivel 3 - Programas", 
                          "Nivel 4 - Asignaturas"]
        
        for i, nivel in enumerate(niveles):
            if i < len(nombres_niveles):
                print(f"\n{nombres_niveles[i]}:")
            else:
                print(f"\nNivel {i}:")
            
            for nodo in nivel:
                print(f"   • {nodo.nombre}")
                if nodo.descripcion:
                    print(f"     ({nodo.descripcion})")
    
    def mostrar_profundidad(self):
        """Muestra el árbol en recorrido por profundidad (DFS)"""
        print("\n" + "="*60)
        print("RECORRIDO EN PROFUNDIDAD (DFS)")
        print("="*60)
        
        if self.arbol is None:
            print(" Debe inicializar el sistema primero")
            return
        
        nodos = self.arbol.recorrido_profundidad()
        
        print("\nOrden de recorrido DFS:")
        for i, nodo in enumerate(nodos, 1):
            print(f"{i}. {nodo.nombre} ({nodo.tipo})")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas del sistema"""
        print("\n" + "="*60)
        print("ESTADÍSTICAS DEL SISTEMA")
        print("="*60)
        
        if self.arbol is None:
            print(" Debe inicializar el sistema primero")
            return
        
        stats = self.arbol.obtener_estadisticas()
        
        print("\n Resumen de entidades:")
        total = sum(stats.values())
        
        for tipo, cantidad in stats.items():
            print(f"   {tipo:15s}: {cantidad:3d}")
        
        print(f"   {'─'*20}")
        print(f"   {'TOTAL':15s}: {total:3d}")
    
    def _mostrar_arbol_simple(self):
        """Muestra una vista simple del árbol"""
        if self.arbol is None:
            return
        
        def imprimir_nodo(nodo, nivel=0):
            indentacion = "  " * nivel
            simbolo = "└─ " if nivel > 0 else ""
            print(f"{indentacion}{simbolo}{nodo.nombre} ({nodo.tipo})")
            for hijo in nodo.hijos:
                imprimir_nodo(hijo, nivel + 1)
        
        imprimir_nodo(self.arbol.raiz)
    
    def cargar_datos_ejemplo(self):
        """Carga datos de ejemplo en el sistema"""
        if self.arbol is None:
            self.arbol = ArbolUniversitario("Universidad Nacional")
        
        # Facultades
        self.arbol.insertar("Universidad Nacional", "Facultad de Ingeniería", "Facultad", "Ciencias de la Ingeniería")
        self.arbol.insertar("Universidad Nacional", "Facultad de Ciencias", "Facultad", "Ciencias Naturales y Matemáticas")
        
        # Departamentos de Ingeniería
        self.arbol.insertar("Facultad de Ingeniería", "Departamento de Sistemas", "Departamento", "Informática y Computación")
        self.arbol.insertar("Facultad de Ingeniería", "Departamento de Industrial", "Departamento", "Ingeniería Industrial")
        
        # Departamentos de Ciencias
        self.arbol.insertar("Facultad de Ciencias", "Departamento de Matemáticas", "Departamento", "Matemática Pura y Aplicada")
        
        # Programas de Sistemas
        self.arbol.insertar("Departamento de Sistemas", "Licenciatura en Informática", "Programa", "Pregrado 5 años")
        self.arbol.insertar("Departamento de Sistemas", "Maestría en Ciencias de Datos", "Programa", "Posgrado 2 años")
        
        # Asignaturas de Informática
        self.arbol.insertar("Licenciatura en Informática", "Estructura de Datos", "Asignatura", "Algoritmos y estructuras")
        self.arbol.insertar("Licenciatura en Informática", "Bases de Datos", "Asignatura", "Gestión de información")
        self.arbol.insertar("Licenciatura en Informática", "Programación Orientada a Objetos", "Asignatura", "Paradigmas de programación")
        
        print("\n Datos de ejemplo cargados correctamente")
