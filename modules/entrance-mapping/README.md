# Entrance Mapping Module

Automated detection and classification of entrances in indoor environments.

## Overview

The Entrance Mapping module detects doors, entrances, and exits from visual data, classifies them by type (main entrance, emergency exit, accessible entrance, etc.), and provides location information for navigation.

## Features

- **Automatic entrance detection** from images/video
- **Entrance classification** (main, emergency, accessible, etc.)
- **Location mapping** with coordinates
- **Accessibility analysis** (wheelchair accessible, etc.)
- **Confidence scoring** for detections

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from src.entrance_mapper import EntranceMapper

# Initialize mapper
mapper = EntranceMapper()

# Detect entrances from image
entrances = mapper.detect_from_image('corridor.jpg')

# Get entrance details
for entrance in entrances:
    print(f"Type: {entrance['type']}")
    print(f"Location: {entrance['location']}")
    print(f"Accessible: {entrance['accessible']}")
```

## API Reference

### EntranceMapper Class

- `detect_from_image(image_path)` - Detect entrances from image
- `detect_from_frame(frame)` - Detect entrances from video frame
- `classify_entrance(detection)` - Classify detected entrance
- `get_entrance_features(detection)` - Extract entrance features
- `reset()` - Reset mapper state

## Testing

```bash
pytest tests/
```

## License

See LICENSE file in root directory.