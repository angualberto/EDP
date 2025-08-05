import unittest
from src.core.vortex_generator import VortexGenerator

class TestVortexGenerator(unittest.TestCase):

    def setUp(self):
        self.vortex_gen = VortexGenerator(m=4, k=1.0, t=0.0)

    def test_generate_vortex_structure(self):
        r = [0.5, 1.0, 1.5]
        theta = [0, 0.5, 1.0]
        z = [0, 1, 2]
        result = self.vortex_gen.generate_vortex_structure(r, theta, z)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), len(r))

    def test_wave_function(self):
        m = 4
        k = 1.0
        t = 0.0
        result = self.vortex_gen.compute_wave_function(m, k, t)
        self.assertIsNotNone(result)

    def test_parameter_validation(self):
        with self.assertRaises(ValueError):
            VortexGenerator(m=-1, k=1.0, t=0.0)

if __name__ == '__main__':
    unittest.main()