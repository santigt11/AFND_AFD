#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase AFND - Autómata Finito No Determinista con transiciones épsilon
"""

from collections import defaultdict

class AFND:
    """Autómata Finito No Determinista con transiciones épsilon"""
    
    def __init__(self):
        self.estados = set()
        self.alfabeto = set()
        self.transiciones = defaultdict(lambda: defaultdict(set))
        self.estado_inicial = None
        self.estados_finales = set()
    
    def agregar_estado(self, estado):
        """Agregar un estado al autómata"""
        self.estados.add(estado)
    
    def establecer_inicial(self, estado):
        """Establecer el estado inicial"""
        self.estado_inicial = estado
        self.estados.add(estado)
    
    def agregar_final(self, estado):
        """Agregar un estado final"""
        self.estados_finales.add(estado)
        self.estados.add(estado)
    
    def agregar_transicion(self, origen, simbolo, destino):
        """Agregar una transición (origen, símbolo) -> destino"""
        self.transiciones[origen][simbolo].add(destino)
        self.estados.add(origen)
        self.estados.add(destino)
        if simbolo != 'ε':
            self.alfabeto.add(simbolo)
    
    def epsilon_clausura(self, estados):
        """Calcular la ε-clausura de un conjunto de estados"""
        clausura = set(estados)
        pila = list(estados)
        
        while pila:
            estado = pila.pop()
            for destino in self.transiciones[estado]['ε']:
                if destino not in clausura:
                    clausura.add(destino)
                    pila.append(destino)
        
        return clausura
    
    def mover(self, estados, simbolo):
        """Función MOVER: estados alcanzables desde 'estados' con 'simbolo'"""
        resultado = set()
        for estado in estados:
            resultado.update(self.transiciones[estado][simbolo])
        return resultado
    
    def imprimir_tabla_transiciones(self):
        """Imprimir la tabla de transiciones del AFND en formato matricial"""
        print("\n=== TABLA DE TRANSICIONES AFND ===")
        
        # Crear alfabeto extendido con épsilon
        alfabeto_extendido = sorted(list(self.alfabeto)) + ['ε']
        estados_ordenados = sorted(list(self.estados))
        
        # Encabezado
        header = "Estado\t" + "\t".join(alfabeto_extendido)
        print(header)
        print("-" * (len(header) + 10))
        
        # Filas de estados
        for estado in estados_ordenados:
            fila = [estado]
            
            for simbolo in alfabeto_extendido:
                transiciones_estado = self.transiciones[estado][simbolo]
                if transiciones_estado:
                    # Convertir set a lista ordenada para consistencia
                    destinos = sorted(list(transiciones_estado))
                    if len(destinos) == 1:
                        fila.append(destinos[0])
                    else:
                        # Múltiples destinos, mostrar como conjunto
                        fila.append("{" + ",".join(destinos) + "}")
                else:
                    fila.append("∅")
            
            # Marcar estados finales con asterisco
            if estado in self.estados_finales:
                fila[0] = f"{estado}*"
            
            print("\t".join(str(x) for x in fila))
