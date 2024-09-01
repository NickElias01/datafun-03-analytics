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
import json

# External library imports (requires virtual environment)
import requests  

# Local module imports
import utils_nickelias      
import nickelias_project_setup 


# Function 1: Fetching data from a url and writing to a .txt file
def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with file_path.open('w', encoding='utf-8') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        write_txt_file(folder_name,filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")


# Function 2: Fetching data from a url and writing to a .xlsx file
def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        write_excel_file(folder_name,filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")


# Function 3: Fetching data from a url and writing to a JSON file
def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with file_path.open('w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)  # Save JSON data with pretty printing
        print(f"JSON data saved to {file_path}")

def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the JSON content
        json_data = response.json()
        # Call your write function to save the parsed JSON content
        write_json_file(folder_name, filename, json_data)
    else:
        print(f"Failed to fetch JSON data: {response.status_code}")