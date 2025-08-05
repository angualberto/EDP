# Vortex Simulator

## Overview
The Vortex Simulator is a Python project designed to generate 3D visualizations of vortex structures based on wave functions. It allows users to simulate different modes by varying parameters such as m, k, and t, and export the results as images, GIFs, or MP4 videos.

## Project Structure
```
vortex-simulator
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── wave_functions.py
│   │   ├── vortex_generator.py
│   │   └── parameters.py
│   ├── visualization
│   │   ├── __init__.py
│   │   ├── plotter_3d.py
│   │   ├── animation.py
│   │   └── export_utils.py
│   └── utils
│       ├── __init__.py
│       ├── math_helpers.py
│       └── file_handlers.py
├── config
│   ├── default_params.json
│   └── simulation_config.yaml
├── examples
│   ├── basic_vortex.py
│   ├── animated_modes.py
│   └── parameter_sweep.py
├── tests
│   ├── __init__.py
│   ├── test_wave_functions.py
│   ├── test_vortex_generator.py
│   └── test_visualization.py
├── output
│   ├── images
│   ├── animations
│   └── videos
├── requirements.txt
├── setup.py
└── README.md
```

## Installation
To set up the Vortex Simulator, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd vortex-simulator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the simulation, execute the main script:
```
python src/main.py
```

### Examples
- **Basic Vortex**: See how to generate a basic vortex structure in `examples/basic_vortex.py`.
- **Animated Modes**: Create animations of different vortex modes in `examples/animated_modes.py`.
- **Parameter Sweep**: Run simulations with varying parameters in `examples/parameter_sweep.py`.

## Output
Generated images, animations, and videos will be stored in the `output` directory under their respective folders (`images`, `animations`, `videos`).

## Testing
To run the tests, use:
```
pytest tests/
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.