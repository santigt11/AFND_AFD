import os
import json

class GraficadorAutomatas:
    """Clase para generar visualizaciones de autómatas usando vis.js"""
    
    def __init__(self, ruta_base="d3"):
        self.ruta_base = ruta_base
        if not os.path.exists(self.ruta_base):
            os.makedirs(self.ruta_base)
    
    def generar_nodos_afnd(self, afnd):
        """Generar nodos para el AFND"""
        nodos = []
        estados_ordenados = sorted(list(afnd.estados))
        
        for i, estado in enumerate(estados_ordenados):
            color = "#97C2FC"  # Color azul por defecto
            
            # Estado inicial - color verde
            if estado == afnd.estado_inicial:
                color = "#7BE141"
            
            # Estado final - color rojo
            if estado in afnd.estados_finales:
                color = "#FB7E81"
            
            # Estado inicial y final - color naranja
            if estado == afnd.estado_inicial and estado in afnd.estados_finales:
                color = "#FFB347"
            
            nodo = {
                "id": i + 1,
                "label": estado,
                "color": color,
                "shape": "circle",
                "size": 30
            }
            nodos.append(nodo)
        
        return nodos, {estado: i + 1 for i, estado in enumerate(estados_ordenados)}
    
    def generar_aristas_afnd(self, afnd, mapeo_estados):
        """Generar aristas para el AFND"""
        aristas = []
        arista_id = 1
        
        for estado_origen in afnd.transiciones:
            for simbolo in afnd.transiciones[estado_origen]:
                for estado_destino in afnd.transiciones[estado_origen][simbolo]:
                    # Agregar épsilon como ε para mejor visualización
                    etiqueta = "ε" if simbolo == "ε" else simbolo
                    
                    arista = {
                        "id": arista_id,
                        "from": mapeo_estados[estado_origen],
                        "to": mapeo_estados[estado_destino],
                        "label": etiqueta,
                        "arrows": "to",
                        "color": {"color": "#2B7CE9"}
                    }
                    
                    # Color especial para transiciones épsilon
                    if simbolo == "ε":
                        arista["color"] = {"color": "#FF6B6B"}
                        arista["dashes"] = True
                    
                    aristas.append(arista)
                    arista_id += 1
        
        return aristas
    
    def generar_nodos_afd(self, afd):
        """Generar nodos para el AFD"""
        nodos = []
        
        for i, estado in enumerate(afd.estados):
            color = "#97C2FC"  # Color azul por defecto
            
            # Estado inicial - color verde
            if estado == afd.estado_inicial:
                color = "#7BE141"
            
            # Estado final - color rojo
            if estado in afd.estados_finales:
                color = "#FB7E81"
            
            # Estado inicial y final - color naranja
            if estado == afd.estado_inicial and estado in afd.estados_finales:
                color = "#FFB347"
            
            # Usar la letra asignada si existe, sino usar el estado original
            etiqueta = afd.estados_a_letras.get(estado, estado)
            if estado in afd.estados_finales:
                etiqueta += "*"
            
            nodo = {
                "id": i + 1,
                "label": etiqueta,
                "title": estado,  # Tooltip con el conjunto original
                "color": color,
                "shape": "circle",
                "size": 30
            }
            nodos.append(nodo)
        
        return nodos, {estado: i + 1 for i, estado in enumerate(afd.estados)}
    
    def generar_aristas_afd(self, afd, mapeo_estados):
        """Generar aristas para el AFD"""
        aristas = []
        arista_id = 1
        
        for estado_origen in afd.transiciones:
            for simbolo in afd.transiciones[estado_origen]:
                estado_destino = afd.transiciones[estado_origen][simbolo]
                
                arista = {
                    "id": arista_id,
                    "from": mapeo_estados[estado_origen],
                    "to": mapeo_estados[estado_destino],
                    "label": simbolo,
                    "arrows": "to",
                    "color": {"color": "#2B7CE9"}
                }
                
                aristas.append(arista)
                arista_id += 1
        
        return aristas
    
    def generar_html_automata(self, titulo, archivo_js):
        """Generar archivo HTML para visualizar un autómata"""
        html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
    <script src="vis.js"></script>
    <style type="text/css">
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }}
        #mynetwork {{
            width: 100%;
            height: 600px;
            border: 2px solid #ddd;
            border-radius: 5px;
            background-color: #fafafa;
        }}
        .legend {{
            margin-top: 20px;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 5px;
            border: 1px solid #ddd;
        }}
        .legend h3 {{
            margin-top: 0;
            color: #333;
        }}
        .legend-item {{
            display: inline-block;
            margin-right: 20px;
            margin-bottom: 10px;
        }}
        .legend-color {{
            display: inline-block;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin-right: 8px;
            vertical-align: middle;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{titulo}</h1>
        <div id="mynetwork"></div>
        
        <div class="legend">
            <h3>Leyenda:</h3>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #7BE141;"></span>
                Estado Inicial
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FB7E81;"></span>
                Estado Final
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FFB347;"></span>
                Estado Inicial y Final
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #97C2FC;"></span>
                Estado Normal
            </div>
        </div>
    </div>

    <script type="text/javascript" src="{archivo_js}"></script>
</body>
</html>"""
        return html_content
    
    def generar_js_automata(self, nodos, aristas):
        """Generar archivo JavaScript para visualizar un autómata"""
        js_content = f"""// Nodos del autómata
var nodes = new vis.DataSet({json.dumps(nodos, indent=2)});

// Aristas del autómata
var edges = new vis.DataSet({json.dumps(aristas, indent=2)});

// Configurar el contenedor y opciones
var container = document.getElementById("mynetwork");
var data = {{
    nodes: nodes,
    edges: edges,
}};

var options = {{
    nodes: {{
        font: {{
            size: 16,
            face: 'Arial',
            color: '#000000'
        }},
        borderWidth: 2,
        shadow: true
    }},
    edges: {{
        font: {{
            size: 14,
            face: 'Arial',
            color: '#000000',
            background: 'white',
            strokeWidth: 2
        }},
        width: 2,
        shadow: true,
        smooth: {{
            type: 'continuous',
            forceDirection: 'none'
        }}
    }},
    physics: {{
        enabled: true,
        stabilization: {{
            enabled: true,
            iterations: 1000,
            updateInterval: 25
        }},
        barnesHut: {{
            gravitationalConstant: -2000,
            centralGravity: 0.3,
            springLength: 95,
            springConstant: 0.04,
            damping: 0.09,
            avoidOverlap: 1
        }}
    }},
    interaction: {{
        dragNodes: true,
        dragView: true,
        zoomView: true
    }}
}};

// Crear la red
var network = new vis.Network(container, data, options);

// Ajustar vista después de la estabilización
network.once("stabilizationIterationsDone", function () {{
    network.fit();
}});
"""
        return js_content
    
    def generar_grafo_afnd(self, afnd, nombre_archivo="afnd"):
        """Generar archivos HTML y JS para visualizar el AFND"""
        nodos, mapeo = self.generar_nodos_afnd(afnd)
        aristas = self.generar_aristas_afnd(afnd, mapeo)
        
        # Generar archivos
        html_content = self.generar_html_automata("Autómata Finito No Determinista (AFND)", f"{nombre_archivo}.js")
        js_content = self.generar_js_automata(nodos, aristas)
        
        # Escribir archivos
        with open(os.path.join(self.ruta_base, f"{nombre_archivo}.html"), 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        with open(os.path.join(self.ruta_base, f"{nombre_archivo}.js"), 'w', encoding='utf-8') as f:
            f.write(js_content)
        
        print(f"✓ Grafo del AFND generado: {self.ruta_base}/{nombre_archivo}.html")
    
    def generar_grafo_afd(self, afd, nombre_archivo="afd"):
        """Generar archivos HTML y JS para visualizar el AFD"""
        nodos, mapeo = self.generar_nodos_afd(afd)
        aristas = self.generar_aristas_afd(afd, mapeo)
        
        # Generar archivos
        html_content = self.generar_html_automata("Autómata Finito Determinista (AFD)", f"{nombre_archivo}.js")
        js_content = self.generar_js_automata(nodos, aristas)
        
        # Escribir archivos
        with open(os.path.join(self.ruta_base, f"{nombre_archivo}.html"), 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        with open(os.path.join(self.ruta_base, f"{nombre_archivo}.js"), 'w', encoding='utf-8') as f:
            f.write(js_content)
        
        print(f"✓ Grafo del AFD generado: {self.ruta_base}/{nombre_archivo}.html")
    
    def generar_ambos_grafos(self, afnd, afd):
        self.generar_grafo_afnd(afnd, "afnd")
        self.generar_grafo_afd(afd, "afd")
