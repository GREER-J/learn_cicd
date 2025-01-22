"""Monte carlo simulation of pi"""
import numpy as np


class MonteCarloPi:
    """Monte carlo simulation of pi"""
    def __init__(self, num_points: int):
        self.generate_data(num_points)

    def generate_data(self, num_points):
        """Generates data

        Args:
            num_points (int): length of data row
        """
        self.data: np.ndarray = np.random.uniform(-1, 1, (num_points, 2))

    def run(self):
        """Run the Monte Carlo simulation."""
        distances = np.sqrt(self.data[:, 0]**2 + self.data[:, 1]**2)
        inside_circle = distances <= 1
        n_inside_circ = np.cumsum(inside_circle)
        n = np.arange(1, len(inside_circle) + 1)
        history = 4 * n_inside_circ / n
        return inside_circle, history
