# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 00:40:31 2023

@author: arslanu
"""

from PIL import Image
import pytesseract
import os

# Set the path to the Tesseract executable
# Replace with your Tesseract OCR installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the folder containing images
folder_path = r'C:/ocr/images'

# Iterate over each file in the folder
for file_name in os.listdir(folder_path):
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Check if the file is an image (you can add more extensions if needed)
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        # Open the image with PIL
        img = Image.open(file_path)

        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(img)

        # Get the base name of the image file (without extension)
        base_name = os.path.splitext(file_name)[0]

        # Create a path for the new text file with the same base name as the image
        text_file_path = os.path.join(folder_path, base_name + '.txt')

        # Write the extracted text to a file
        with open(text_file_path, 'w') as file:
            file.write(text)

        print(f"Text extracted and saved to {text_file_path}")
