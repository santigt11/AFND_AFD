# Programa principal simple para convertir AFND a AFD

from afnd import AFND
from conversor import convertir_afnd_a_afd
from generador_grafos import GraficadorAutomatas

def crear_afnd():
    """Crear un AFND de ejemplo para demostración"""
    afnd = AFND()
    
    # Definir estados
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
    
    # Estado inicial y finales
    afnd.establecer_inicial('q0')
    afnd.agregar_final('q10')
    
    # Transiciones
    afnd.agregar_transicion('q0', 'ε', 'q1')
    afnd.agregar_transicion('q1', 'ε', 'q2')
    afnd.agregar_transicion('q1', 'ε', 'q4')
    afnd.agregar_transicion('q0', 'ε', 'q7')
    afnd.agregar_transicion('q2', 'a', 'q3')
    afnd.agregar_transicion('q4', 'b', 'q5')
    afnd.agregar_transicion('q5', 'ε', 'q6')
    afnd.agregar_transicion('q6', 'ε', 'q7')
    afnd.agregar_transicion('q7', 'a', 'q8')
    afnd.agregar_transicion('q8', 'b', 'q9')
    afnd.agregar_transicion('q9', 'b', 'q10')
    afnd.agregar_transicion('q6', 'ε', 'q1')
    afnd.agregar_transicion('q3', 'ε', 'q6')
    
    return afnd

def main():
    print("CONVERSIÓN DE AFND A AFD")
    print("=" * 50)
    
    # Crear el AFND
    afnd = crear_afnd()
    
    # Mostrar la tabla del AFND con epsilon clausuras calculadas
    afnd.imprimir_tabla_transiciones()
      # Convertir a AFD usando el conversor arreglado
    afd = convertir_afnd_a_afd(afnd)
    
    # Mostrar las tablas del AFD
    afd.mostrar_tabla()
    afd.mostrar_conjuntos()
    
    # Generar los grafos de ambos autómatas
    graficador = GraficadorAutomatas()
    graficador.generar_ambos_grafos(afnd, afd)
    
    print("\n" + "=" * 50)
    print("Conversión completada")

if __name__ == "__main__":
    main()
