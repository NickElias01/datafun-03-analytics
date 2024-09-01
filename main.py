# main.py

# Importing the necessary functions from your module
from nickelias_analytics import (
    fetch_and_write_txt_data,
    fetch_and_write_excel_data,
)

# Define folder name and filenames
folder_name = "data"
txt_filename = "example_text.txt"
excel_filename = "example_data.xlsx"

# Define URLs for the data sources
text_url = "https://www.gutenberg.org/ebooks/1112.txt.utf-8"
excel_url = "https://www.gutenberg.org/ebooks/1112.txt.utf-8"

# Fetch and save text data
fetch_and_write_txt_data(folder_name, txt_filename, text_url)

# Fetch and save Excel data
fetch_and_write_excel_data(folder_name, excel_filename, excel_url)