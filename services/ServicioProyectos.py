"""Servicio para gestionar el Sistema de Gestión de Proyectos de Software usando grafo dirigido"""

from models.Grafo import GrafoDependencias
from utils.Teclado import Teclado


class ServicioProyectos:
    """Servicio que gestiona las operaciones del sistema de proyectos de software"""
    
    def __init__(self):
        """Inicializa el servicio con un grafo vacío"""
        self.grafo = GrafoDependencias()
    
    def agregar_modulo(self):
        """Agrega un nuevo módulo al grafo"""
        print("\n" + "="*60)
        print("AGREGAR NUEVO MÓDULO")
        print("="*60)
        
        nombre = Teclado.read_text(
            "Ingrese el nombre del módulo:",
            min_length=2,
            max_length=50
        )
        
        descripcion = input("Ingrese una descripción (opcional, Enter para omitir): ").strip()
        
        if self.grafo.agregar_modulo(nombre, descripcion):
            print(f"\n Módulo '{nombre}' agregado correctamente")
        else:
            print(f"\n Error: El módulo '{nombre}' ya existe")
    
    def agregar_dependencia(self):
        """Agrega una dependencia entre dos módulos"""
        print("\n" + "="*60)
        print("AGREGAR DEPENDENCIA ENTRE MÓDULOS")
        print("="*60)
        
        if len(self.grafo.modulos) == 0:
            print(" No hay módulos en el sistema. Agregue módulos primero.")
            return
        
        print("\nMódulos disponibles:")
        self._listar_modulos_simple()
        
        modulo_origen = Teclado.read_text(
            "\nIngrese el nombre del módulo que DEPENDE:",
            min_length=1,
            max_length=50
        )
        
        modulo_destino = Teclado.read_text(
            "Ingrese el nombre del módulo DEL QUE DEPENDE:",
            min_length=1,
            max_length=50
        )
        
        if self.grafo.agregar_dependencia(modulo_origen, modulo_destino):
            print(f"\n Dependencia agregada: '{modulo_origen}' → '{modulo_destino}'")
            print(f"   ('{modulo_origen}' depende de '{modulo_destino}')")
        else:
            print(f"\n Error: No se pudo agregar la dependencia")
            print("   Verifique que ambos módulos existan y no sea una auto-dependencia")
    
    def eliminar_dependencia(self):
        """Elimina una dependencia entre dos módulos"""
        print("\n" + "="*60)
        print("ELIMINAR DEPENDENCIA")
        print("="*60)
        
        if len(self.grafo.modulos) == 0:
            print(" No hay módulos en el sistema")
            return
        
        print("\nDependencias actuales:")
        self._mostrar_todas_dependencias()
        
        modulo_origen = Teclado.read_text(
            "\nIngrese el módulo origen:",
            min_length=1,
            max_length=50
        )
        
        modulo_destino = Teclado.read_text(
            "Ingrese el módulo destino:",
            min_length=1,
            max_length=50
        )
        
        if self.grafo.eliminar_dependencia(modulo_origen, modulo_destino):
            print(f"\n Dependencia eliminada correctamente")
        else:
            print(f"\n Error: No se encontró la dependencia")
    
    def eliminar_modulo(self):
        """Elimina un módulo del sistema"""
        print("\n" + "="*60)
        print("ELIMINAR MÓDULO")
        print("="*60)
        
        if len(self.grafo.modulos) == 0:
            print(" No hay módulos en el sistema")
            return
        
        print("\nMódulos disponibles:")
        self._listar_modulos_simple()
        
        nombre = Teclado.read_text(
            "\nIngrese el nombre del módulo a eliminar:",
            min_length=1,
            max_length=50
        )
        
        # Verificar impacto antes de eliminar
        dependientes = self.grafo.obtener_dependientes(nombre)
        if dependientes:
            print(f"\n  ADVERTENCIA: {len(dependientes)} módulo(s) dependen de '{nombre}':")
            for dep in dependientes:
                print(f"   - {dep}")
            confirmar = input("\n¿Está seguro de eliminar? (s/n): ").lower()
            if confirmar != 's':
                print("Operación cancelada")
                return
        
        if self.grafo.eliminar_modulo(nombre):
            print(f"\n Módulo '{nombre}' eliminado correctamente")
        else:
            print(f"\n Error: No se encontró el módulo '{nombre}'")
    
    def ver_dependencias_directas(self):
        """Muestra las dependencias directas de un módulo"""
        print("\n" + "="*60)
        print("DEPENDENCIAS DIRECTAS DE UN MÓDULO")
        print("="*60)
        
        if len(self.grafo.modulos) == 0:
            print(" No hay módulos en el sistema")
            return
        
        nombre = Teclado.read_text(
            "Ingrese el nombre del módulo:",
            min_length=1,
            max_length=50
        )
        
        if nombre not in self.grafo.modulos:
            print(f"\n El módulo '{nombre}' no existe")
            return
        
        dependencias = self.grafo.obtener_dependencias_directas(nombre)
        
        if not dependencias:
            print(f"\n El módulo '{nombre}' no tiene dependencias directas")
        else:
            print(f"\n '{nombre}' depende directamente de {len(dependencias)} módulo(s):")
            for dep in dependencias:
                print(f"   → {dep}")
    
    def ver_dependencias_transitivas(self):
        """Muestra todas las dependencias transitivas de un módulo"""
        print("\n" + "="*60)
        print("DEPENDENCIAS TRANSITIVAS (DIRECTAS E INDIRECTAS)")
        print("="*60)
        
        if len(self.grafo.modulos) == 0:
            print(" No hay módulos en el sistema")
            return
        
        nombre = Teclado.read_text(
            "Ingrese el nombre del módulo:",
            min_length=1,
            max_length=50
        )
        
        if nombre not in self.grafo.modulos:
            print(f"\n El módulo '{nombre}' no existe")
            return
        
        dependencias = self.grafo.obtener_dependencias_transitivas(nombre)
        
        if not dependencias:
            print(f"\n El módulo '{nombre}' no tiene dependencias")
        else:
            print(f"\n '{nombre}' depende (directa o indirectamente) de {len(dependencias)} módulo(s):")
            for dep in dependencias:
                print(f"   → {dep}")
    
    def detectar_ciclos(self):
        """Detecta ciclos en las dependencias"""
        print("\n" + "="*60)
        print("DETECCIÓN DE CICLOS (DEPENDENCIAS CIRCULARES)")
        print("="*60)
        
        if len(self.grafo.modulos) == 0:
            print(" No hay módulos en el sistema")
            return
        
        tiene_ciclos, ciclos = self.grafo.detectar_ciclos()
        
        if not tiene_ciclos:
            print("\n No se detectaron dependencias circulares")
            print("   El grafo es acíclico (DAG - Directed Acyclic Graph)")
        else:
            print(f"\n  SE DETECTARON {len(ciclos)} CICLO(S) EN LAS DEPENDENCIAS:")
            for i, ciclo in enumerate(ciclos, 1):
                print(f"\n   Ciclo {i}:")
                print(f"   {' → '.join(ciclo)}")
            print("\n Los ciclos pueden causar problemas de compilación")
    
    def ordenamiento_topologico(self):
        """Muestra el orden de compilación de los módulos"""
        print("\n" + "="*60)
        print("ORDEN DE COMPILACIÓN (ORDENAMIENTO TOPOLÓGICO)")
        print("="*60)
        
        if len(self.grafo.modulos) == 0:
            print(" No hay módulos en el sistema")
            return
        
        orden = self.grafo.ordenamiento_topologico()
        
        if orden is None:
            print("\n No se puede determinar el orden de compilación")
            print("   Existen dependencias circulares en el grafo")
            print("   Use la opción de 'Detectar ciclos' para identificarlos")
        else:
            print(f"\n Orden de compilación óptimo ({len(orden)} módulos):")
            for i, modulo in enumerate(orden, 1):
                print(f"   {i}. {modulo}")
    
    def ver_modulos_independientes(self):
        """Muestra los módulos sin dependencias"""
        print("\n" + "="*60)
        print("MÓDULOS INDEPENDIENTES (SIN DEPENDENCIAS)")
        print("="*60)
        
        if len(self.grafo.modulos) == 0:
            print(" No hay módulos en el sistema")
            return
        
        independientes = self.grafo.obtener_modulos_independientes()
        
        if not independientes:
            print("\n No hay módulos independientes")
            print("   Todos los módulos tienen al menos una dependencia")
        else:
            print(f"\n Módulos que pueden compilarse primero ({len(independientes)}):")
            print("   (No tienen dependencias de otros módulos)")
            for modulo in independientes:
                print(f"    {modulo}")
    
    def analisis_impacto(self):
        """Analiza el impacto de modificar un módulo"""
        print("\n" + "="*60)
        print("ANÁLISIS DE IMPACTO")
        print("="*60)
        
        if len(self.grafo.modulos) == 0:
            print(" No hay módulos en el sistema")
            return
        
        nombre = Teclado.read_text(
            "Ingrese el módulo a analizar:",
            min_length=1,
            max_length=50
        )
        
        if nombre not in self.grafo.modulos:
            print(f"\n El módulo '{nombre}' no existe")
            return
        
        afectados = self.grafo.analisis_impacto(nombre)
        
        if not afectados:
            print(f"\n Modificar '{nombre}' NO afectará a otros módulos")
            print("   (Ningún módulo depende de este)")
        else:
            print(f"\n Modificar '{nombre}' AFECTARÁ a {len(afectados)} módulo(s):")
            print("   (Módulos que dependen directa o indirectamente de este)")
            for modulo in afectados:
                print(f"     {modulo}")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas del grafo"""
        print("\n" + "="*60)
        print("ESTADÍSTICAS DEL SISTEMA")
        print("="*60)
        
        if len(self.grafo.modulos) == 0:
            print(" No hay módulos en el sistema")
            return
        
        stats = self.grafo.obtener_estadisticas()
        
        print("\n Resumen del grafo:")
        print(f"   Total de módulos:         {stats['total_modulos']}")
        print(f"   Total de dependencias:    {stats['total_dependencias']}")
        print(f"   Módulos independientes:   {stats['modulos_independientes']}")
        print(f"   Tiene ciclos:             {'Sí ' if stats['tiene_ciclos'] else 'No '}")
        if stats['tiene_ciclos']:
            print(f"   Cantidad de ciclos:       {stats['cantidad_ciclos']}")
        
        # Información adicional
        if stats['total_modulos'] > 0:
            promedio = stats['total_dependencias'] / stats['total_modulos']
            print(f"\n   Promedio de dependencias por módulo: {promedio:.2f}")
    
    def listar_todos_modulos(self):
        """Lista todos los módulos con sus dependencias"""
        print("\n" + "="*60)
        print("LISTA COMPLETA DE MÓDULOS Y DEPENDENCIAS")
        print("="*60)
        
        if len(self.grafo.modulos) == 0:
            print(" No hay módulos en el sistema")
            return
        
        print(f"\nTotal de módulos: {len(self.grafo.modulos)}\n")
        
        for nombre, modulo in sorted(self.grafo.modulos.items()):
            print(f" {modulo.nombre}")
            if modulo.descripcion:
                print(f"   Descripción: {modulo.descripcion}")
            
            deps = self.grafo.obtener_dependencias_directas(nombre)
            if deps:
                print(f"   Depende de: {', '.join(deps)}")
            else:
                print(f"   Sin dependencias ")
            
            dependientes = self.grafo.obtener_dependientes(nombre)
            if dependientes:
                print(f"   Requerido por: {', '.join(dependientes)}")
            
            print()
    
    def _listar_modulos_simple(self):
        """Lista los módulos de forma simple"""
        for i, nombre in enumerate(sorted(self.grafo.modulos.keys()), 1):
            print(f"   {i}. {nombre}")
    
    def _mostrar_todas_dependencias(self):
        """Muestra todas las dependencias del sistema"""
        hay_dependencias = False
        for modulo, deps in sorted(self.grafo.dependencias.items()):
            if deps:
                hay_dependencias = True
                print(f"   {modulo} → {', '.join(deps)}")
        
        if not hay_dependencias:
            print("   (No hay dependencias registradas)")
    
    def cargar_datos_ejemplo(self):
        """Carga datos de ejemplo en el sistema"""
        # Módulos
        modulos = [
            ("Autenticación", "Gestión de usuarios y login"),
            ("Base de Datos", "Capa de acceso a datos"),
            ("API REST", "Interfaz de servicios web"),
            ("Validaciones", "Validación de datos"),
            ("Logs", "Sistema de registro de eventos"),
            ("Reportes", "Generación de reportes"),
            ("Notificaciones", "Envío de notificaciones"),
            ("Pagos", "Procesamiento de pagos")
        ]
        
        for nombre, desc in modulos:
            self.grafo.agregar_modulo(nombre, desc)
        
        # Dependencias
        dependencias = [
            ("API REST", "Autenticación"),
            ("API REST", "Validaciones"),
            ("Autenticación", "Base de Datos"),
            ("Autenticación", "Logs"),
            ("Reportes", "Base de Datos"),
            ("Reportes", "Autenticación"),
            ("Notificaciones", "Logs"),
            ("Pagos", "Autenticación"),
            ("Pagos", "Base de Datos"),
            ("Pagos", "Notificaciones"),
            ("Validaciones", "Logs")
        ]
        
        for origen, destino in dependencias:
            self.grafo.agregar_dependencia(origen, destino)
        
        print("\n Datos de ejemplo cargados correctamente")
        print(f"   - {len(modulos)} módulos")
        print(f"   - {len(dependencias)} dependencias")
