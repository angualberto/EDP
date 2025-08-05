import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm

def create_vortex_animation(r, theta, z, t_values, m, k, output_file, fps=30):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    def update(frame):
        ax.clear()
        t = t_values[frame]
        fourier_result = generate_fourier_modes(r, theta, z, t, m, k)
        Z_final = z + fourier_result
        X = r * np.cos(theta)
        Y = r * np.sin(theta)
        ax.plot_surface(X, Y, Z_final, cmap='coolwarm', alpha=0.7)
        ax.set_title(f"Vortex Animation: t={t:.2f}")
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')

    ani = animation.FuncAnimation(fig, update, frames=len(t_values), repeat=False)
    ani.save(output_file, writer='ffmpeg', fps=fps)
    plt.close(fig)

def generate_fourier_modes(r, theta, z, t, m, k):
    fourier_sum = np.zeros_like(r)
    n_fourier_modes = 4  # Example value, can be parameterized

    for n in range(1, n_fourier_modes + 1):
        amplitude_n = 1.0 / n**0.5
        omega_n = 1.2 * (1 + 0.2 * n)
        k_n = k * n / 2
        
        fourier_term = amplitude_n * np.cos(n * m * theta + k_n * z - omega_n * t)
        fourier_sum += fourier_term
    
    return fourier_sum