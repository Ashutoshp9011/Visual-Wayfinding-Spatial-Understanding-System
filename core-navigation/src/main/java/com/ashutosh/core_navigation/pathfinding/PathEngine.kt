package com.ashutosh.core_navigation.pathfinding

import com.ashutosh.core_navigation.graph.NavNode
import com.ashutosh.core_navigation.graph.NavigationGraph
import com.ashutosh.core_navigation.graph.extensions.edgesFrom
import java.util.PriorityQueue
import kotlin.math.abs
import kotlin.math.hypot

class PathEngine(private val graph: NavigationGraph) {

    fun findPath(startId: String, goalId: String): List<NavNode> {
        val open = PriorityQueue<State>(compareBy { it.f })
        val gScore = mutableMapOf(startId to 0f)
        val parent = mutableMapOf<String, String>()
        open.add(State(startId, heuristic(startId, goalId)))

        while (open.isNotEmpty()) {
            val curr = open.poll()!!
            if (curr.id == goalId) return reconstruct(parent, goalId)
            
            for (edge in graph.edgesFrom(curr.id)) {
                val neighbor = if (edge.from == curr.id) edge.to else edge.from
                val g = gScore.getOrDefault(curr.id, Float.MAX_VALUE) + edge.weight
                if (g < gScore.getOrDefault(neighbor, Float.MAX_VALUE)) {
                    gScore[neighbor] = g
                    parent[neighbor] = curr.id
                    open.add(State(neighbor, g + heuristic(neighbor, goalId)))
                }
            }
        }
        return emptyList()
    }

    private fun reconstruct(parent: Map<String, String>, goalId: String): List<NavNode> {
        val path = mutableListOf<NavNode>()
        var curr: String? = goalId
        while (curr != null) {
            graph.nodes[curr]?.let { path.add(0, it) }
            curr = parent[curr]
        }
        return path
    }

    private fun heuristic(a: String, b: String): Float {
        val na = graph.nodes[a] ?: return 0f
        val nb = graph.nodes[b] ?: return 0f
        // Manhattan on same floor, add floor penalty for stairs/lift
        val floorPenalty = abs(na.floor - nb.floor) * 50f
        return hypot((na.x - nb.x).toDouble(), (na.y - nb.y).toDouble()).toFloat() + floorPenalty
    }
}

data class State(val id: String, val f: Float)
