package com.ashutosh.core_navigation.graph

data class NavEdge(
    val from: String,
    val to: String,
    val weight: Float,           // Euclidean distance
    val corridorWidth: Float = 1.5f,
    val isBidirectional: Boolean = true
)
