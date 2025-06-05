var nodes = new vis.DataSet([
{id: 1, label: "A", color: "lightgreen"},
{id: 2, label: "B", color: "lightblue"},
{id: 3, label: "C", color: "lightblue"},
{id: 4, label: "D", color: "lightblue"},
{id: 5, label: "E*", color: "lightcoral"},
]);

var edges = new vis.DataSet([
{from: 1, to: 2, label: "a", arrows: "to"},
{from: 1, to: 3, label: "b", arrows: "to"},
{from: 2, to: 2, label: "a", arrows: "to"},
{from: 2, to: 4, label: "b", arrows: "to"},
{from: 3, to: 2, label: "a", arrows: "to"},
{from: 3, to: 3, label: "b", arrows: "to"},
{from: 4, to: 2, label: "a", arrows: "to"},
{from: 4, to: 5, label: "b", arrows: "to"},
{from: 5, to: 2, label: "a", arrows: "to"},
{from: 5, to: 3, label: "b", arrows: "to"},
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
