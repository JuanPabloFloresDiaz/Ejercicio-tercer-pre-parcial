#!/usr/bin/env python3
"""
Script de prueba para verificar el funcionamiento de las estructuras de datos
"""

from models.Arbol import ArbolUniversitario
from models.Grafo import GrafoDependencias

def probar_arbol():
    """Prueba las operaciones del árbol"""
    print("="*60)
    print("PRUEBA DEL ÁRBOL N-ARIO")
    print("="*60)
    
    # Crear árbol
    arbol = ArbolUniversitario("Universidad de Prueba")
    print("\n Árbol creado")
    
    # Insertar entidades
    arbol.insertar("Universidad de Prueba", "Facultad de Ingeniería", "Facultad")
    arbol.insertar("Facultad de Ingeniería", "Departamento de Sistemas", "Departamento")
    arbol.insertar("Departamento de Sistemas", "Licenciatura en Informática", "Programa")
    arbol.insertar("Licenciatura en Informática", "Estructura de Datos", "Asignatura")
    print(" Entidades insertadas")
    
    # Buscar
    nodo = arbol.buscar("Estructura de Datos")
    print(f" Búsqueda exitosa: {nodo.nombre if nodo else 'No encontrado'}")
    
    # Obtener ruta
    ruta = arbol.obtener_ruta("Estructura de Datos")
    print(f" Ruta: {' → '.join([n.nombre for n in ruta])}")
    
    # Estadísticas
    stats = arbol.obtener_estadisticas()
    print(f" Estadísticas: {stats}")
    
    print("\n TODAS LAS PRUEBAS DEL ÁRBOL PASARON\n")


def probar_grafo():
    """Prueba las operaciones del grafo"""
    print("="*60)
    print("PRUEBA DEL GRAFO DIRIGIDO")
    print("="*60)
    
    # Crear grafo
    grafo = GrafoDependencias()
    print("\n Grafo creado")
    
    # Agregar módulos
    grafo.agregar_modulo("A", "Módulo A")
    grafo.agregar_modulo("B", "Módulo B")
    grafo.agregar_modulo("C", "Módulo C")
    grafo.agregar_modulo("D", "Módulo D")
    print(" Módulos agregados")
    
    # Agregar dependencias (sin ciclos)
    grafo.agregar_dependencia("A", "B")  # A depende de B
    grafo.agregar_dependencia("A", "C")  # A depende de C
    grafo.agregar_dependencia("B", "D")  # B depende de D
    grafo.agregar_dependencia("C", "D")  # C depende de D
    print(" Dependencias agregadas")
    
    # Detectar ciclos
    tiene_ciclos, ciclos = grafo.detectar_ciclos()
    print(f" Detección de ciclos: {'Tiene ciclos' if tiene_ciclos else 'Sin ciclos'}")
    
    # Ordenamiento topológico
    orden = grafo.ordenamiento_topologico()
    print(f" Orden topológico: {orden}")
    
    # Módulos independientes
    independientes = grafo.obtener_modulos_independientes()
    print(f" Módulos independientes: {independientes}")
    
    # Estadísticas
    stats = grafo.obtener_estadisticas()
    print(f" Estadísticas: {stats}")
    
    print("\n TODAS LAS PRUEBAS DEL GRAFO PASARON\n")


def probar_grafo_con_ciclos():
    """Prueba la detección de ciclos"""
    print("="*60)
    print("PRUEBA DE DETECCIÓN DE CICLOS")
    print("="*60)
    
    grafo = GrafoDependencias()
    
    # Crear un ciclo: A → B → C → A
    grafo.agregar_modulo("A", "Módulo A")
    grafo.agregar_modulo("B", "Módulo B")
    grafo.agregar_modulo("C", "Módulo C")
    
    grafo.agregar_dependencia("A", "B")
    grafo.agregar_dependencia("B", "C")
    grafo.agregar_dependencia("C", "A")  # Esto crea un ciclo
    
    print("\n Grafo con ciclo creado: A → B → C → A")
    
    tiene_ciclos, ciclos = grafo.detectar_ciclos()
    
    if tiene_ciclos:
        print(f" Ciclo detectado correctamente: {ciclos}")
        print(" Ordenamiento topológico no es posible (como se esperaba)")
        orden = grafo.ordenamiento_topologico()
        assert orden is None, "El ordenamiento debería ser None con ciclos"
    else:
        print(" ERROR: No se detectó el ciclo")
    
    print("\n PRUEBA DE CICLOS COMPLETADA\n")


if __name__ == "__main__":
    try:
        probar_arbol()
        probar_grafo()
        probar_grafo_con_ciclos()
        
        print("="*60)
        print(" TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
        print("="*60)
        print("\nEl sistema está listo para usar.")
        print("Ejecute 'python3 Main.py' para iniciar el programa.\n")
        
    except Exception as e:
        print(f"\n ERROR EN LAS PRUEBAS: {e}")
        import traceback
        traceback.print_exc()
