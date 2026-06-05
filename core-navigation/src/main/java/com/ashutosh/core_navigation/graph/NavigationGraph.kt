package com.ashutosh.core_navigation.graph

class NavigationGraph {

    private val nodes = mutableListOf<GraphNode>()
    private val edges = mutableListOf<GraphEdge>()

    fun addNode(node: GraphNode) {
        nodes.add(node)
    }

    fun addEdge(edge: GraphEdge) {
        edges.add(edge)
    }

    fun getNodes(): List<GraphNode> = nodes

    fun getEdges(): List<GraphEdge> = edges
}