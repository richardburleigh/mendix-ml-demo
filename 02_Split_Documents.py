import os
import re
from bs4 import BeautifulSoup


def split_md_files(folder_path):
    # Create a new folder to store the split files
    output_folder = os.path.join(folder_path, "split_files")
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all HTML files in the folder
    html_files = [f for f in os.listdir(folder_path) if f.endswith(".html")]

    for file_name in html_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r", encoding="utf-8") as file:
            # Read the content of the HTML file
            content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(content, "html.parser")

        # Find all the paragraphs
        paragraphs = soup.find_all("p")

        # Split the content based on the paragraphs
        for i, paragraph in enumerate(paragraphs):
            # Generate a new file name
            base_name = os.path.splitext(file_name)[0]
            new_file_name = f"{base_name}_part{i+1}.html"
            new_file_path = os.path.join(output_folder, new_file_name)

            # Write the paragraph to a new file
            with open(new_file_path, "w", encoding="utf-8") as new_file:
                new_file.write(str(paragraph))

            print(f"Split file created: {new_file_path}")

        print(f"Original file deleted: {file_path}")

    print("All files split successfully!")

# Provide the folder path containing the Markdown files
folder_path = "data"
split_md_files(folder_path)
