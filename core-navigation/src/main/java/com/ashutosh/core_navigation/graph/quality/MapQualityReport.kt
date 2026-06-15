package com.ashutosh.core_navigation.graph.quality

import com.ashutosh.core_navigation.graph.NavigationGraph

data class MapQualityReport(
    val score: Float,           // 0–100
    val nodeCount: Int,
    val disconnectedNodes: Int,
    val ocrAvgConfidence: Float,
    val issues: List<String>
)

fun NavigationGraph.qualityReport(): MapQualityReport {
    val issues = mutableListOf<String>()
    val disconnected = nodes.keys.count { id -> edges.none { it.from == id || it.to == id } }
    if (disconnected > 0) issues += "$disconnected isolated nodes"

    val unlabeledNodes = nodes.values.count { it.label.isNullOrBlank() }
    if (unlabeledNodes > 0) issues += "$unlabeledNodes nodes missing labels"

    val avgOcr = rooms.values.map { it.ocrConfidence }.average().toFloat()
    if (avgOcr < 0.7f) issues += "Low OCR confidence (${(avgOcr*100).toInt()}%)"

    val score = 100f - (disconnected * 10f) - (unlabeledNodes * 2f) - (( 1f - avgOcr) * 30f)
    return MapQualityReport(score.coerceIn(0f, 100f), nodes.size, disconnected, avgOcr, issues)
}