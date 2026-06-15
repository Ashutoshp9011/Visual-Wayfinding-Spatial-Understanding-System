package com.ashutosh.core_navigation.graph.extensions

import com.ashutosh.core_navigation.graph.NavEdge
import com.ashutosh.core_navigation.graph.NavNode
import com.ashutosh.core_navigation.graph.NavigationGraph

fun NavigationGraph.edgesFrom(nodeId: String): List<NavEdge> {
    return edges.filter {
        it.from == nodeId || it.to == nodeId
    }
}

fun NavigationGraph.findNodeById(nodeId: String): NavNode? {
    return nodes[nodeId]
}

fun NavigationGraph.neighborsOf(nodeId: String): List<NavNode> {
    val connectedNodeIds = edgesFrom(nodeId).map { if (it.from == nodeId) it.to else it.from }
    return connectedNodeIds.mapNotNull { nodes[it] }
}
