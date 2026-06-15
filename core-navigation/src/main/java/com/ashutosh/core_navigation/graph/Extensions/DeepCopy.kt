package com.ashutosh.core_navigation.graph.extensions

/**
 * Creates a deep copy of the receiver object.
 * This is typically used for Graph, Node, or Edge objects to ensure
 * structural independence during navigation path calculations.
 */
fun <T> T.deepCopy(): T {
    // TODO: Implement deep copy logic based on the specific graph model classes
    return this
}

