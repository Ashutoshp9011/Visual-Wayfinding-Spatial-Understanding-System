"""
Helper utilities for step tracking
"""

import numpy as np
from scipy.ndimage import uniform_filter1d
from typing import Optional


def smooth_signal(signal: np.ndarray, window_size: int = 5) -> np.ndarray:
    """
    Apply smoothing filter to signal.
    
    Args:
        signal (np.ndarray): Input signal
        window_size (int): Smoothing window size
        
    Returns:
        np.ndarray: Smoothed signal
    """
    if len(signal) < window_size:
        return signal
    return uniform_filter1d(signal, size=window_size, mode='nearest')


def calculate_distance(steps: int, stride_length: float) -> float:
    """
    Calculate distance traveled based on steps and stride length.
    
    Args:
        steps (int): Number of steps
        stride_length (float): Average stride length in meters
        
    Returns:
        float: Distance in meters
    """
    return max(0, steps * stride_length)


def normalize_signal(signal: np.ndarray) -> np.ndarray:
    """
    Normalize signal to 0-1 range.
    
    Args:
        signal (np.ndarray): Input signal
        
    Returns:
        np.ndarray: Normalized signal
    """
    min_val = np.min(signal)
    max_val = np.max(signal)
    if max_val - min_val == 0:
        return np.zeros_like(signal)
    return (signal - min_val) / (max_val - min_val)


def calculate_stride_variability(steps_data: np.ndarray) -> float:
    """
    Calculate stride variability from step intervals.
    
    Args:
        steps_data (np.ndarray): Array of step timestamps
        
    Returns:
        float: Coefficient of variation
    """
    if len(steps_data) < 2:
        return 0.0
    intervals = np.diff(steps_data)
    if np.mean(intervals) == 0:
        return 0.0
    return np.std(intervals) / np.mean(intervals)