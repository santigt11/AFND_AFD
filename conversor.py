from afd import AFD

def convertir_afnd_a_afd(afnd):
    afd = AFD()
    
    # Estado inicial del AFD: epsilon clausura del estado inicial del AFND
    estado_inicial = afnd.epsilon_clausura([afnd.estado_inicial])
    estado_inicial_str = "{" + ",".join(sorted(estado_inicial)) + "}"
    
    afd.estados.append(estado_inicial_str)
    afd.estado_inicial = estado_inicial_str
    
    # Si contiene un estado final del AFND, es final en el AFD
    for estado in estado_inicial:
        if estado in afnd.estados_finales:
            afd.estados_finales.append(estado_inicial_str)
            break
    
    # Lista de estados por procesar
    estados_por_procesar = [estado_inicial]
    estados_procesados = []
    
    # Procesar cada estado
    for conjunto in estados_por_procesar:
        conjunto_str = "{" + ",".join(sorted(conjunto)) + "}"
        
        if conjunto in estados_procesados:
            continue
        
        estados_procesados.append(conjunto)
        
        # Para cada símbolo del alfabeto
        for simbolo in ['a', 'b']:
            # Calcular MOVER y luego epsilon clausura
            estados_mover = afnd.mover(conjunto, simbolo)
            
            if estados_mover:
                nuevo_conjunto = afnd.epsilon_clausura(estados_mover)
                nuevo_conjunto_str = "{" + ",".join(sorted(nuevo_conjunto)) + "}"
                
                # Agregar transición
                afd.agregar_transicion(conjunto_str, simbolo, nuevo_conjunto_str)
                
                # Si es un estado nuevo, agregarlo
                if nuevo_conjunto_str not in afd.estados:
                    afd.estados.append(nuevo_conjunto_str)
                    
                    # Verificar si es estado final
                    for estado in nuevo_conjunto:
                        if estado in afnd.estados_finales:
                            afd.estados_finales.append(nuevo_conjunto_str)
                            break
                
                # Si no fue procesado, agregarlo a la lista
                if nuevo_conjunto not in estados_procesados and nuevo_conjunto not in estados_por_procesar:
                    estados_por_procesar.append(nuevo_conjunto)
    
    # Asignar letras a los estados
    afd.asignar_letras()
    return afd
