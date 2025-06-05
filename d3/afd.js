// Nodos del autómata
var nodes = new vis.DataSet([
  {
    "id": 1,
    "label": "A",
    "title": "{q0,q1,q2,q4,q7}",
    "color": "#7BE141",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 2,
    "label": "B",
    "title": "{q1,q2,q3,q4,q6,q7,q8}",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 3,
    "label": "C",
    "title": "{q1,q2,q4,q5,q6,q7}",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 4,
    "label": "D",
    "title": "{q1,q2,q4,q5,q6,q7,q9}",
    "color": "#97C2FC",
    "shape": "circle",
    "size": 30
  },
  {
    "id": 5,
    "label": "E*",
    "title": "{q1,q10,q2,q4,q5,q6,q7}",
    "color": "#FB7E81",
    "shape": "circle",
    "size": 30
  }
]);

// Aristas del autómata
var edges = new vis.DataSet([
  {
    "id": 1,
    "from": 1,
    "to": 2,
    "label": "a",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 2,
    "from": 1,
    "to": 3,
    "label": "b",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 3,
    "from": 2,
    "to": 2,
    "label": "a",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 4,
    "from": 2,
    "to": 4,
    "label": "b",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 5,
    "from": 3,
    "to": 2,
    "label": "a",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 6,
    "from": 3,
    "to": 3,
    "label": "b",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 7,
    "from": 4,
    "to": 2,
    "label": "a",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 8,
    "from": 4,
    "to": 5,
    "label": "b",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 9,
    "from": 5,
    "to": 2,
    "label": "a",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
  },
  {
    "id": 10,
    "from": 5,
    "to": 3,
    "label": "b",
    "arrows": "to",
    "color": {
      "color": "#2B7CE9"
    }
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
