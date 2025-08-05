def calculate_wave_function(m, k, t, theta, z):
    return np.sin(m * theta) * np.exp(-k * z) * np.cos(t)

def generate_radial_coordinates(num_points, r_min, r_max):
    return np.linspace(r_min, r_max, num_points)

def generate_theta_coordinates(num_points):
    return np.linspace(0, 2 * np.pi, num_points)

def compute_vortex_parameters(m, k, t):
    return {
        'wave_function': calculate_wave_function(m, k, t, np.linspace(0, 2 * np.pi, 100), 0),
        'amplitude': 1.0 / (m + 1),
        'frequency': k * m
    }