import numpy as np
import matplotlib.pyplot as plt
from src.core.vortex_generator import VortexGenerator
from src.visualization.plotter_3d import plot_vortex
from src.visualization.export_utils import save_image

def parameter_sweep(m_values, k_values, t_values):
    for m in m_values:
        for k in k_values:
            for t in t_values:
                print(f"Running simulation for m={m}, k={k}, t={t}...")
                
                vortex_gen = VortexGenerator(m, k, t)
                vortex_structure = vortex_gen.generate_vortex_structure()
                
                plot_vortex(vortex_structure)
                save_image(f"output/images/vortex_m{m}_k{k}_t{t}.png")

if __name__ == "__main__":
    m_values = [1, 2, 3, 4]
    k_values = [0.1, 0.2, 0.3]
    t_values = [0, 1, 2]

    parameter_sweep(m_values, k_values, t_values)