"""Creates a collection of figures for animation, one from each frame"""
import os
import numpy as np
import matplotlib.pyplot as plt


def do_animation(points, inside_circle, history, figures_dir):
    """Generate frames for an animation and save them as individual plots."""
    # Ensure the output directory exists
    os.makedirs(figures_dir, exist_ok=True)

    # Set up the plot
    plt.figure(figsize=(15, 10))
    theta = np.linspace(0, 2 * np.pi, 500)  # Circle boundary

    for i in range(1, len(points) + 1):  # Start from 1 for 0 to i slices
        plt.clf()

        # Top subplot: Scatter plot of points
        plt.subplot(2, 1, 1)
        plt.scatter(points[:i][inside_circle[:i], 0],
                    points[:i][inside_circle[:i], 1],
                    color='blue', label='Inside Circle')

        plt.scatter(points[:i][~inside_circle[:i], 0],
                    points[:i][~inside_circle[:i], 1],
                    color='red', label='Outside Circle')

        plt.plot(np.cos(theta), np.sin(theta),
                 color='black',
                 linestyle='--',
                 label='Circle Boundary')
        plt.axis('equal')
        plt.legend()
        plt.title("Monte Carlo Simulation of Pi")
        plt.xlabel('E')
        plt.ylabel('N')

        # Bottom subplot: Line graph of π estimation
        plt.subplot(2, 1, 2)
        plt.plot(range(1, i + 1), history[:i], label="Estimated Pi")
        plt.axhline(np.pi, color='red', linestyle='--', label="Actual Pi")
        plt.xlabel("Number of Points")
        plt.ylabel("Estimated Pi")
        plt.title("Convergence of Pi")
        plt.legend()

        # Save the frame
        frame_path = os.path.join(figures_dir, f"frame_{i:04d}.png")  # Zero-padded filenames
        plt.savefig(frame_path)

    plt.close()  # Close the figure to free up resources
