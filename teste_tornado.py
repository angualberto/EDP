#!/usr/bin/env python3
# filepath: enhanced_tornado_simulator.py

"""
Enhanced 3D Tornado Simulator with Wave Propagation
Implements η(θ,z,t) = A_{m,k} * e^{i(mθ + kz - ω_{m,k}t)}
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Backend without display
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D
import json
from datetime import datetime

class TornadoSimulator:
    def __init__(self, config_file=None):
        """Initialize tornado simulator with physics parameters"""
        self.load_config(config_file)
        self.setup_colormap()
    
    def load_config(self, config_file):
        """Load simulation parameters"""
        # Default parameters
        self.params = {
            # Physical parameters
            'gamma': 10.0,          # Circulation strength (Γ)
            'sigma': 0.1,           # Surface tension (σ)
            'rho': 1.0,             # Density (ρ)
            'a': 1.0,               # Characteristic radius
            
            # Wave parameters
            'm_mode': 4,            # Azimuthal mode number
            'k_wave': 0.5,          # Axial wave number
            'n_fourier_modes': 6,   # Number of Fourier modes
            'n_layers': 8,          # Number of vertical layers
            
            # Simulation parameters
            'r_max': 15.0,          # Maximum radius
            'z_max': 20.0,          # Maximum height
            'n_r': 40,              # Radial resolution
            'n_theta': 80,          # Angular resolution
            'n_z': 30,              # Vertical resolution
            
            # Animation parameters
            'fps': 20,
            'duration': 3.0,        # seconds
            'save_frames': True
        }
        
        if config_file:
            try:
                with open(config_file, 'r') as f:
                    custom_params = json.load(f)
                    self.params.update(custom_params)
            except FileNotFoundError:
                print(f"Config file {config_file} not found, using defaults")
    
    def setup_colormap(self):
        """Create custom colormap for tornado visualization"""
        colors = ['#000080', '#0040FF', '#00FFFF', '#FFFF00', '#FF4000', '#800000']
        self.tornado_cmap = LinearSegmentedColormap.from_list('tornado', colors, N=256)
    
    def wave_frequency(self, m, k):
        """
        Calculate wave frequency using two formulations:
        1. ω_{m,k} = (Γ/2πa²) * m * (ka)²
        2. ω_{m,k}² = (σ/ρa³) * m(m² - 1)
        """
        # Primary frequency (circulation-based)
        omega_1 = (self.params['gamma'] / (2 * np.pi * self.params['a']**2)) * \
                  m * (k * self.params['a'])**2
        
        # Secondary frequency (surface tension-based)
        if m > 1:
            omega_2_squared = (self.params['sigma'] / (self.params['rho'] * self.params['a']**3)) * \
                             m * (m**2 - 1)
            omega_2 = np.sqrt(max(0, omega_2_squared))
        else:
            omega_2 = 0
        
        # Combine both contributions
        return omega_1 + 0.1 * omega_2
    
    def wave_function(self, r, theta, z, t, m, k):
        """
        Calculate wave displacement η(θ,z,t) = A_{m,k} * e^{i(mθ + kz - ω_{m,k}t)}
        Returns real part for visualization
        """
        omega = self.wave_frequency(m, k)
        amplitude = 1.0 / (1 + m + k)  # Decay with mode number
        
        # Phase calculation
        phase = m * theta + k * z - omega * t
        
        # Radial decay
        radial_decay = np.exp(-0.1 * r / self.params['a'])
        
        # Complex wave function
        eta_complex = amplitude * radial_decay * np.exp(1j * phase)
        
        # Return real part for visualization
        return np.real(eta_complex)
    
    def generate_fourier_layers(self, t=0):
        """Generate 3D tornado structure using Fourier series"""
        # Create coordinate grids
        r = np.linspace(0.5, self.params['r_max'], self.params['n_r'])
        theta = np.linspace(0, 2*np.pi, self.params['n_theta'])
        z_levels = np.linspace(0, self.params['z_max'], self.params['n_layers'])
        
        X_layers, Y_layers, Z_layers = [], [], []
        
        for z_level in z_levels:
            R, THETA = np.meshgrid(r, theta)
            Z = np.full_like(R, z_level)
            
            # Calculate Fourier series sum
            fourier_sum = np.zeros_like(R)
            
            for n in range(1, self.params['n_fourier_modes'] + 1):
                k_n = self.params['k_wave'] * n / 2
                wave_contrib = self.wave_function(R, THETA, Z, t, 
                                                self.params['m_mode'], k_n)
                fourier_sum += wave_contrib / n
            
            # Apply height modulation
            Z_final = Z + fourier_sum * (1 + 0.1 * z_level)
            
            # Convert to Cartesian coordinates
            X = R * np.cos(THETA)
            Y = R * np.sin(THETA)
            
            X_layers.append(X)
            Y_layers.append(Y)
            Z_layers.append(Z_final)
        
        return X_layers, Y_layers, Z_layers
    
    def plot_3d_tornado(self, X_layers, Y_layers, Z_layers, t=0, save_path=None):
        """Create advanced 3D visualization"""
        fig = plt.figure(figsize=(16, 12))
        fig.patch.set_facecolor('#1a1a1a')
        
        # Main 3D plot
        ax1 = fig.add_subplot(2, 2, 1, projection='3d')
        ax1.set_facecolor('#1a1a1a')
        
        # Plot layers with transparency
        for i, (X, Y, Z) in enumerate(zip(X_layers, Y_layers, Z_layers)):
            alpha = 0.6 * (1 - i / len(Z_layers))
            surf = ax1.plot_surface(X, Y, Z, cmap=self.tornado_cmap, 
                                  alpha=alpha, linewidth=0, antialiased=True)
        
        ax1.set_title(f'3D Tornado - Wave Modes (t={t:.2f}s)', 
                     color='white', fontsize=14)
        ax1.set_xlabel('X (m)', color='white')
        ax1.set_ylabel('Y (m)', color='white')
        ax1.set_zlabel('Z (m)', color='white')
        ax1.tick_params(colors='white')
        
        # Top view
        ax2 = fig.add_subplot(2, 2, 2)
        ax2.set_facecolor('#1a1a1a')
        if X_layers and Y_layers and Z_layers:
            contour = ax2.contourf(X_layers[-1], Y_layers[-1], Z_layers[-1], 
                                 levels=20, cmap=self.tornado_cmap)
            ax2.contour(X_layers[-1], Y_layers[-1], Z_layers[-1], 
                       levels=10, colors='white', alpha=0.3, linewidths=0.5)
        
        ax2.set_title('Top View - Wave Pattern', color='white')
        ax2.set_xlabel('X (m)', color='white')
        ax2.set_ylabel('Y (m)', color='white')
        ax2.tick_params(colors='white')
        ax2.set_aspect('equal')
        
        # Wave frequency analysis
        ax3 = fig.add_subplot(2, 2, 3)
        ax3.set_facecolor('#1a1a1a')
        
        modes = np.arange(1, self.params['n_fourier_modes'] + 1)
        frequencies = [self.wave_frequency(self.params['m_mode'], 
                                         self.params['k_wave'] * n / 2) 
                      for n in modes]
        
        bars = ax3.bar(modes, frequencies, color='cyan', alpha=0.7, 
                      edgecolor='white')
        ax3.set_title('Wave Frequency Spectrum', color='white')
        ax3.set_xlabel('Mode Number', color='white')
        ax3.set_ylabel('Frequency (rad/s)', color='white')
        ax3.tick_params(colors='white')
        ax3.grid(True, alpha=0.3)
        
        # Parameters display
        ax4 = fig.add_subplot(2, 2, 4)
        ax4.set_facecolor('#1a1a1a')
        ax4.axis('off')
        
        param_text = f"""
        WAVE PARAMETERS
        ─────────────────
        m-mode: {self.params['m_mode']}
        Circulation Γ: {self.params['gamma']:.1f}
        Surface tension σ: {self.params['sigma']:.3f}
        Density ρ: {self.params['rho']:.1f}
        Radius a: {self.params['a']:.1f} m
        
        SIMULATION
        ─────────────────
        Fourier modes: {self.params['n_fourier_modes']}
        Layers: {self.params['n_layers']}
        Time: {t:.2f} s
        
        FREQUENCIES
        ─────────────────
        ω₁ = (Γ/2πa²)m(ka)²
        ω₂² = (σ/ρa³)m(m²-1)
        """
        
        ax4.text(0.05, 0.95, param_text, transform=ax4.transAxes,
                fontsize=10, color='white', verticalalignment='top',
                fontfamily='monospace',
                bbox=dict(boxstyle="round,pad=0.5", facecolor='#2d2d2d', 
                         alpha=0.8, edgecolor='cyan'))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight',
                       facecolor='#1a1a1a', edgecolor='none')
            print(f"Saved: {save_path}")
        
        plt.close()
    
    def create_animation(self, output_path="tornado_animation.gif"):
        """Create animated sequence"""
        n_frames = int(self.params['fps'] * self.params['duration'])
        time_points = np.linspace(0, self.params['duration'], n_frames)
        
        frame_paths = []
        
        for i, t in enumerate(time_points):
            print(f"Generating frame {i+1}/{n_frames} (t={t:.2f}s)")
            
            X_layers, Y_layers, Z_layers = self.generate_fourier_layers(t)
            
            frame_path = f"temp_frame_{i:03d}.png"
            self.plot_3d_tornado(X_layers, Y_layers, Z_layers, t, frame_path)
            frame_paths.append(frame_path)
        
        # Create GIF (requires pillow)
        try:
            from PIL import Image
            images = []
            for path in frame_paths:
                images.append(Image.open(path))
            
            images[0].save(output_path, save_all=True, append_images=images[1:],
                          duration=1000//self.params['fps'], loop=0)
            
            # Cleanup temporary files
            import os
            for path in frame_paths:
                os.remove(path)
            
            print(f"Animation saved: {output_path}")
            
        except ImportError:
            print("PIL not available. Individual frames saved.")
    
    def run_simulation(self):
        """Run complete simulation"""
        print("Starting Enhanced Tornado Simulation...")
        print(f"Parameters: m={self.params['m_mode']}, "
              f"modes={self.params['n_fourier_modes']}, "
              f"layers={self.params['n_layers']}")
        
        # Generate static frame
        X_layers, Y_layers, Z_layers = self.generate_fourier_layers(0)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        static_path = f"tornado_3d_{timestamp}.png"
        self.plot_3d_tornado(X_layers, Y_layers, Z_layers, 0, static_path)
        
        # Generate animation
        if self.params['save_frames']:
            anim_path = f"tornado_animation_{timestamp}.gif"
            self.create_animation(anim_path)
        
        print("Simulation completed!")

if __name__ == "__main__":
    # Create and run simulation
    simulator = TornadoSimulator()
    simulator.run_simulation()