#!/usr/bin/env python3

import json
import yaml
from core.parameters import load_parameters
from core.vortex_generator import VortexGenerator
from visualization.plotter_3d import plot_vortex
from visualization.animation import create_animation
from visualization.export_utils import export_results

def main():
    print("Welcome to the Vortex Simulator!")
    
    # Load parameters from configuration files
    params = load_parameters()
    
    # Initialize the vortex generator with the loaded parameters
    vortex_gen = VortexGenerator(params)
    
    # Generate the vortex structure
    vortex_structure = vortex_gen.generate_vortex()
    
    # Plot the vortex structure in 3D
    plot_vortex(vortex_structure)
    
    # Create an animation of the vortex modes
    create_animation(vortex_structure)
    
    # Export results as images and videos
    export_results(vortex_structure)

    print("Simulation complete! Check the output directory for results.")

if __name__ == "__main__":
    main()