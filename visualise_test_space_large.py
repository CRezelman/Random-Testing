import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define multiple clustered failure regions
FAILURE_CLUSTERS = [
    {'center': [20, 20, 20], 'radius': 5},
    {'center': [50, 50, 50], 'radius': 8},
    {'center': [80, 30, 70], 'radius': 6},
]

# Mock API with multiple failure zones
def mock_api(x, y, z):
    for cluster in FAILURE_CLUSTERS:
        cx, cy, cz = cluster['center']
        r = cluster['radius']
        if np.linalg.norm([x - cx, y - cy, z - cz]) < r:
            return "fail"
    return "pass"

# Generate random test inputs
def generate_random_tests(n):
    return np.random.uniform(0, 100, (n, 3))

# Run test inputs through the mock API
def evaluate_tests(inputs):
    results = []
    for x, y, z in inputs:
        result = mock_api(x, y, z)
        results.append(result)
    return results

# Plot pass/fail test results in 3D
def plot_results(inputs, results):
    inputs = np.array(inputs)
    results = np.array(results)
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    passes = inputs[results == 'pass']
    fails = inputs[results == 'fail']

    ax.scatter(passes[:, 0], passes[:, 1], passes[:, 2], c='green', label='Pass', alpha=0.4)
    ax.scatter(fails[:, 0], fails[:, 1], fails[:, 2], c='red', label='Fail', alpha=0.8)

    # Draw spheres for visualising the clusters
    for cluster in FAILURE_CLUSTERS:
        cx, cy, cz = cluster['center']
        ax.text(cx, cy, cz, "Fail Zone", color='red')

    ax.set_title("Random Testing Across Expanded Input Space")
    ax.set_xlabel("Input X")
    ax.set_ylabel("Input Y")
    ax.set_zlabel("Input Z")
    ax.legend()
    plt.show()

# Main
num_tests = 2000
test_inputs = generate_random_tests(num_tests)
test_results = evaluate_tests(test_inputs)
plot_results(test_inputs, np.array(test_results))
