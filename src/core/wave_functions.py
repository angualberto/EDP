def wave_function(theta, z, t, m, k):
    amplitude = 1.0  # Amplitude of the wave function
    return amplitude * np.cos(m * theta + k * z - t)

def compute_wave_modes(theta, z, t, m_values, k_values):
    wave_results = {}
    for m in m_values:
        for k in k_values:
            wave_results[(m, k)] = wave_function(theta, z, t, m, k)
    return wave_results

def generate_wave_surface(theta, z, t, m, k):
    wave_surface = wave_function(theta, z, t, m, k)
    return wave_surface