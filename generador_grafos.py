def crear_grafo_afnd(afnd):
    """Crea un grafo del AFND de manera simple"""
    print("Creando grafo del AFND...")
    
    # Lista de nodos (círculos del grafo)
    nodos = []
    
    # Convertir estados a lista ordenada
    lista_estados = sorted(list(afnd.estados))
    
    # Crear cada nodo
    contador = 1
    for estado in lista_estados:
        # Decidir el color del nodo
        color = "lightblue"  # Color normal
        
        if estado == afnd.estado_inicial:
            color = "lightgreen"  # Estado inicial en verde
        
        if estado in afnd.estados_finales:
            color = "lightcoral"  # Estado final en rojo
        
        # Crear el nodo
        nodo = {
            "id": contador,
            "label": estado,
            "color": color
        }
        nodos.append(nodo)
        contador = contador + 1
    
    # Lista de conexiones (flechas del grafo)
    conexiones = []
    
    # Mapear estados a números
    estado_a_numero = {}
    for i, estado in enumerate(lista_estados):
        estado_a_numero[estado] = i + 1
    
    # Crear cada conexión
    for estado_origen in afnd.transiciones:
        for simbolo in afnd.transiciones[estado_origen]:
            for estado_destino in afnd.transiciones[estado_origen][simbolo]:
                # Crear la conexión
                conexion = {
                    "from": estado_a_numero[estado_origen],
                    "to": estado_a_numero[estado_destino],
                    "label": simbolo if simbolo != 'ε' else "ε"
                }
                conexiones.append(conexion)
    
    # Crear el archivo JavaScript
    crear_archivo_js("d3/afnd.js", nodos, conexiones)
    
    # Crear el archivo HTML
    crear_archivo_html("d3/afnd.html", "afnd.js", "AFND - Automata No Determinista")
    
    print("✓ Grafo del AFND creado: d3/afnd.html")


def crear_grafo_afd(afd):
    """Crea un grafo del AFD de manera simple"""
    print("Creando grafo del AFD...")
    
    # Lista de nodos (círculos del grafo)
    nodos = []
    
    # Crear cada nodo
    for i, estado in enumerate(afd.estados):
        # Decidir el color del nodo
        color = "lightblue"  # Color normal
        
        if estado == afd.estado_inicial:
            color = "lightgreen"  # Estado inicial en verde
        
        if estado in afd.estados_finales:
            color = "lightcoral"  # Estado final en rojo
        
        # Usar la letra asignada
        etiqueta = afd.estados_a_letras.get(estado, estado)
        if estado in afd.estados_finales:
            etiqueta = etiqueta + "*"
        
        # Crear el nodo
        nodo = {
            "id": i + 1,
            "label": etiqueta,
            "color": color
        }
        nodos.append(nodo)
    
    # Lista de conexiones (flechas del grafo)
    conexiones = []
    
    # Mapear estados a números
    estado_a_numero = {}
    for i, estado in enumerate(afd.estados):
        estado_a_numero[estado] = i + 1
    
    # Crear cada conexión
    for estado_origen in afd.transiciones:
        for simbolo in afd.transiciones[estado_origen]:
            estado_destino = afd.transiciones[estado_origen][simbolo]
            
            # Crear la conexión
            conexion = {
                "from": estado_a_numero[estado_origen],
                "to": estado_a_numero[estado_destino],
                "label": simbolo
            }
            conexiones.append(conexion)
    
    # Crear el archivo JavaScript
    crear_archivo_js("d3/afd.js", nodos, conexiones)
    
    # Crear el archivo HTML
    crear_archivo_html("d3/afd.html", "afd.js", "AFD - Automata Determinista")
    
    print("✓ Grafo del AFD creado: d3/afd.html")


def crear_archivo_js(nombre_archivo, nodos, conexiones):
    """Crea el archivo JavaScript con los datos del grafo"""
    
    # Convertir nodos a texto
    texto_nodos = "var nodes = new vis.DataSet([\n"
    for nodo in nodos:
        texto_nodos += f'{{id: {nodo["id"]}, label: "{nodo["label"]}", color: "{nodo["color"]}"}},\n'
    texto_nodos += "]);\n\n"
    
    # Convertir conexiones a texto
    texto_conexiones = "var edges = new vis.DataSet([\n"
    for conexion in conexiones:
        texto_conexiones += f'{{from: {conexion["from"]}, to: {conexion["to"]}, label: "{conexion["label"]}", arrows: "to"}},\n'
    texto_conexiones += "]);\n\n"
    
    # Crear el código completo
    codigo_js = texto_nodos + texto_conexiones + """var container = document.getElementById("mynetwork");
var data = {
    nodes: nodes,
    edges: edges,
};
var options = {
    nodes: {
        shape: "circle",
        size: 30,
        font: {
            size: 16
        }
    },
    edges: {
        width: 2,
        font: {
            size: 14
        }
    },
    physics: {
        enabled: true,
        barnesHut: {
            springLength: 200
        }
    }
};
var network = new vis.Network(container, data, options);
"""
    
    # Escribir el archivo
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(codigo_js)


def crear_archivo_html(nombre_archivo, archivo_js, titulo):
    """Crea el archivo HTML para mostrar el grafo"""
    
    codigo_html = f"""<!DOCTYPE html>
<html>
<head>
    <title>{titulo}</title>
    <script src="vis.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1 {{
            text-align: center;
            color: #333;
        }}
        #mynetwork {{
            width: 800px;
            height: 600px;
            border: 1px solid lightgray;
            margin: 0 auto;
        }}
        .info {{
            text-align: center;
            margin: 20px;
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <h1>{titulo}</h1>
    <div class="info">
        <strong>Verde:</strong> Estado inicial | 
        <strong>Rojo:</strong> Estado final | 
        <strong>Azul:</strong> Estado normal
    </div>
    <div id="mynetwork"></div>
    <script src="{archivo_js}"></script>
</body>
</html>"""
    
    # Escribir el archivo
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(codigo_html)


def crear_ambos_grafos(afnd, afd):
    """Crea los grafos de ambos autómatas"""
    print("\n=== CREANDO GRAFOS ===")
    
    # Crear carpeta si no existe
    import os
    if not os.path.exists("d3"):
        os.makedirs("d3")
    
    # Crear los grafos
    crear_grafo_afnd(afnd)
    crear_grafo_afd(afd)
    
    print("\n✓ ¡Grafos creados exitosamente!")
    print("✓ Abre los archivos .html en tu navegador para ver los grafos")
