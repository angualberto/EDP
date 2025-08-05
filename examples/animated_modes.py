import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from src.core.wave_functions import compute_wave_function
from src.visualization.export_utils import save_animation

def animate_modes(m_values, k_values, t_values, r, theta, z):
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    
    def update(frame):
        ax.clear()
        m = m_values[frame % len(m_values)]
        k = k_values[frame % len(k_values)]
        t = t_values[frame % len(t_values)]
        
        wave_function = compute_wave_function(r, theta, z, m, k, t)
        X = r * np.cos(theta)
        Y = r * np.sin(theta)
        
        ax.plot_surface(X, Y, wave_function, cmap='coolwarm', alpha=0.7)
        ax.set_title(f"Vortex Mode: m={m}, k={k}, t={t}")
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Wave Function')
        
    ani = FuncAnimation(fig, update, frames=len(m_values) * len(k_values) * len(t_values), repeat=True)
    
    return ani

if __name__ == "__main__":
    r = np.linspace(0.5, 10, 30)
    theta = np.linspace(0, 2 * np.pi, 60)
    z = np.full_like(r, 5.0)

    m_values = [1, 2, 3, 4]
    k_values = [1, 2]
    t_values = np.linspace(0, 10, 100)

    animation = animate_modes(m_values, k_values, t_values, r, theta, z)
    save_animation(animation, "vortex_modes_animation.mp4")