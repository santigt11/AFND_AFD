class AFD:
    """Un autómata que solo puede estar en un estado a la vez"""
    
    def __init__(self):
        # Lista de todos los estados
        self.estados = []
        
        # Diccionario de transiciones: estado -> símbolo -> estado destino
        self.transiciones = {}
        
        # El estado donde empieza el autómata
        self.estado_inicial = ""
        
        # Lista de estados finales (de aceptación)
        self.estados_finales = []
        
        # Diccionario para convertir estados a letras (A, B, C...)
        self.estados_a_letras = {}
    
    def agregar_transicion(self, estado_origen, simbolo, estado_destino):
        """Agrega una transición: desde un estado, con un símbolo, a otro estado"""
        
        # Crear el diccionario para el estado origen si no existe
        if estado_origen not in self.transiciones:
            self.transiciones[estado_origen] = {}
        
        # Agregar la transición
        self.transiciones[estado_origen][simbolo] = estado_destino
    
    def asignar_letras(self):
        """Asigna letras A, B, C... a los estados"""
        
        # El estado inicial siempre es A
        if self.estado_inicial in self.estados:
            self.estados_a_letras[self.estado_inicial] = 'A'
        
        # Asignar B, C, D... a los demás estados
        letra_numero = 1  # Para B, C, D...
        for estado in self.estados:
            if estado != self.estado_inicial:
                letra = chr(ord('A') + letra_numero)  # Convertir número a letra
                self.estados_a_letras[estado] = letra
                letra_numero = letra_numero + 1
    
    def mostrar_tabla(self):
        """Muestra la tabla de transiciones del AFD"""
        
        print("\n=== TABLA DE TRANSICIONES AFD ===")
        print("Estado\ta\tb")
        print("-" * 20)
        
        # Mostrar estados en orden: primero el inicial (A), luego los demás
        estados_en_orden = [self.estado_inicial]
        for estado in self.estados:
            if estado != self.estado_inicial:
                estados_en_orden.append(estado)
        
        # Mostrar cada estado
        for estado in estados_en_orden:
            letra = self.estados_a_letras[estado]
            
            # Agregar * si es estado final
            if estado in self.estados_finales:
                letra = letra + "*"
            
            linea = letra + "\t"
            
            # Columna para símbolo 'a'
            if estado in self.transiciones and 'a' in self.transiciones[estado]:
                destino = self.transiciones[estado]['a']
                linea = linea + self.estados_a_letras[destino]
            else:
                linea = linea + "∅"  # Vacío
            
            linea = linea + "\t"
            
            # Columna para símbolo 'b'
            if estado in self.transiciones and 'b' in self.transiciones[estado]:
                destino = self.transiciones[estado]['b']
                linea = linea + self.estados_a_letras[destino]
            else:
                linea = linea + "∅"  # Vacío
            
            print(linea)
    
    def mostrar_conjuntos(self):
        """Muestra qué conjunto de estados del AFND representa cada estado del AFD"""
        
        print("\n=== TABLA DE CONJUNTOS ===")
        print("Estado\t\tConjunto de estados del AFND")
        print("-" * 45)
        
        # Mostrar estados en orden: primero el inicial (A), luego los demás
        estados_en_orden = [self.estado_inicial]
        for estado in self.estados:
            if estado != self.estado_inicial:
                estados_en_orden.append(estado)
        
        # Mostrar cada estado
        for estado in estados_en_orden:
            letra = self.estados_a_letras[estado]
            
            # Agregar * si es estado final
            if estado in self.estados_finales:
                letra = letra + "*"
            
            # El estado ya viene como string con formato {q0,q1}
            print(f"{letra}\t\t{estado}")
