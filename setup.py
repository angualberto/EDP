from setuptools import setup, find_packages

setup(
    name='vortex-simulator',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python project for simulating and visualizing vortex structures based on wave functions.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'pandas',
        'pyyaml',
        'imageio',
        'plotly',
    ],
    entry_points={
        'console_scripts': [
            'vortex-simulator=main:main',
        ],
    },
)