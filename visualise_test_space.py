import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Mock API with a failure region
def mock_api(x, y, z):
    if 4 <= x <= 6 and 4 <= y <= 6 and 4 <= z <= 6:
        return "fail"
    return "pass"

# Random test input generation
def generate_random_tests(n):
    return np.random.uniform(0, 10, (n, 3))

# Run the tests
def evaluate_tests(inputs):
    results = []
    for x, y, z in inputs:
        result = mock_api(x, y, z)
        results.append(result)
    return results

# Visualise results
def plot_results(inputs, results):
    inputs = np.array(inputs)
    results = np.array(results)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    passes = inputs[results == 'pass']
    fails = inputs[results == 'fail']

    ax.scatter(passes[:, 0], passes[:, 1], passes[:, 2], c='green', label='Pass')
    ax.scatter(fails[:, 0], fails[:, 1], fails[:, 2], c='red', label='Fail')

    ax.set_title("Random Testing on Mock API")
    ax.set_xlabel("Input X")
    ax.set_ylabel("Input Y")
    ax.set_zlabel("Input Z")
    ax.legend()
    plt.show()

# Main
num_tests = 100
test_inputs = generate_random_tests(num_tests)
test_results = evaluate_tests(test_inputs)
plot_results(test_inputs, test_results)
