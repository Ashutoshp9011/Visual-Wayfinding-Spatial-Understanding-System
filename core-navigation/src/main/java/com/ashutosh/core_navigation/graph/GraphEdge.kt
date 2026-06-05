package com.ashutosh.core_navigation.graph

data class GraphEdge(
    val fromNodeId: String,
    val toNodeId: String,
    val distance: Float
)