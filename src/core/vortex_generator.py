class VortexGenerator:
    def __init__(self, m, k, t, exp_decay_rate=0.5):
        self.m = m
        self.k = k
        self.t = t
        self.exp_decay_rate = exp_decay_rate

    def wave_function(self, r, theta, z):
        amplitude_n = 1.0 / (self.k ** 0.5)
        gamma_n = self.exp_decay_rate * self.k / 10
        alpha_n = self.exp_decay_rate * self.k / 15
        omega_n = 1.2 * (1 + 0.2 * self.k)
        k_n = 0.4 * self.k / 2

        exp_radial = np.exp(-gamma_n * r)
        exp_vertical = np.exp(-alpha_n * z)

        return amplitude_n * exp_radial * exp_vertical * np.cos(self.k * self.m * theta + k_n * z - omega_n * self.t)

    def generate_vortex_structure(self, r, theta, z):
        vortex_structure = np.zeros_like(r)

        for n in range(1, self.k + 1):
            vortex_structure += self.wave_function(r, theta, z)

        return vortex_structure

    def export_results(self, results, filename):
        np.save(filename, results)  # Save results as a .npy file

    def simulate(self, r, theta, z):
        return self.generate_vortex_structure(r, theta, z)