// Nodos del autómata
var nodes = new vis.DataSet([
  {
    "id": 1,
    "label": "q0",
    "color": "#7BE141",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 2,
    "label": "q1",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 3,
    "label": "q10",
    "color": "#FB7E81",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 4,
    "label": "q2",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 5,
    "label": "q3",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 6,
    "label": "q4",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 7,
    "label": "q5",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 8,
    "label": "q6",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 9,
    "label": "q7",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 10,
    "label": "q8",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 11,
    "label": "q9",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  }
]);

// Aristas del autómata
var edges = new vis.DataSet([
  {
    "id": 1,
    "from": 1,
    "to": 9,
    "label": "\u03b5",
    "arrows": "to",
    "color": {
      "color": "#FF6B6B"
    },
    "dashes": true
  },
  {
    "id": 2,
    "from": 1,
    "to": 2,
    "label": "\u03b5",
    "arrows": "to",
    "color": {
      "color": "#FF6B6B"
    },
    "dashes": true
  },
  {
    "id": 3,
    "from": 2,
    "to": 4,
    "label": "\u03b5",
    "arrows": "to",
    "color": {
      "color": "#FF6B6B"
    },
    "dashes": true
  },
  {
    "id": 4,
    "from": 2,
    "to": 6,
    "label": "\u03b5",
    "arrows": "to",
    "color": {
      "color": "#FF6B6B"
    },
    "dashes": true
  },
  {
    "id": 5,
    "from": 4,
    "to": 5,
    "label": "a",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 6,
    "from": 6,
    "to": 7,
    "label": "b",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 7,
    "from": 7,
    "to": 8,
    "label": "\u03b5",
    "arrows": "to",
    "color": {
      "color": "#FF6B6B"
    },
    "dashes": true
  },
  {
    "id": 8,
    "from": 8,
    "to": 9,
    "label": "\u03b5",
    "arrows": "to",
    "color": {
      "color": "#FF6B6B"
    },
    "dashes": true
  },
  {
    "id": 9,
    "from": 8,
    "to": 2,
    "label": "\u03b5",
    "arrows": "to",
    "color": {
      "color": "#FF6B6B"
    },
    "dashes": true
  },
  {
    "id": 10,
    "from": 9,
    "to": 10,
    "label": "a",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 11,
    "from": 10,
    "to": 11,
    "label": "b",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 12,
    "from": 11,
    "to": 3,
    "label": "b",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 13,
    "from": 5,
    "to": 8,
    "label": "\u03b5",
    "arrows": "to",
    "color": {
      "color": "#FF6B6B"
    },
    "dashes": true
  }
]);

// Configurar el contenedor y opciones
var container = document.getElementById("mynetwork");
var data = {
    nodes: nodes,
    edges: edges,
};

var options = {
    nodes: {
        font: {
            size: 16,
            face: 'Arial',
            color: '#000000'
        },
        borderWidth: 2,
        shadow: true
    },
    edges: {
        font: {
            size: 14,
            face: 'Arial',
            color: '#000000',
            background: 'white',
            strokeWidth: 2
        },
        width: 2,
        shadow: true,
        smooth: {
            type: 'continuous',
            forceDirection: 'none'
        }
    },
    physics: {
        enabled: true,
        stabilization: {
            enabled: true,
            iterations: 1000,
            updateInterval: 25
        },
        barnesHut: {
            gravitationalConstant: -2000,
            centralGravity: 0.3,
            springLength: 95,
            springConstant: 0.04,
            damping: 0.09,
            avoidOverlap: 1
        }
    },
    interaction: {
        dragNodes: true,
        dragView: true,
        zoomView: true
    }
};

// Crear la red
var network = new vis.Network(container, data, options);

// Ajustar vista después de la estabilización
network.once("stabilizationIterationsDone", function () {
    network.fit();
});
