"""
Unit tests for EntranceMapper
"""

import pytest
import numpy as np
from src.entrance_mapper import EntranceMapper


class TestEntranceMapper:
    """Test suite for EntranceMapper class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.mapper = EntranceMapper()
    
    def test_initialization(self):
        """Test mapper initialization"""
        assert self.mapper.detected_entrances == []
        assert self.mapper.detector is not None
        assert self.mapper.classifier is not None
    
    def test_get_detected_entrances_empty(self):
        """Test getting entrances when none detected"""
        entrances = self.mapper.get_detected_entrances()
        assert entrances == []
    
    def test_reset(self):
        """Test mapper reset"""
        self.mapper.detected_entrances = [{'type': 'main_entrance'}]
        self.mapper.reset()
        assert self.mapper.detected_entrances == []
    
    def test_check_accessibility(self):
        """Test accessibility check"""
        detection = {'width': 1.0}
        accessible = self.mapper._check_accessibility(detection)
        assert accessible is True
    
    def test_get_entrance_features(self):
        """Test feature extraction"""
        detection = {
            'bbox': (10, 20, 100, 150),
            'center': (60, 95),
            'width': 100,
            'height': 150,
            'area': 15000
        }
        features = self.mapper.get_entrance_features(detection)
        assert 'bounding_box' in features
        assert 'center' in features
        assert 'width' in features


if __name__ == "__main__":
    pytest.main([__file__])