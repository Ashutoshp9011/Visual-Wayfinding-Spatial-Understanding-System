package com.ashutosh.core_navigation.state

data class NavigationState(
    val currentNodeId: String? = null,
    val destinationNodeId: String? = null,
    val isNavigating: Boolean = false
)