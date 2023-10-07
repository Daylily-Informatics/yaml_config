from setuptools import setup, find_packages

setup(
    name='yaml_config',
    version='0.0.2',
    description='A Python library for managing project yaml secrets configurations',
    author='John Major',
    author_email='john@daylilyinformatics.com',
    url='https://github.com/Daylily-Informatics/yaml_config',
    packages=find_packages(),
    install_requires=[
        'pyyaml',  # List your project's dependencies here
    ],
    entry_points={
        'console_scripts': [
            'yaml_config = yaml_config.config_manager:main',  # Replace 'my_project' and 'config_manager' with your actual package and module names
        ],
    },
)
