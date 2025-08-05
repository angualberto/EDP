import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_vortex_3d(X, Y, Z, title="Vortex Structure", cmap='coolwarm', save_path=None):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap=cmap, alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Plot saved as {save_path}")
    
    plt.show()