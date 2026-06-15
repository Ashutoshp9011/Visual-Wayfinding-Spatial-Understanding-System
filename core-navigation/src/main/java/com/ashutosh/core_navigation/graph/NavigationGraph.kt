package com.ashutosh.core_navigation.graph

data class NavigationGraph(
    val nodes: MutableMap<String, NavNode> = mutableMapOf(),
    val edges: MutableList<NavEdge> = mutableListOf(),
    val rooms: MutableMap<String, RoomModel> = mutableMapOf(),
    val floors: Int = 1
) {
    fun addNode(node: NavNode) {
        nodes[node.id] = node
    }

    fun addEdge(edge: NavEdge) {
        edges.add(edge)
    }

    fun addRoom(room: RoomModel) {
        rooms[room.id] = room
    }
}
