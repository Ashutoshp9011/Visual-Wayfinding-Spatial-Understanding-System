package com.ashutosh.core_navigation.instructions

import com.ashutosh.core_navigation.graph.NavNode
import com.ashutosh.core_navigation.graph.NodeType

fun generateInstructions(
    path: List<NavNode>
): List<String> {

    val instructions = mutableListOf<String>()

    for (i in 1 until path.size - 1) {

        val prev = path[i - 1]
        val curr = path[i]
        val next = path[i + 1]

        when (curr.type) {

            NodeType.TURN -> {

                val bearing =
                    bearing(prev, curr, next)

                instructions +=
                    if (bearing > 0)
                        "Turn right at ${curr.label ?: "junction"}"
                    else
                        "Turn left at ${curr.label ?: "junction"}"
            }

            NodeType.STAIR ->
                instructions +=
                    "Take stairs to floor ${next.floor}"

            NodeType.LIFT ->
                instructions +=
                    "Take lift to floor ${next.floor}"

            NodeType.DOOR ->
                instructions +=
                    "Go through door — ${curr.label ?: ""}"

            NodeType.LANDMARK ->
                instructions +=
                    "Pass ${curr.label}"

            else -> {}
        }
    }

    instructions +=
        "Arrive at ${path.last().label ?: "destination"}"

    return instructions
}

private fun bearing(
    a: NavNode,
    b: NavNode,
    c: NavNode
): Float {

    val v1x = b.x - a.x
    val v1y = b.y - a.y

    val v2x = c.x - b.x
    val v2y = c.y - b.y

    return v1x * v2y - v1y * v2x
}
