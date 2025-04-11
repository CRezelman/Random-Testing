# FSCS Testing Tool

This tool is designed to generate failure clusters and run random and FSCS-ART (Failure-driven Similarity-based Clustering and Adaptive Random Testing) tests. It also visualizes the results of the testing process.

## Features
- Generate failure clusters.
- Run random testing and FSCS-ART testing strategies.
- Visualize the results of the testing process.

## Requirements
- Python 3.8 or higher
- Virtual environment (recommended)

## Installation

1. Clone the repository or download the project files.

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On **Windows (PowerShell)**:
     ```powershell
     .\.venv\Scripts\Activate
     ```
   - On **Windows (Bash)**:
     ```bash
     source .venv/Scripts/activate
     ```
   - On **Linux/Mac**:
     ```bash
     source .venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure the virtual environment is activated:
   ```bash
   source .venv/Scripts/activate  # Windows (Bash)
   # or
   source .venv/bin/activate      # Linux/Mac
   ```

2. Run the tool:
   ```bash
   python fscs_testing/__main__.py
   ```

## Configuration
The tool uses a `config` module to set parameters such as:
- `num_tests`: Number of tests to run.
- `seed`: Random seed for reproducibility.

Modify these parameters in the `config` file as needed.

## Output
- Logs will display the progress and results of the testing process.
- Visualizations of the results will be generated using the `plot_results` function.

## License
This project is licensed under the MIT License.
