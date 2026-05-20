"""
Entrance Mapper - Main class for entrance detection and mapping
"""

import numpy as np
from typing import List, Dict, Tuple, Optional
import cv2
from .detection.entrance_detector import EntranceDetector
from .classification.entrance_classifier import EntranceClassifier
from .utils.image_utils import load_image, resize_image


class EntranceMapper:
    """
    Detects and maps entrances in indoor environments.
    
    Combines detection and classification to identify doors, entrances,
    and exits with accessibility information.
    """
    
    def __init__(self, model_path: Optional[str] = None):
        """
        Initialize EntranceMapper.
        
        Args:
            model_path (str): Path to pre-trained model (optional)
        """
        self.detector = EntranceDetector()
        self.classifier = EntranceClassifier()
        self.detected_entrances = []
        self.model_path = model_path
    
    def detect_from_image(self, image_path: str, confidence_threshold: float = 0.5) -> List[Dict]:
        """
        Detect entrances from an image file.
        
        Args:
            image_path (str): Path to image file
            confidence_threshold (float): Minimum confidence score
            
        Returns:
            List[Dict]: List of detected entrances with details
        """
        # Load image
        image = load_image(image_path)
        if image is None:
            return []
        
        # Detect entrance regions
        detections = self.detector.detect(image)
        
        # Classify and extract features
        entrances = []
        for detection in detections:
            if detection['confidence'] >= confidence_threshold:
                entrance_info = self._process_detection(detection, image)
                entrances.append(entrance_info)
        
        self.detected_entrances = entrances
        return entrances
    
    def detect_from_frame(self, frame: np.ndarray, confidence_threshold: float = 0.5) -> List[Dict]:
        """
        Detect entrances from a video frame.
        
        Args:
            frame (np.ndarray): Video frame (BGR or RGB)
            confidence_threshold (float): Minimum confidence score
            
        Returns:
            List[Dict]: List of detected entrances
        """
        # Detect entrance regions
        detections = self.detector.detect(frame)
        
        # Classify and extract features
        entrances = []
        for detection in detections:
            if detection['confidence'] >= confidence_threshold:
                entrance_info = self._process_detection(detection, frame)
                entrances.append(entrance_info)
        
        return entrances
    
    def classify_entrance(self, detection: Dict) -> str:
        """
        Classify a detected entrance.
        
        Args:
            detection (Dict): Detection information
            
        Returns:
            str: Entrance classification
        """
        return self.classifier.classify(detection)
    
    def get_entrance_features(self, detection: Dict) -> Dict[str, any]:
        """
        Extract features from detected entrance.
        
        Args:
            detection (Dict): Detection information
            
        Returns:
            Dict: Extracted features
        """
        features = {
            'bounding_box': detection.get('bbox'),
            'center': detection.get('center'),
            'width': detection.get('width'),
            'height': detection.get('height'),
            'area': detection.get('area'),
            'color_histogram': detection.get('histogram'),
            'edges': detection.get('edges')
        }
        return features
    
    def _process_detection(self, detection: Dict, image: np.ndarray) -> Dict:
        """
        Process a single detection and extract all information.
        
        Args:
            detection (Dict): Raw detection data
            image (np.ndarray): Original image
            
        Returns:
            Dict: Processed entrance information
        """
        entrance_type = self.classifier.classify(detection)
        
        entrance_info = {
            'type': entrance_type,
            'location': detection.get('center'),
            'bbox': detection.get('bbox'),
            'confidence': detection.get('confidence'),
            'accessible': self._check_accessibility(detection),
            'features': self.get_entrance_features(detection)
        }
        
        return entrance_info
    
    def _check_accessibility(self, detection: Dict) -> bool:
        """
        Check if entrance appears to be wheelchair accessible.
        
        Args:
            detection (Dict): Detection information
            
        Returns:
            bool: True if appears accessible
        """
        # TODO: Implement accessibility detection
        # Check for ramps, automatic doors, width, etc.
        width = detection.get('width', 0)
        return width >= 0.9  # Minimum 0.9m for wheelchair access
    
    def get_detected_entrances(self) -> List[Dict]:
        """
        Get all detected entrances from last detection.
        
        Returns:
            List[Dict]: List of detected entrances
        """
        return self.detected_entrances
    
    def reset(self) -> None:
        """
        Reset mapper state.
        """
        self.detected_entrances = []