package com.ashutosh.step_tracking

import com.ashutosh.core_navigation.position.PositionManager

class StepTrackerManager(private val positionManager: PositionManager) {
    fun onStepDetected(stepLength: Float, angle: Float) {
        // Implementation for step detection logic
    }
}
