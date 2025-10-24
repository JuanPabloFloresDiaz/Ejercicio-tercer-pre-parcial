"""
Programa principal para el ejercicio de Estructuras de Datos - Árboles vs Grafos
Permite gestionar dos sistemas:
1. Sistema de Gestión Universitaria (Árbol n-ario)
2. Sistema de Gestión de Proyectos de Software (Grafo dirigido)
"""

from utils.Teclado import Teclado
from services.ServicioUniversitario import ServicioUniversitario
from services.ServicioProyectos import ServicioProyectos


def limpiar_pantalla():
    """Simula limpieza de pantalla con líneas en blanco"""
    print("\n" * 2)


def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "="*60)
        print(" "*10 + "ESTRUCTURAS DE DATOS - ÁRBOLES VS GRAFOS")
        print("="*60)
        print("\n EJERCICIOS DISPONIBLES:\n")
        print("1. Sistema de Gestión Universitaria (ÁRBOL N-ARIO)")
        print("   Jerarquía: Rectoría → Facultades → Departamentos → Programas → Asignaturas")
        print()
        print("2. Sistema de Gestión de Proyectos de Software (GRAFO DIRIGIDO)")
        print("   Módulos con dependencias y análisis de ciclos")
        print()
        print("0. Salir")
        print("="*60)
        
        opcion = Teclado.read_integer("Seleccione una opción:", min_value=0, max_value=2)
        
        if opcion == 1:
            limpiar_pantalla()
            menu_universitario()
        elif opcion == 2:
            limpiar_pantalla()
            menu_proyectos()
        elif opcion == 0:
            print("\n ¡Gracias por usar el programa! Hasta pronto.\n")
            break


def menu_universitario():
    """Menú para el Sistema de Gestión Universitaria (Árbol)"""
    servicio = ServicioUniversitario()
    
    while True:
        print("\n" + "="*60)
        print(" "*8 + "SISTEMA DE GESTIÓN UNIVERSITARIA (ÁRBOL)")
        print("="*60)
        print("\n OPERACIONES DISPONIBLES:\n")
        print("1.  Inicializar sistema")
        print("2.  Cargar datos de ejemplo")
        print("3.  Insertar nueva entidad")
        print("4.  Buscar entidad")
        print("5.  Eliminar entidad")
        print("6.  Listar hijos de una entidad")
        print("7.  Mostrar ruta jerárquica")
        print("8.  Mostrar estructura por niveles (BFS)")
        print("9.  Mostrar recorrido en profundidad (DFS)")
        print("10. Ver estadísticas del sistema")
        print()
        print("0.  Volver al menú principal")
        print("="*60)
        
        opcion = Teclado.read_integer("Seleccione una opción:", min_value=0, max_value=10)
        
        if opcion == 1:
            servicio.inicializar_sistema()
        elif opcion == 2:
            servicio.cargar_datos_ejemplo()
        elif opcion == 3:
            servicio.insertar_entidad()
        elif opcion == 4:
            servicio.buscar_entidad()
        elif opcion == 5:
            servicio.eliminar_entidad()
        elif opcion == 6:
            servicio.listar_hijos()
        elif opcion == 7:
            servicio.mostrar_ruta()
        elif opcion == 8:
            servicio.mostrar_por_niveles()
        elif opcion == 9:
            servicio.mostrar_profundidad()
        elif opcion == 10:
            servicio.mostrar_estadisticas()
        elif opcion == 0:
            print("\n Volviendo al menú principal...")
            break
        
        if opcion != 0:
            input("\nPresione Enter para continuar...")


def menu_proyectos():
    """Menú para el Sistema de Gestión de Proyectos de Software (Grafo)"""
    servicio = ServicioProyectos()
    
    while True:
        print("\n" + "="*60)
        print(" "*5 + "SISTEMA DE GESTIÓN DE PROYECTOS DE SOFTWARE (GRAFO)")
        print("="*60)
        print("\n OPERACIONES DISPONIBLES:\n")
        print("--- GESTIÓN DE MÓDULOS ---")
        print("1.  Agregar módulo")
        print("2.  Eliminar módulo")
        print("3.  Listar todos los módulos")
        print()
        print("--- GESTIÓN DE DEPENDENCIAS ---")
        print("4.  Agregar dependencia")
        print("5.  Eliminar dependencia")
        print("6.  Ver dependencias directas de un módulo")
        print("7.  Ver dependencias transitivas de un módulo")
        print()
        print("--- ANÁLISIS DEL GRAFO ---")
        print("8.  Detectar ciclos (dependencias circulares)")
        print("9.  Ordenamiento topológico (orden de compilación)")
        print("10. Ver módulos independientes")
        print("11. Análisis de impacto de un módulo")
        print("12. Ver estadísticas del sistema")
        print()
        print("--- OTROS ---")
        print("13. Cargar datos de ejemplo")
        print()
        print("0.  Volver al menú principal")
        print("="*60)
        
        opcion = Teclado.read_integer("Seleccione una opción:", min_value=0, max_value=13)
        
        if opcion == 1:
            servicio.agregar_modulo()
        elif opcion == 2:
            servicio.eliminar_modulo()
        elif opcion == 3:
            servicio.listar_todos_modulos()
        elif opcion == 4:
            servicio.agregar_dependencia()
        elif opcion == 5:
            servicio.eliminar_dependencia()
        elif opcion == 6:
            servicio.ver_dependencias_directas()
        elif opcion == 7:
            servicio.ver_dependencias_transitivas()
        elif opcion == 8:
            servicio.detectar_ciclos()
        elif opcion == 9:
            servicio.ordenamiento_topologico()
        elif opcion == 10:
            servicio.ver_modulos_independientes()
        elif opcion == 11:
            servicio.analisis_impacto()
        elif opcion == 12:
            servicio.mostrar_estadisticas()
        elif opcion == 13:
            servicio.cargar_datos_ejemplo()
        elif opcion == 0:
            print("\n Volviendo al menú principal...")
            break
        
        if opcion != 0:
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n  Programa interrumpido por el usuario")
        print(" ¡Hasta pronto!\n")
    except Exception as e:
        print(f"\n Error inesperado: {e}")
        print("Por favor, contacte al administrador del sistema\n")