"""
Entrance Detection - Identifies door and entrance regions in images
"""

import numpy as np
import cv2
from typing import List, Dict, Tuple
from sklearn.cluster import DBSCAN


class EntranceDetector:
    """
    Detects entrance and door regions in images using edge detection and segmentation.
    """
    
    def __init__(self, min_size: Tuple[int, int] = (50, 100)):
        """
        Initialize EntranceDetector.
        
        Args:
            min_size (Tuple): Minimum detection size (width, height)
        """
        self.min_size = min_size
    
    def detect(self, image: np.ndarray) -> List[Dict]:
        """
        Detect entrance regions in image.
        
        Args:
            image (np.ndarray): Input image (BGR)
            
        Returns:
            List[Dict]: List of detected entrances with bounding boxes
        """
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply edge detection
        edges = cv2.Canny(gray, 100, 200)
        
        # Dilate edges to connect nearby edges
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        dilated = cv2.dilate(edges, kernel, iterations=2)
        
        # Find contours
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Process contours
        detections = []
        for contour in contours:
            detection = self._process_contour(contour, image)
            if detection is not None:
                detections.append(detection)
        
        return detections
    
    def _process_contour(self, contour: np.ndarray, image: np.ndarray) -> Dict:
        """
        Process a single contour and extract detection info.
        
        Args:
            contour (np.ndarray): Contour points
            image (np.ndarray): Original image
            
        Returns:
            Dict: Detection information or None
        """
        x, y, w, h = cv2.boundingRect(contour)
        
        # Check minimum size
        if w < self.min_size[0] or h < self.min_size[1]:
            return None
        
        # Check aspect ratio (doors are typically taller than wide)
        aspect_ratio = h / (w + 1e-6)
        if aspect_ratio < 1.0:  # More wide than tall
            return None
        
        # Calculate confidence based on area
        area = cv2.contourArea(contour)
        image_area = image.shape[0] * image.shape[1]
        confidence = min(area / (image_area / 10), 1.0)
        
        detection = {
            'bbox': (x, y, w, h),
            'center': (x + w // 2, y + h // 2),
            'width': w,
            'height': h,
            'area': area,
            'aspect_ratio': aspect_ratio,
            'confidence': confidence
        }
        
        return detection