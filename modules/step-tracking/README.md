# Step Tracking Module

Real-time step detection and tracking for indoor navigation systems.

## Overview

The Step Tracking module detects and tracks user steps to provide accurate stride measurements and distance calculations for indoor wayfinding applications.

## Features

- **Real-time step detection** from motion sensors
- **Stride length calculation** and personalization
- **Step counting and validation**
- **Movement pattern analysis**
- **Data smoothing and filtering**

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from src.step_tracker import StepTracker

# Initialize tracker
tracker = StepTracker(stride_length=0.75)

# Process sensor data
steps_detected = tracker.detect_steps(accelerometer_data)

# Get statistics
stats = tracker.get_statistics()
print(f"Total steps: {stats['total_steps']}")
print(f"Distance traveled: {stats['distance']:.2f}m")
```

## API Reference

### StepTracker Class

- `detect_steps(data)` - Detect steps from sensor data
- `get_step_count()` - Get total step count
- `get_distance()` - Calculate distance traveled
- `calibrate_stride(distance, steps)` - Calibrate stride length
- `reset()` - Reset tracker state

## Testing

```bash
pytest tests/
```

## License

See LICENSE file in root directory.