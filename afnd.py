class AFND:
    """Un autómata que puede estar en varios estados al mismo tiempo"""
    
    def __init__(self):
        # Lista de todos los estados
        self.estados = set()
        
        # Lista de símbolos del alfabeto (a, b, etc.)
        self.alfabeto = set()
        
        # Diccionario de transiciones: 
        # estado -> símbolo -> lista de estados destino
        self.transiciones = {}
        
        # El estado donde empieza el autómata
        self.estado_inicial = None
        
        # Los estados donde el autómata acepta la cadena
        self.estados_finales = set()
    
    def agregar_estado(self, nombre_estado):
        """Agrega un nuevo estado al autómata"""
        self.estados.add(nombre_estado)
    
    def establecer_inicial(self, nombre_estado):
        """Define cuál es el estado inicial"""
        self.estado_inicial = nombre_estado
        self.estados.add(nombre_estado)
    
    def agregar_final(self, nombre_estado):
        """Marca un estado como final (de aceptación)"""
        self.estados_finales.add(nombre_estado)
        self.estados.add(nombre_estado)
    
    def agregar_transicion(self, estado_origen, simbolo, estado_destino):
        """Agrega una transición: desde un estado, con un símbolo, a otro estado"""
        
        # Agregar los estados si no existen
        self.estados.add(estado_origen)
        self.estados.add(estado_destino)
        
        # Agregar el símbolo al alfabeto (excepto épsilon)
        if simbolo != 'ε':
            self.alfabeto.add(simbolo)
        
        # Crear la estructura de transiciones si no existe
        if estado_origen not in self.transiciones:
            self.transiciones[estado_origen] = {}
        
        if simbolo not in self.transiciones[estado_origen]:
            self.transiciones[estado_origen][simbolo] = set()
        
        # Agregar la transición
        self.transiciones[estado_origen][simbolo].add(estado_destino)
    
    def epsilon_clausura(self, lista_estados):
        """Encuentra todos los estados alcanzables con transiciones épsilon"""
        
        # Empezar con los estados dados
        resultado = set(lista_estados)
        
        # Lista de estados por revisar
        por_revisar = list(lista_estados)
        
        # Revisar cada estado
        while por_revisar:
            estado_actual = por_revisar.pop()
            
            # Si este estado tiene transiciones épsilon
            if estado_actual in self.transiciones and 'ε' in self.transiciones[estado_actual]:
                
                # Revisar cada estado alcanzable con épsilon
                for nuevo_estado in self.transiciones[estado_actual]['ε']:
                    
                    # Si no lo habíamos visitado antes
                    if nuevo_estado not in resultado:
                        resultado.add(nuevo_estado)
                        por_revisar.append(nuevo_estado)
        
        return resultado
    
    def mover(self, lista_estados, simbolo):
        """Encuentra estados alcanzables desde la lista con el símbolo dado"""
        
        resultado = set()
        
        # Para cada estado en la lista
        for estado in lista_estados:
            
            # Si el estado tiene transiciones con este símbolo
            if estado in self.transiciones and simbolo in self.transiciones[estado]:
                
                # Agregar todos los estados destino
                resultado.update(self.transiciones[estado][simbolo])
        
        return resultado
    
    def imprimir_tabla_transiciones(self):
        """Muestra la tabla de transiciones del AFND"""
        
        print("\n=== TABLA DE TRANSICIONES AFND ===")
        
        # Crear lista de símbolos incluyendo épsilon
        simbolos = sorted(list(self.alfabeto)) + ['ε']
        estados_lista = sorted(list(self.estados))
        
        # Imprimir encabezado
        encabezado = "Estado\t" + "\t".join(simbolos)
        print(encabezado)
        print("-" * (len(encabezado) + 10))
        
        # Imprimir cada estado
        for estado in estados_lista:
            
            # Nombre del estado (con * si es final)
            nombre = estado
            if estado in self.estados_finales:
                nombre = f"{estado}*"
            
            fila = [nombre]
            
            # Para cada símbolo
            for simbolo in simbolos:
                
                # Si hay transiciones con este símbolo
                if estado in self.transiciones and simbolo in self.transiciones[estado]:
                    destinos = sorted(list(self.transiciones[estado][simbolo]))
                    
                    if len(destinos) == 1:
                        fila.append(destinos[0])
                    else:
                        # Múltiples destinos
                        fila.append("{" + ",".join(destinos) + "}")
                else:
                    fila.append("∅")  # Vacío
            
            print("\t".join(fila))
