import unittest
import numpy as np
import matplotlib.pyplot as plt
from src.visualization.plotter_3d import plot_vortex_structure
from src.visualization.animation import create_vortex_animation

class TestVisualization(unittest.TestCase):

    def setUp(self):
        self.r = np.linspace(0.5, 10, 30)
        self.theta = np.linspace(0, 2 * np.pi, 60)
        self.R, self.THETA = np.meshgrid(self.r, self.theta)
        self.Z = np.full_like(self.R, 5.0)

    def test_plot_vortex_structure(self):
        Z_final = self.Z + np.sin(self.R)  # Dummy data for testing
        fig = plot_vortex_structure(self.R, self.THETA, Z_final)
        self.assertIsInstance(fig, plt.Figure)

    def test_create_vortex_animation(self):
        output_path = "output/animations/test_animation.mp4"
        success = create_vortex_animation(self.R, self.THETA, self.Z, output_path)
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()