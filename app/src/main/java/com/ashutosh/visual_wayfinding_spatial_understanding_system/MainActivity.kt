package com.ashutosh.visual_wayfinding_spatial_understanding_system

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.ashutosh.entrancemapping.EntranceMapper
import com.ashutosh.steptracker.StepTrackerManager
import com.ashutosh.pathdrawing.PathRenderer
import com.ashutosh.core_navigation.graph.NavigationGraph
import com.ashutosh.core_navigation.position.PositionManager
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.ashutosh.visual_wayfinding_spatial_understanding_system.ui.theme.VisualWayfindingSpatialUnderstandingSystemTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

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
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    Greeting(
                        name = "Android",
                        modifier = Modifier.padding(innerPadding)
                    )
                }
            }
        }
    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    VisualWayfindingSpatialUnderstandingSystemTheme {
        Greeting("Android")
    }
}