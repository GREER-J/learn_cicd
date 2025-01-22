import numpy as np


class MonteCarloPi:
    def __init__(self, num_points: int):
        self.data: np.ndarray = np.random.uniform(-1, 1, (num_points, 2))

    def run(self):
        """Run the Monte Carlo simulation."""
        distances = np.sqrt(self.data[:, 0]**2 + self.data[:, 1]**2)
        inside_circle = distances <= 1
        history = 4 * np.cumsum(inside_circle) / np.arange(1, len(inside_circle) + 1)
        return inside_circle, history
