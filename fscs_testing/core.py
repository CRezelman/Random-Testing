from config import dimension_range, num_clusters, radius_range, seed
import numpy as np
import logging

logger = logging.getLogger(__name__)

def generate_failure_clusters():
    clusters = []
    logger.info(f"Generating {num_clusters} failure clusters with radius range {radius_range}")
    for i in range(num_clusters):
        centre = np.random.uniform(0, dimension_range, 3)
        radius_frac = np.random.uniform(*radius_range)
        radius = dimension_range * radius_frac
        clusters.append({'center': centre, 'radius': radius})
        logger.info(f"Cluster {i+1}: Centre={centre}, Radius={radius:.2f} (Fraction={radius_frac:.2f})")
    return clusters

def mock_api(x, y, z, clusters):
    for cluster in clusters:
        cx, cy, cz = cluster['center']
        r = cluster['radius']
        if np.linalg.norm([x - cx, y - cy, z - cz]) < r:
            return "fail"
    return "pass"
