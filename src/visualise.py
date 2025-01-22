import os
import numpy as np
import matplotlib.pyplot as plt


def save_results(points, inside_circle, history, output_dir):
    """Save results as animations and figures."""
    os.makedirs(output_dir, exist_ok=True)

    # Save scatter plot
    plt.figure()
    theta = np.linspace(0, 2 * np.pi, 500)
    plt.scatter(points[inside_circle, 0], points[inside_circle, 1], color='blue', label='Inside Circle')
    plt.scatter(points[~inside_circle, 0], points[~inside_circle, 1], color='red', label='Outside Circle')
    plt.plot(np.cos(theta), np.sin(theta), color='black', linestyle='--', label='Circle Boundary')
    plt.axis('equal')
    plt.legend()
    plt.title("Monte Carlo Simulation of Pi")
    plt.savefig(os.path.join(output_dir, "scatter_plot.png"))

    # Save history plot
    plt.figure()
    plt.plot(history, label="Estimated Pi")
    plt.axhline(np.pi, color='red', linestyle='--', label="Actual Pi")
    plt.xlabel("Number of Points")
    plt.ylabel("Estimated Pi")
    plt.title("Convergence of Pi")
    plt.legend()
    plt.savefig(os.path.join(output_dir, "pi_convergence.png"))
    plt.close('all')
