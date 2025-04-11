from core import generate_failure_clusters
from strategies import run_random_tests, run_fscs_art_tests
from visualise import plot_results
from logger import setup_logger
from config import num_tests, seed
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

def main():
    setup_logger()
    logging.info("Initialising failure clusters and running tests...")
    clusters = generate_failure_clusters()

    random_inputs, random_results = run_random_tests(num_tests, clusters)
    logging.info(f"Random Testing: {sum(random_results == 'fail')} failures found.")

    fscs_inputs, fscs_results = run_fscs_art_tests(num_tests, clusters)
    logging.info(f"FSCS-ART Testing: {sum(fscs_results == 'fail')} failures found.")

    plot_results(random_inputs, random_results, fscs_inputs, fscs_results, clusters)

if __name__ == "__main__":
    main()
