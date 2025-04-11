import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define multiple clustered failure regions
# FAILURE_CLUSTERS = [
#     {'center': [20, 20, 20], 'radius': 5},
#     {'center': [50, 50, 50], 'radius': 8},
#     {'center': [80, 30, 70], 'radius': 6},
# ]
DIMENSION_RANGE = 1000
FAILURE_CLUSTERS = [
    {'center': [np.random.uniform(0, DIMENSION_RANGE), np.random.uniform(0, DIMENSION_RANGE), np.random.uniform(0, DIMENSION_RANGE)], 'radius': DIMENSION_RANGE * 0.15},
    {'center': [np.random.uniform(0, DIMENSION_RANGE), np.random.uniform(0, DIMENSION_RANGE), np.random.uniform(0, DIMENSION_RANGE)], 'radius': DIMENSION_RANGE * 0.05},
    {'center': [np.random.uniform(0, DIMENSION_RANGE), np.random.uniform(0, DIMENSION_RANGE), np.random.uniform(0, DIMENSION_RANGE)], 'radius': DIMENSION_RANGE * 0.1},
]

# Mock API with multiple failure zones
def mock_api(x, y, z):
    for cluster in FAILURE_CLUSTERS:
        cx, cy, cz = cluster['center']
        r = cluster['radius']
        if np.linalg.norm([x - cx, y - cy, z - cz]) < r:
            return "fail"
    return "pass"

# FSCS-ART selection: select candidate that is farthest from existing failures
def fscs_art_generate(failure_set, num_candidates=1000):
    candidates = np.random.uniform(0, DIMENSION_RANGE, (num_candidates, 3))
    if not failure_set:
        return candidates[np.random.randint(num_candidates)]

    failure_array = np.array(failure_set)
    max_min_distance = -1
    best_candidate = None

    for candidate in candidates:
        distances = np.linalg.norm(failure_array - candidate, axis=1)
        min_distance = np.min(distances)
        if min_distance > max_min_distance:
            max_min_distance = min_distance
            best_candidate = candidate

    return best_candidate
    

# Run FSCS-ART random testing
def run_fscs_art_tests(n_tests=2000):
    failure_set = []
    all_inputs = []
    all_results = []

    for _ in range(n_tests):
        test_input = fscs_art_generate(failure_set, 50)
        x, y, z = test_input
        result = mock_api(x, y, z)
        all_inputs.append([x, y, z])
        all_results.append(result)
        if result == "fail":
            failure_set.append([x, y, z])

    return np.array(all_inputs), np.array(all_results)

# Plot FSCS-ART results
def plot_fscs_results(inputs, results):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    passes = inputs[results == 'pass']
    fails = inputs[results == 'fail']

    ax.scatter(passes[:, 0], passes[:, 1], passes[:, 2], c='green', label='Pass', alpha=0.4)
    ax.scatter(fails[:, 0], fails[:, 1], fails[:, 2], c='red', label='Fail', alpha=0.8)

    for cluster in FAILURE_CLUSTERS:
        cx, cy, cz = cluster['center']
        ax.text(cx, cy, cz, "Fail Zone", color='red')

    ax.set_title("FSCS-ART: Adaptive Random Testing Results")
    ax.set_xlabel("Input X")
    ax.set_ylabel("Input Y")
    ax.set_zlabel("Input Z")
    ax.legend()
    plt.show()

# Run FSCS-ART test and plot
fscs_inputs, fscs_results = run_fscs_art_tests()
plot_fscs_results(fscs_inputs, fscs_results)

