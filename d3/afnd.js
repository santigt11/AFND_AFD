var nodes = new vis.DataSet([
{id: 1, label: "q0", color: "lightgreen"},
{id: 2, label: "q1", color: "lightblue"},
{id: 3, label: "q10", color: "lightcoral"},
{id: 4, label: "q2", color: "lightblue"},
{id: 5, label: "q3", color: "lightblue"},
{id: 6, label: "q4", color: "lightblue"},
{id: 7, label: "q5", color: "lightblue"},
{id: 8, label: "q6", color: "lightblue"},
{id: 9, label: "q7", color: "lightblue"},
{id: 10, label: "q8", color: "lightblue"},
{id: 11, label: "q9", color: "lightblue"},
]);

var edges = new vis.DataSet([
{from: 1, to: 9, label: "ε", arrows: "to"},
{from: 1, to: 2, label: "ε", arrows: "to"},
{from: 2, to: 4, label: "ε", arrows: "to"},
{from: 2, to: 6, label: "ε", arrows: "to"},
{from: 4, to: 5, label: "a", arrows: "to"},
{from: 6, to: 7, label: "b", arrows: "to"},
{from: 7, to: 8, label: "ε", arrows: "to"},
{from: 8, to: 9, label: "ε", arrows: "to"},
{from: 8, to: 2, label: "ε", arrows: "to"},
{from: 9, to: 10, label: "a", arrows: "to"},
{from: 10, to: 11, label: "b", arrows: "to"},
{from: 11, to: 3, label: "b", arrows: "to"},
{from: 5, to: 8, label: "ε", arrows: "to"},
]);

var container = document.getElementById("mynetwork");
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
