package com.ashutosh.entrance_mapping

import com.ashutosh.core_navigation.graph.GraphNode
import com.ashutosh.core_navigation.graph.NodeType
import com.ashutosh.core_navigation.position.Coordinate

class EntranceMapper {
    fun createEntranceNode(): GraphNode {
        return GraphNode(
            id = "entrance_1",
            coordinate = Coordinate(0f, 0f),
            type = NodeType.ENTRANCE
        )
    }
}
