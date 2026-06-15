package com.ashutosh.core_navigation.graph

import android.graphics.RectF

data class RoomModel(
    val id: String,
    val number: String,
    val type: RoomType,          // ROOM, LAB, WASHROOM, HALL, etc.
    val side: Side,              // LEFT, RIGHT
    val floor: Int,
    val boundingBox: RectF,
    val ocrConfidence: Float,
    val doorNodeId: String
)
