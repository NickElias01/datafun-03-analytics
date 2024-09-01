"""
This module demonstrates the following skills:

1. Fetching data from the web using the `requests` module.
2. Processing the fetched data using Python collections such as lists, dictionaries, and sets.
3. Writing the processed data to different file formats, including text files, CSV, and JSON.

The module is designed to showcase the ability to interact with web data, manipulate it in memory, and then save it in various formats for further analysis or use.
"""


# Standard library imports
import csv
import pathlib 

# External library imports (requires virtual environment)
import requests  

# Local module imports
import utils_nickelias      
import nickelias_project_setup 


def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        write_txt_file(folder_name,filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        write_excel_file(folder_name,filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")


def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with file_path.open('w', encoding='utf-8') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")


def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")