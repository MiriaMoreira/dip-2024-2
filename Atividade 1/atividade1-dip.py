import argparse
import numpy as np
import cv2

def generate_image(seed, width, height, mean, std):
    """
    Generates a grayscale image with pixel values sampled from a normal distribution.

    Args:
        seed (int): Random seed for reproducibility (student's registration number).
        width (int): Width of the generated image.
        height (int): Height of the generated image.
        mean (float): Mean of the normal distribution.
        std (float): Standard deviation of the normal distribution.

    Returns:
        image (numpy.ndarray): The generated image.
    """
    ### START CODE HERE ###
    ### TODO
    ### END CODE HERE ###
    np.random.seed(seed)  # Set the seed for reproducibility
    image = np.random.normal(loc=mean, scale=std, size=(height, width)) # corrected size order
    image = np.clip(image, 0, 255).astype(np.uint8)
    return image

def main():
    # Argument parser
    parser = argparse.ArgumentParser(description="Generate an image with pixel values sampled from a normal distribution.")

    parser.add_argument('--registration_number', type=int, default=19111285, required=False, help="Student's registration number (used as seed)")
    parser.add_argument('--width', type=int, default=512, required=False, help="Width of the image")
    parser.add_argument('--height', type=int, default=512, required=False, help="Height of the image")
    parser.add_argument('--mean', type=float, default=256, required=False, help="Mean of the normal distribution")
    parser.add_argument('--std', type=float, required=False, default=50, help="Standard deviation of the normal distribution")
    parser.add_argument('--output', type=str, required=False, default="imagem_atv1.png", help="Path to save the generated image")

    args = parser.parse_args()

    # Generate the image
    image = generate_image(args.registration_number, args.width, args.height, args.mean, args.std)

    # Save the generated image
    cv2.imwrite(args.output, image)

    print(f"Image successfully generated and saved to {args.output}")

if __name__ == "__main__":
    main()