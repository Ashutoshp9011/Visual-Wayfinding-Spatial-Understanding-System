package com.ashutosh.core_navigation.graph

data class NavNode(
    val id: String,
    val x: Float, val y: Float,
    val floor: Int,
    val type: NodeType,
    val label: String? = null,
    val roomId: String? = null,
    val confidence: Float = 1f
)
