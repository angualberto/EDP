# File: /vortex-simulator/vortex-simulator/src/core/parameters.py

DEFAULT_MODE_M = 4
DEFAULT_N_FOURIER_MODES = 4
DEFAULT_N_LAYERS = 4
DEFAULT_LAYER_SPACING = 3.0
DEFAULT_EXP_DECAY_RATE = 0.5

def load_parameters_from_json(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def load_parameters_from_yaml(file_path):
    import yaml
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def get_default_parameters():
    return {
        'mode_m': DEFAULT_MODE_M,
        'n_fourier_modes': DEFAULT_N_FOURIER_MODES,
        'n_layers': DEFAULT_N_LAYERS,
        'layer_spacing': DEFAULT_LAYER_SPACING,
        'exp_decay_rate': DEFAULT_EXP_DECAY_RATE
    }