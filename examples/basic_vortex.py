#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from src.core.vortex_generator import VortexGenerator
from src.visualization.plotter_3d import plot_vortex_3d
from src.visualization.export_utils import save_plot

def main():
    # Parameters for the vortex
    m = 4  # mode
    k = 1  # wave number
    t = 0  # time

    # Create a vortex generator instance
    vortex_gen = VortexGenerator(m, k)

    # Generate the vortex structure
    r, theta, z, vortex_structure = vortex_gen.generate_vortex(t)

    # Plot the vortex structure in 3D
    fig = plot_vortex_3d(r, theta, z, vortex_structure)
    
    # Save the plot as an image
    save_plot(fig, "output/images/basic_vortex.png")

if __name__ == "__main__":
    main()