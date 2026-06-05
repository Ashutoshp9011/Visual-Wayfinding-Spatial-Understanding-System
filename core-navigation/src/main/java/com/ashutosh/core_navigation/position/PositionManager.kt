package com.ashutosh.core_navigation.position

class PositionManager {

    private var currentPosition: Coordinate? = null

    fun updatePosition(position: Coordinate) {
        currentPosition = position
    }

    fun getCurrentPosition(): Coordinate? {
        return currentPosition
    }

    fun clear() {
        currentPosition = null
    }
}