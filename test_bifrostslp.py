# test_bifrostslp.py
"""
Tests for BifrostSlp module.
"""

import unittest
from bifrostslp import BifrostSlp

class TestBifrostSlp(unittest.TestCase):
    """Test cases for BifrostSlp class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BifrostSlp()
        self.assertIsInstance(instance, BifrostSlp)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BifrostSlp()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
