from afd import AFD

def convertir_afnd_a_afd(afnd):
    """Convierte un AFND a AFD usando el algoritmo de construcción de subconjuntos"""
    
    print("Convirtiendo AFND a AFD...")
    
    # Crear el nuevo AFD
    afd = AFD()
    
    # PASO 1: Crear el estado inicial del AFD
    # Es la épsilon-clausura del estado inicial del AFND
    estado_inicial_conjunto = afnd.epsilon_clausura([afnd.estado_inicial])
    estado_inicial_texto = "{" + ",".join(sorted(estado_inicial_conjunto)) + "}"
    
    # Agregar el estado inicial al AFD
    afd.estados.append(estado_inicial_texto)
    afd.estado_inicial = estado_inicial_texto
    
    # Si contiene un estado final del AFND, también es final en el AFD
    for estado in estado_inicial_conjunto:
        if estado in afnd.estados_finales:
            afd.estados_finales.append(estado_inicial_texto)
            break
    
    # PASO 2: Procesar todos los estados
    # Lista de conjuntos de estados que necesitamos procesar
    por_procesar = [estado_inicial_conjunto]
    
    # Lista de conjuntos ya procesados
    ya_procesados = []
    
    # Procesar cada conjunto de estados
    for conjunto_actual in por_procesar:
        
        # Si ya lo procesamos, saltarlo
        if conjunto_actual in ya_procesados:
            continue
        
        # Marcar como procesado
        ya_procesados.append(conjunto_actual)
        
        # Convertir conjunto a texto para usar como nombre del estado
        conjunto_texto = "{" + ",".join(sorted(conjunto_actual)) + "}"
        
        # PASO 3: Para cada símbolo del alfabeto
        for simbolo in ['a', 'b']:
            
            # Aplicar función MOVER
            estados_mover = afnd.mover(conjunto_actual, simbolo)
            
            # Si hay estados alcanzables
            if estados_mover:
                
                # Aplicar épsilon-clausura
                nuevo_conjunto = afnd.epsilon_clausura(estados_mover)
                nuevo_conjunto_texto = "{" + ",".join(sorted(nuevo_conjunto)) + "}"
                
                # Agregar la transición al AFD
                afd.agregar_transicion(conjunto_texto, simbolo, nuevo_conjunto_texto)
                
                # Si es un estado nuevo, agregarlo
                if nuevo_conjunto_texto not in afd.estados:
                    afd.estados.append(nuevo_conjunto_texto)
                    
                    # Verificar si debe ser estado final
                    for estado in nuevo_conjunto:
                        if estado in afnd.estados_finales:
                            afd.estados_finales.append(nuevo_conjunto_texto)
                            break
                
                # Si no fue procesado, agregarlo a la lista de pendientes
                if nuevo_conjunto not in ya_procesados and nuevo_conjunto not in por_procesar:
                    por_procesar.append(nuevo_conjunto)
    
    # PASO 4: Asignar letras a los estados del AFD
    afd.asignar_letras()
    
    print("✓ Conversión completada")
    return afd
