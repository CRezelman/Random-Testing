import numpy as np
from config import dimension_range
from core import mock_api

def run_random_tests(n_tests, clusters):
    all_inputs, all_results = [], []
    for _ in range(n_tests):
        candidate = np.random.uniform(0, dimension_range, 3)
        result = mock_api(*candidate, clusters)
        all_inputs.append(candidate)
        all_results.append(result)
    return np.array(all_inputs), np.array(all_results)

def run_fscs_art_avoid_failure_tests(n_tests, clusters, num_candidates=50):
    failure_set = []
    all_inputs = []
    all_results = []

    for _ in range(n_tests):
        test_input = fscs_art_generate(failure_set, num_candidates)
        result = mock_api(*test_input, clusters)
        all_inputs.append(test_input)
        all_results.append(result)
        if result == "fail":
            failure_set.append(test_input.tolist())
    return np.array(all_inputs), np.array(all_results)

def run_fscs_art_avoid_all_tests(n_tests, clusters, num_candidates=50):
    tested_points = []
    all_inputs = []
    all_results = []

    for _ in range(n_tests):
        test_input = fscs_art_generate(tested_points, num_candidates)
        result = mock_api(*test_input, clusters)
        all_inputs.append(test_input)
        all_results.append(result)
        tested_points.append(test_input.tolist())
    return np.array(all_inputs), np.array(all_results)


def fscs_art_generate(avoid_set, num_candidates=1000):
    candidates = np.random.uniform(0, dimension_range, (num_candidates, 3))
    if not avoid_set:
        return candidates[np.random.randint(num_candidates)]

    avoid_array = np.array(avoid_set)
    max_min_distance = -1
    best_candidate = None

    for candidate in candidates:
        distances = np.linalg.norm(avoid_array - candidate, axis=1)
        min_distance = np.min(distances)
        if min_distance > max_min_distance:
            max_min_distance = min_distance
            best_candidate = candidate
    return best_candidate
