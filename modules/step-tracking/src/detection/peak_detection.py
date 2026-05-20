"""
Peak Detection - Identifies step peaks in acceleration data
"""

import numpy as np
from scipy.signal import find_peaks
from typing import Tuple


class PeakDetector:
    """
    Detects peaks in acceleration signals that correspond to step events.
    """
    
    def __init__(self, sensor_freq: float = 100.0, prominence: float = 0.5):
        """
        Initialize PeakDetector.
        
        Args:
            sensor_freq (float): Sensor sampling frequency in Hz
            prominence (float): Minimum peak prominence threshold
        """
        self.sensor_freq = sensor_freq
        self.prominence = prominence
        self.min_distance = int(0.3 * sensor_freq)  # Minimum 0.3s between steps
        
    def detect(self, signal: np.ndarray) -> np.ndarray:
        """
        Detect peaks in the acceleration signal.
        
        Args:
            signal (np.ndarray): Acceleration magnitude signal
            
        Returns:
            np.ndarray: Indices of detected peaks
        """
        if len(signal) < self.min_distance * 2:
            return np.array([])
        
        # Find peaks with constraints
        peaks, _ = find_peaks(
            signal,
            height=np.mean(signal),
            distance=self.min_distance,
            prominence=self.prominence
        )
        
        return peaks
    
    def detect_with_confidence(self, signal: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Detect peaks and return confidence scores.
        
        Args:
            signal (np.ndarray): Acceleration magnitude signal
            
        Returns:
            Tuple: (peak indices, confidence scores)
        """
        if len(signal) < self.min_distance * 2:
            return np.array([]), np.array([])
        
        peaks, properties = find_peaks(
            signal,
            height=np.mean(signal),
            distance=self.min_distance,
            prominence=self.prominence
        )
        
        # Calculate confidence based on prominence
        if len(peaks) > 0:
            prominence_values = properties['prominences']
            confidence = prominence_values / (np.max(prominence_values) + 1e-6)
        else:
            confidence = np.array([])
        
        return peaks, confidence