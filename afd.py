class AFD:
    def __init__(self):
        self.estados = []
        self.transiciones = {}
        self.estado_inicial = ""
        self.estados_finales = []
        self.estados_a_letras = {}
    
    def agregar_transicion(self, origen, simbolo, destino):
        # Crear la clave si no existe
        if origen not in self.transiciones:
            self.transiciones[origen] = {}
        
        # Agregar la transición
        self.transiciones[origen][simbolo] = destino
    
    def asignar_letras(self):
        # Asignar letras A, B, C, D... a los estados
        # El estado inicial siempre debe ser A
        if self.estado_inicial in self.estados:
            self.estados_a_letras[self.estado_inicial] = 'A'
        
        letra_actual = 1  # B, C, D...
        for estado in self.estados:
            if estado != self.estado_inicial:
                self.estados_a_letras[estado] = chr(ord('A') + letra_actual)
                letra_actual += 1
    
    def mostrar_tabla(self):
        print("\n=== TABLA DE TRANSICIONES AFD ===")
        print("Estado\ta\tb")
        print("-" * 20)
        
        # Mostrar estados en orden: primero el inicial (A), luego los demás
        estados_ordenados = [self.estado_inicial] + [e for e in self.estados if e != self.estado_inicial]
        
        for estado in estados_ordenados:
            letra = self.estados_a_letras[estado]
            linea = letra
            
            # Marcar estados finales con *
            if estado in self.estados_finales:
                linea += "*"
            linea += "\t"
            
            # Columna 'a'
            if estado in self.transiciones and 'a' in self.transiciones[estado]:
                destino = self.transiciones[estado]['a']
                linea += self.estados_a_letras[destino]
            else:
                linea += "∅"
            linea += "\t"
            
            # Columna 'b'
            if estado in self.transiciones and 'b' in self.transiciones[estado]:
                destino = self.transiciones[estado]['b']
                linea += self.estados_a_letras[destino]
            else:
                linea += "∅"
            
            print(linea)
    
    def mostrar_conjuntos(self):
        print("\n=== TABLA DE CONJUNTOS ===")
        print("Estado\t\tConjunto de estados del AFND")
        print("-" * 45)
        
        # Mostrar estados en orden: primero el inicial (A), luego los demás
        estados_ordenados = [self.estado_inicial] + [e for e in self.estados if e != self.estado_inicial]
        
        for estado in estados_ordenados:
            letra = self.estados_a_letras[estado]
            
            # Marcar estados finales con *
            if estado in self.estados_finales:
                letra += "*"
              # El estado ya viene como string con formato {q0,q1}
            print(f"{letra}\t\t{estado}")
