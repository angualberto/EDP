import unittest
from src.core.wave_functions import compute_wave_function

class TestWaveFunctions(unittest.TestCase):

    def test_wave_function(self):
        # Test parameters
        m = 4
        k = 2
        t = 1
        theta = 0.5
        z = 1.0
        
        # Expected output (this should be calculated based on the actual wave function logic)
        expected_result = compute_wave_function(theta, z, t, m, k)
        
        # Call the function to test
        result = compute_wave_function(theta, z, t, m, k)
        
        # Assert the result is as expected
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_wave_function_with_different_parameters(self):
        # Test with different parameters
        m = 3
        k = 1
        t = 0
        theta = 1.0
        z = 2.0
        
        expected_result = compute_wave_function(theta, z, t, m, k)
        result = compute_wave_function(theta, z, t, m, k)
        
        self.assertAlmostEqual(result, expected_result, places=5)

if __name__ == '__main__':
    unittest.main()