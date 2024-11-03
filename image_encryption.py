from PIL import Image
import random

def encrypt_image(image_path, output_path, key=42):
    # Load image
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    
    # Set random seed for reproducibility (based on a key)
    random.seed(key)
    
    # Step 1: Swap pixels randomly
    num_swaps = (width * height) // 2  # number of swaps to make
    for _ in range(num_swaps):
        # Randomly pick two pixels to swap
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        
        # Swap pixel values
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]
    
    # Step 2: Apply a mathematical operation (e.g., add a constant to each pixel)
    constant = 50  # Adjust constant as needed for scrambling effect
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Apply transformation and ensure pixel values stay in range [0, 255]
            r = (r + constant) % 256
            g = (g + constant) % 256
            b = (b + constant) % 256
            pixels[x, y] = (r, g, b)
    
    # Save the encrypted image
    img.save(output_path)
    print("Image encrypted and saved.")

def decrypt_image(encrypted_image_path, output_path, key=42):
    # Load encrypted image
    img = Image.open(encrypted_image_path)
    pixels = img.load()
    width, height = img.size
    
    # Set random seed for reproducibility (same key as encryption)
    random.seed(key)
    
    # Step 1: Reverse the mathematical operation
    constant = 50
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Reverse transformation
            r = (r - constant) % 256
            g = (g - constant) % 256
            b = (b - constant) % 256
            pixels[x, y] = (r, g, b)
    
    # Step 2: Reverse the pixel swapping
    swaps = []
    num_swaps = (width * height) // 2
    for _ in range(num_swaps):
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        swaps.append(((x1, y1), (x2, y2)))
    
    # Reverse swap order
    for (x1, y1), (x2, y2) in reversed(swaps):
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]
    
    # Save the decrypted image
    img.save(output_path)
    print("Image decrypted and saved.")

# Example usage
encrypt_image("input.jpg", "encrypted_image.jpg", key=12345)
decrypt_image("encrypted_image.jpg", "decrypted_image.jpg", key=12345)
