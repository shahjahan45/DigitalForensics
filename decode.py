import os
from PIL import Image
import stepic

# File path to the encoded image
file_path = r"D:\python Data science\Forensics\encoded_image.png"

# Check if the file exists
if os.path.exists(file_path):
    # Load the encoded image (ensure it's a PNG)
    encoded_image = Image.open(file_path)

    # Decode the hidden message
    hidden_message = stepic.decode(encoded_image)

    # Print the hidden message directly (no need to decode)
    print("The hidden message is:", hidden_message)
else:
    print(f"File not found: {file_path}")
