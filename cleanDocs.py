import os
import shutil
from PyPDF2 import PdfReader

# Define source and destination directories
source_directory = "azure-docs"
destination_directory = "docs-clean"

# Create the source directory if it doesn't exist
if not os.path.exists(source_directory):
    os.makedirs(source_directory)

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Function to check if a PDF file is not empty
def is_pdf_not_empty(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        if len(reader.pages) == 0:
            return False
        # Check for text in the first page to ensure it's not just blank pages
        first_page_text = reader.pages[0].extract_text()
        if not first_page_text or first_page_text.isspace():
            return False
        return True
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return False

# Iterate over all files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(".pdf"):
        full_path = os.path.join(source_directory, filename)
        # Check if the PDF is not empty and move it to the destination directory
        if is_pdf_not_empty(full_path):
            shutil.move(full_path, os.path.join(destination_directory, filename))
            print(f"Moved '{filename}' to {destination_directory}")
