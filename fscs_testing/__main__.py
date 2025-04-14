from core import generate_failure_clusters
from strategies import run_random_tests, run_fscs_art_avoid_failure_tests, run_fscs_art_avoid_all_tests
from visualise import plot_results
from logger import setup_logger
from config import num_tests, seed, num_candidates, dimension_range, num_clusters, radius_range
import logging
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)
logger = logging.getLogger(__name__)

if seed is not None:
    np.random.seed(seed)
    logger.info(f"Random seed set to: {seed}")
else:
    logger.info("Random seed not set (non-deterministic run)")

logger.info("Configuration:")
logger.info(f"  Dimension Range: {dimension_range}")
logger.info(f"  Number of Candidates: {num_candidates}")
logger.info(f"  Number of Tests: {num_tests}")
logger.info(f"  Number of Clusters: {num_clusters}")
logger.info(f"  Radius Range: {radius_range}")

def main():
    setup_logger()

    logging.info("Initialising failure clusters and running tests...")
    clusters = generate_failure_clusters()

    random_inputs, random_results = run_random_tests(num_tests, clusters)
    logging.info(f"Random Testing: {sum(random_results == 'fail')} failures found.")

    fscs_avoid_fail_inputs, fscs_avoid_fail_results = run_fscs_art_avoid_failure_tests(num_tests, clusters)
    logging.info(f"FSCS-ART Testing - Max Distance from Failures: {sum(fscs_avoid_fail_results == 'fail')} failures found.")

    fscs_avoid_all_inputs, fscs_avoid_all_results = run_fscs_art_avoid_all_tests(num_tests, clusters)
    logging.info(f"FSCS-ART Testing - Max Distance all points: {sum(fscs_avoid_all_results == 'fail')} failures found.")

    result_sets = {
        "Random": (random_inputs, random_results),
        "Avoid Failures": (fscs_avoid_fail_inputs, fscs_avoid_fail_results),
        "Avoid All": (fscs_avoid_all_inputs, fscs_avoid_all_results),
    }

    plot_results(result_sets, clusters)


if __name__ == "__main__":
    main()
