"""Main file for CICD learn project"""
from monte_carlo_pi import MonteCarloPi
from plot_animation import do_animation
from video_writer import generate_mp4_from_figures


def main():
    """Run program"""
    # Step 1: Run simulation
    num_points = 100
    simulation = MonteCarloPi(num_points)
    inside_circle, history = simulation.run()

    # Define directories
    output_dir = './out'
    figures_dir = "./out/figures"  # Directory to store PNG images

    # Step 3: Generate animation frames
    do_animation(simulation.data, inside_circle, history, figures_dir)

    # Step 4: Create MP4 video from animation frames
    generate_mp4_from_figures(figures_dir, output_dir, batch_size=num_points)


if __name__ == "__main__":
    main()
