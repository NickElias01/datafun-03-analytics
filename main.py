# main.py

# Importing the necessary functions from your module
from nickelias_analytics import (fetch_and_write_txt_data, fetch_and_write_excel_data, fetch_and_write_json_data)

# Define folder name and filenames
folder_name = "data"
txt_filename = "example_text.txt"
excel_filename = "example_data.xlsx"
json_filename = "example_json.json"

# Define URLs for the data sources
text_url = "https://www.gutenberg.org/ebooks/1112.txt.utf-8"
excel_url = "https://www.gutenberg.org/ebooks/1112.txt.utf-8"
json_url = "https://www.gutenberg.org/ebooks/1112.txt.utf-8"

# Fetch and save text data
fetch_and_write_txt_data(folder_name, txt_filename, text_url)

# Fetch and save Excel data
fetch_and_write_excel_data(folder_name, excel_filename, excel_url)

# Fetch and save JSON data
fetch_and_write_json_data(folder_name, json_filename, json_url)