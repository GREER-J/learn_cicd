"""Renders animation from collection of figures"""
import os
import time
import imageio.v3 as imageio


def generate_mp4_from_figures(figures_dir, output_dir, batch_size=350):
    """
    Generate MP4 video files from PNG figures in batches.

    Parameters:
    - figures_dir: Directory containing the PNG figures.
    - output_dir: Directory to save the resulting MP4 files.
    - batch_size: Number of images per MP4 file.
    """
    start_time = time.time()
    images = []
    iset = 0

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Collect all figure filenames and sort them
    filenames = sorted([f for f in os.listdir(figures_dir) if f.endswith('.png')])

    for i, filename in enumerate(filenames, start=1):
        filepath = os.path.join(figures_dir, filename)
        images.append(imageio.imread(filepath))

        # Save batch when batch size is reached
        if (i % batch_size) == 0:
            output_file = os.path.join(output_dir, f'results_{iset:03d}.mp4')
            imageio.imwrite(output_file, images, fps=10)  # Corrected to imwrite
            print(f"Saved {output_file}")
            iset += 1
            images = []

    # Save any remaining images
    if images:
        output_file = os.path.join(output_dir, f'results_{iset:03d}.mp4')
        imageio.imwrite(output_file, images, fps=10)
        print(f"Saved {output_file}")

    elapsed_time = time.time() - start_time
    print(f"MP4 generation complete in {elapsed_time:.2f} seconds.")
