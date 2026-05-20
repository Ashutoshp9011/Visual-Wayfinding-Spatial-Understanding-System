"""
Unit tests for StepTracker
"""

import pytest
import numpy as np
from src.step_tracker import StepTracker


class TestStepTracker:
    """Test suite for StepTracker class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.tracker = StepTracker(stride_length=0.75)
    
    def test_initialization(self):
        """Test tracker initialization"""
        assert self.tracker.step_count == 0
        assert self.tracker.total_distance == 0.0
        assert self.tracker.stride_length == 0.75
    
    def test_set_stride_length(self):
        """Test stride length setter"""
        self.tracker.set_stride_length(0.8)
        assert self.tracker.stride_length == 0.8
    
    def test_calibrate_stride(self):
        """Test stride calibration"""
        calibrated = self.tracker.calibrate_stride(10.0, 13)
        assert abs(calibrated - (10.0 / 13)) < 0.01
    
    def test_get_step_count(self):
        """Test getting step count"""
        assert self.tracker.get_step_count() == 0
    
    def test_get_distance(self):
        """Test getting distance"""
        assert self.tracker.get_distance() == 0.0
    
    def test_get_statistics(self):
        """Test statistics generation"""
        stats = self.tracker.get_statistics()
        assert 'total_steps' in stats
        assert 'distance' in stats
        assert 'stride_length' in stats
    
    def test_reset(self):
        """Test tracker reset"""
        self.tracker.step_count = 10
        self.tracker.total_distance = 7.5
        self.tracker.reset()
        assert self.tracker.step_count == 0
        assert self.tracker.total_distance == 0.0


if __name__ == "__main__":
    pytest.main([__file__])