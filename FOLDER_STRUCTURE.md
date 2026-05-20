```
modules/
├── step-tracking/              # ✅ Step detection module
│   ├── src/
│   │   ├── __init__.py
│   │   ├── step_tracker.py     # Main StepTracker class
│   │   ├── detection/
│   │   │   ├── __init__.py
│   │   │   └── peak_detection.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── helpers.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_step_tracker.py
│   ├── requirements.txt
│   └── README.md
│
├── path-drawing/               # ✅ Path visualization module
│   ├── src/
│   │   ├── __init__.py
│   │   ├── path_drawer.py      # Main PathDrawer class
│   │   ├── rendering/
│   │   │   ├── __init__.py
│   │   │   └── renderer.py
│   │   ├── export/
│   │   │   ├── __init__.py
│   │   │   ├── svg_exporter.py
│   │   │   └── image_exporter.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── geometry.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_path_drawer.py
│   ├── requirements.txt
│   └── README.md
│
├── entrance-mapping/           # ✅ Entrance detection module
│   ├── src/
│   │   ├── __init__.py
│   │   ├── entrance_mapper.py   # Main EntranceMapper class
│   │   ├── detection/
│   │   │   ├── __init__.py
│   │   │   └── entrance_detector.py
│   │   ├── classification/
│   │   │   ├── __init__.py
│   │   │   └── entrance_classifier.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── image_utils.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_entrance_mapper.py
│   ├── requirements.txt
│   └── README.md
│
└── __init__.py

shared/                        # ✅ Shared resources
├── __init__.py
├── constants.py              # Shared constants
├── config.py                 # Configuration
└── data_models.py            # Common data structures
```
