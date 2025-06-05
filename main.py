from afnd import AFND
from conversor import convertir_afnd_a_afd
from generador_grafos import crear_ambos_grafos

def crear_ejemplo_afnd():
    """Crea un AFND de ejemplo para demostrar la conversión"""
    
    print("Creando AFND...")
    
    # Crear un nuevo AFND
    afnd = AFND()
    
    # Agregar todos los estados
    afnd.agregar_estado('q0')
    afnd.agregar_estado('q1') 
    afnd.agregar_estado('q2')
    afnd.agregar_estado('q3')
    afnd.agregar_estado('q4')
    afnd.agregar_estado('q5')
    afnd.agregar_estado('q6')
    afnd.agregar_estado('q7')
    afnd.agregar_estado('q8')
    afnd.agregar_estado('q9')
    afnd.agregar_estado('q10')
    
    # Definir el estado inicial y final
    afnd.establecer_inicial('q0')
    afnd.agregar_final('q10')
    
    # Agregar todas las transiciones
    afnd.agregar_transicion('q0', 'ε', 'q1')    # épsilon desde q0 a q1
    afnd.agregar_transicion('q1', 'ε', 'q2')    # épsilon desde q1 a q2
    afnd.agregar_transicion('q1', 'ε', 'q4')    # épsilon desde q1 a q4
    afnd.agregar_transicion('q0', 'ε', 'q7')    # épsilon desde q0 a q7
    afnd.agregar_transicion('q2', 'a', 'q3')    # 'a' desde q2 a q3
    afnd.agregar_transicion('q4', 'b', 'q5')    # 'b' desde q4 a q5
    afnd.agregar_transicion('q5', 'ε', 'q6')    # épsilon desde q5 a q6
    afnd.agregar_transicion('q6', 'ε', 'q7')    # épsilon desde q6 a q7
    afnd.agregar_transicion('q7', 'a', 'q8')    # 'a' desde q7 a q8
    afnd.agregar_transicion('q8', 'b', 'q9')    # 'b' desde q8 a q9
    afnd.agregar_transicion('q9', 'b', 'q10')   # 'b' desde q9 a q10
    afnd.agregar_transicion('q6', 'ε', 'q1')    # épsilon desde q6 a q1
    afnd.agregar_transicion('q3', 'ε', 'q6')    # épsilon desde q3 a q6
    
    print(" ||AFND creado exitosamente||")
    return afnd

def main():
    """Función principal del programa"""
    
    print("=" * 60)
    print("    CONVERSIÓN DE AFND A AFD   ")
    print("=" * 60)
    
    # PASO 1: Crear el AFND de ejemplo
    afnd = crear_ejemplo_afnd()
    
    # PASO 2: Mostrar la tabla del AFND
    afnd.imprimir_tabla_transiciones()
    
    # PASO 3: Convertir el AFND a AFD
    afd = convertir_afnd_a_afd(afnd)
    
    # PASO 4: Mostrar las tablas del AFD
    afd.mostrar_tabla()
    afd.mostrar_conjuntos()
    
    # PASO 5: Crear los grafos para visualizar
    crear_ambos_grafos(afnd, afd)
    
    print("\n" + "=" * 60)
    print("    ¡CONVERSIÓN COMPLETADA EXITOSAMENTE!")
    print("=" * 60)

# Este código se ejecuta cuando corres el archivo
if __name__ == "__main__":
    main()
