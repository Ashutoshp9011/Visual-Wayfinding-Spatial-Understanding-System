package com.ashutosh.visual_wayfinding_spatial_understanding_system

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp

import com.ashutosh.entrance_mapping.EntranceMapper
import com.ashutosh.step_tracking.StepTrackerManager
import com.ashutosh.path_drawing.PathRenderer
import com.ashutosh.core_navigation.graph.NavigationGraph
import com.ashutosh.core_navigation.position.PositionManager

import com.ashutosh.visual_wayfinding_spatial_understanding_system.ui.theme.VisualWayfindingSpatialUnderstandingSystemTheme

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Initialize Navigation System
        val graph = NavigationGraph()

        val entranceMapper = EntranceMapper()
        val entranceNode = entranceMapper.createEntranceNode()
        graph.addNode(entranceNode)

        val positionManager = PositionManager()

        val tracker = StepTrackerManager(positionManager)
        tracker.onStepDetected(5f, 10f)

        val renderer = PathRenderer()
        renderer.draw(graph)

        enableEdgeToEdge()

        setContent {
            VisualWayfindingSpatialUnderstandingSystemTheme {
                VisualWayfindingApp()
            }
        }
    }
}

@Composable
fun VisualWayfindingApp() {

    Scaffold(
        modifier = Modifier.fillMaxSize()
    ) { innerPadding ->

        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
                .padding(16.dp)
        ) {

            Text(
                text = "Visual Wayfinding & Spatial Understanding System",
                style = MaterialTheme.typography.headlineSmall
            )

            Spacer(modifier = Modifier.height(20.dp))

            Text("✓ Entrance Mapping Initialized")
            Text("✓ Navigation Graph Loaded")
            Text("✓ Step Tracking Active")
            Text("✓ Position Manager Running")
            Text("✓ Path Renderer Ready")

            Spacer(modifier = Modifier.height(20.dp))

            Button(
                onClick = {
                    // Future navigation action
                }
            ) {
                Text("Start Navigation")
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun PreviewApp() {
    VisualWayfindingSpatialUnderstandingSystemTheme {
        VisualWayfindingApp()
    }
}