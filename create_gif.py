import imageio.v3 as iio
from PIL import Image
import numpy as np

def resize_images(image_files, target_size=(500, 500)):
    """Resize images to the target size and return them as numpy arrays."""
    resized_images = []
    for file in image_files:
        img = Image.open(file)  # Open image
        img = img.resize(target_size)  # Resize image
        img_array = np.array(img)  # Convert to NumPy array
        resized_images.append(img_array)  # Store the resized image
    return resized_images

def create_gif(image_files, output_name='output.gif', duration=500, loop=0):
    """Creates a GIF from a list of image files."""
    images = resize_images(image_files)  # Ensure all images are the same size

    if not images:
        print("No images found!")
        return

    iio.imwrite(output_name, images, duration=duration, loop=loop)  # Create GIF
    print(f"GIF saved as {output_name}")

# Example usage
filenames = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg']  # Update with your images
create_gif(filenames, 'my_animation.gif', duration=500, loop=0)
