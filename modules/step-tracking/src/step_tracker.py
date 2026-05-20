"""
Step Tracker - Main class for step detection and tracking
"""

import numpy as np
from typing import List, Dict, Tuple, Optional
from .detection.peak_detection import PeakDetector
from .utils.helpers import smooth_signal, calculate_distance


class StepTracker:
    """
    Real-time step tracking and detection system.
    
    Detects steps from accelerometer data and calculates distance traveled
    based on stride length.
    """
    
    def __init__(self, stride_length: float = 0.75, sensor_freq: float = 100.0):
        """
        Initialize StepTracker.
        
        Args:
            stride_length (float): Average stride length in meters (default: 0.75m)
            sensor_freq (float): Sensor sampling frequency in Hz (default: 100Hz)
        """
        self.stride_length = stride_length
        self.sensor_freq = sensor_freq
        self.step_count = 0
        self.total_distance = 0.0
        self.steps_history = []
        self.peak_detector = PeakDetector(sensor_freq=sensor_freq)
        
    def detect_steps(self, accel_data: np.ndarray) -> int:
        """
        Detect steps from accelerometer data.
        
        Args:
            accel_data (np.ndarray): Acceleration data array (shape: (N, 3) or (N,))
            
        Returns:
            int: Number of steps detected
        """
        # Calculate magnitude of acceleration vector
        if accel_data.ndim == 2:
            accel_magnitude = np.linalg.norm(accel_data, axis=1)
        else:
            accel_magnitude = accel_data
            
        # Smooth the signal
        smoothed = smooth_signal(accel_magnitude, window_size=5)
        
        # Detect peaks (step events)
        peaks = self.peak_detector.detect(smoothed)
        
        # Update step count
        new_steps = len(peaks) - len(self.steps_history)
        self.step_count += max(0, new_steps)
        self.steps_history = peaks.tolist()
        
        # Update distance
        self.total_distance = calculate_distance(self.step_count, self.stride_length)
        
        return new_steps
    
    def get_step_count(self) -> int:
        """
        Get total number of steps detected.
        
        Returns:
            int: Total step count
        """
        return self.step_count
    
    def get_distance(self) -> float:
        """
        Get total distance traveled.
        
        Returns:
            float: Distance in meters
        """
        return self.total_distance
    
    def calibrate_stride(self, known_distance: float, measured_steps: int) -> float:
        """
        Calibrate stride length based on known distance and measured steps.
        
        Args:
            known_distance (float): Known distance traveled in meters
            measured_steps (int): Number of steps measured
            
        Returns:
            float: Calibrated stride length
        """
        if measured_steps > 0:
            self.stride_length = known_distance / measured_steps
        return self.stride_length
    
    def set_stride_length(self, stride_length: float) -> None:
        """
        Set the stride length manually.
        
        Args:
            stride_length (float): Stride length in meters
        """
        if stride_length > 0:
            self.stride_length = stride_length
    
    def get_statistics(self) -> Dict[str, float]:
        """
        Get tracking statistics.
        
        Returns:
            Dict: Dictionary containing statistics
        """
        return {
            'total_steps': self.step_count,
            'distance': self.total_distance,
            'stride_length': self.stride_length,
            'avg_speed': self._calculate_avg_speed()
        }
    
    def reset(self) -> None:
        """
        Reset the tracker to initial state.
        """
        self.step_count = 0
        self.total_distance = 0.0
        self.steps_history = []
    
    def _calculate_avg_speed(self) -> float:
        """
        Calculate average speed (placeholder).
        
        Returns:
            float: Average speed in m/s
        """
        # TODO: Implement speed calculation based on timestamp data
        return 0.0