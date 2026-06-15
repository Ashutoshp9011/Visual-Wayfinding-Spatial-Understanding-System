package com.ashutosh.core_navigation.graph

import com.ashutosh.core_navigation.position.Coordinate
import kotlin.math.pow
import kotlin.math.sqrt

data class GraphNode(
    val id: String,
    val coordinate: Coordinate,
    val type: NodeType,
    val neighbors: List<String> = emptyList()
) {
    fun distanceTo(other: GraphNode): Double {
        return sqrt(
            (other.coordinate.x - coordinate.x).toDouble().pow(2) +
                    (other.coordinate.y - coordinate.y).toDouble().pow(2)
        )
    }
}
