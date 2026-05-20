"""
Entrance Classification - Classifies detected entrances by type
"""

import numpy as np
from typing import Dict, List


class EntranceClassifier:
    """
    Classifies detected entrances into categories:
    - main_entrance
    - emergency_exit
    - accessible_entrance
    - regular_door
    - service_entrance
    """
    
    def __init__(self):
        """
        Initialize EntranceClassifier.
        """
        self.entrance_types = [
            'main_entrance',
            'emergency_exit',
            'accessible_entrance',
            'regular_door',
            'service_entrance'
        ]
    
    def classify(self, detection: Dict) -> str:
        """
        Classify a detected entrance.
        
        Args:
            detection (Dict): Detection information
            
        Returns:
            str: Entrance type classification
        """
        # Extract features
        aspect_ratio = detection.get('aspect_ratio', 1.5)
        area = detection.get('area', 0)
        width = detection.get('width', 0)
        
        # Simple classification heuristics
        # TODO: Replace with machine learning model
        
        if aspect_ratio > 2.5:
            return 'emergency_exit'
        elif width > 150:  # Wide entrance
            return 'main_entrance'
        elif area < 5000:  # Small area
            return 'service_entrance'
        else:
            return 'regular_door'
    
    def classify_with_confidence(self, detection: Dict) -> tuple:
        """
        Classify entrance and return confidence scores.
        
        Args:
            detection (Dict): Detection information
            
        Returns:
            tuple: (classification, confidence_scores)
        """
        entrance_type = self.classify(detection)
        
        # Calculate confidence scores for each class
        confidences = self._calculate_confidences(detection)
        
        return entrance_type, confidences
    
    def _calculate_confidences(self, detection: Dict) -> Dict[str, float]:
        """
        Calculate confidence scores for each entrance type.
        
        Args:
            detection (Dict): Detection information
            
        Returns:
            Dict: Confidence scores by type
        """
        aspect_ratio = detection.get('aspect_ratio', 1.5)
        area = detection.get('area', 0)
        width = detection.get('width', 0)
        base_conf = detection.get('confidence', 0.5)
        
        confidences = {
            'main_entrance': base_conf * (1.0 if width > 150 else 0.5),
            'emergency_exit': base_conf * (1.0 if aspect_ratio > 2.5 else 0.3),
            'accessible_entrance': base_conf * 0.6,
            'regular_door': base_conf * 0.8,
            'service_entrance': base_conf * (1.0 if area < 5000 else 0.4)
        }
        
        return confidences