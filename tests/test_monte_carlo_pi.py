"""Docscring"""
import numpy as np
from monte_carlo_pi import MonteCarloPi


def test_mc_pi_data_creation():
    """Test initial creation"""
    num_points = 10
    sim = MonteCarloPi(num_points)

    assert sim.data.shape == (num_points, 2)
    assert np.all(sim.data >= -1) and np.all(sim.data <= 1)


def test_run_simulation():
    """Test simulation"""
    sim = MonteCarloPi(100)
    inside_circle, history = sim.run()
    assert len(inside_circle) == 100
    assert len(history) == 100
    assert 0 <= history[-1] <= 4
