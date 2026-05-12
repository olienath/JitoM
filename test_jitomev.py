# test_jitomev.py
"""
Tests for JitoMEV module.
"""

import unittest
from jitomev import JitoMEV

class TestJitoMEV(unittest.TestCase):
    """Test cases for JitoMEV class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JitoMEV()
        self.assertIsInstance(instance, JitoMEV)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JitoMEV()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
