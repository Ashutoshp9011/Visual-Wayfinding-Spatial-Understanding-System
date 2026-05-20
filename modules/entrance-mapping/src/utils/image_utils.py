"""
Image utilities for entrance mapping
"""

import cv2
import numpy as np
from typing import Optional, Tuple


def load_image(image_path: str) -> Optional[np.ndarray]:
    """
    Load image from file.
    
    Args:
        image_path (str): Path to image file
        
    Returns:
        np.ndarray: Loaded image (BGR) or None if failed
    """
    try:
        image = cv2.imread(image_path)
        if image is None:
            return None
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


def resize_image(image: np.ndarray, size: Tuple[int, int]) -> np.ndarray:
    """
    Resize image to specified size.
    
    Args:
        image (np.ndarray): Input image
        size (Tuple): Target size (width, height)
        
    Returns:
        np.ndarray: Resized image
    """
    return cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)


def process_image(image: np.ndarray, target_size: Tuple[int, int] = (640, 480)) -> np.ndarray:
    """
    Process image for detection (resize and normalize).
    
    Args:
        image (np.ndarray): Input image
        target_size (Tuple): Target size
        
    Returns:
        np.ndarray: Processed image
    """
    # Resize
    resized = resize_image(image, target_size)
    
    # Normalize
    normalized = resized.astype(np.float32) / 255.0
    
    return normalized


def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert image to grayscale.
    
    Args:
        image (np.ndarray): Input image (BGR)
        
    Returns:
        np.ndarray: Grayscale image
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_adaptive_threshold(image: np.ndarray) -> np.ndarray:
    """
    Apply adaptive thresholding to image.
    
    Args:
        image (np.ndarray): Input grayscale image
        
    Returns:
        np.ndarray: Thresholded image
    """
    return cv2.adaptiveThreshold(
        image,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )