from src.monte_carlo_pi import MonteCarloPi
from src.visualise import save_results
from src.plot_animation import do_animation
from src.video_writer import generate_mp4_from_figures


def main():
    # Step 1: Run simulation
    num_points = 500
    simulation = MonteCarloPi(num_points)
    inside_circle, history = simulation.run()

    # Define directories
    output_dir = './out'
    figures_dir = "./out/figures"  # Directory to store PNG images

    # Step 2: Save scatter plot and convergence results
    save_results(simulation.data, inside_circle, history, output_dir)

    # Step 3: Generate animation frames
    do_animation(simulation.data, inside_circle, history, figures_dir)

    # Step 4: Create MP4 video from animation frames
    generate_mp4_from_figures(figures_dir, output_dir, batch_size=num_points)


if __name__ == "__main__":
    main()
