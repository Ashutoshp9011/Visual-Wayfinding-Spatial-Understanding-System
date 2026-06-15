package com.ashutosh.entrance_mapping

import com.ashutosh.core_navigation.graph.NavNode
import com.ashutosh.core_navigation.graph.NodeType
import com.ashutosh.core_navigation.position.Coordinate

class EntranceMapper {
    fun createEntranceNode(): NavNode {
        val coord = Coordinate(0f, 0f)
        return NavNode(
            id = "entrance_1",
            x = coord.x,
            y = coord.y,
            floor = 0,
            type = NodeType.ENTRANCE
        )
    }
}
