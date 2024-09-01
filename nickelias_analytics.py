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
from collections import Counter
import re

# External library imports (requires virtual environment)
import requests
import pandas as pd

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

    
    def process_text_data(folder_name, input_filename, output_filename):
    # Read the text file
        file_path = pathlib.Path(folder_name).joinpath(input_filename)
        with file_path.open('r', encoding='utf-8') as file:
            text = file.read()
        
        # Clean and split the text into words
        words = re.findall(r'\b\w+\b', text.lower())  # List of words (lowercase)
        # Create a set of unique words
        unique_words = set(words)
        # Count word frequency using Counter
        word_count = Counter(words)
        # Calculate total and unique word counts
        total_words = len(words)
        unique_word_count = len(unique_words)
        
        # Write the statistics to an output text file
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding='utf-8') as output_file:
            output_file.write(f"Total Words: {total_words}\n")
            output_file.write(f"Unique Words: {unique_word_count}\n")
            output_file.write(f"\nWord Frequency:\n")
            for word, count in word_count.most_common():
                output_file.write(f"{word}: {count}\n")
        
        print(f"Text processing complete. Results saved to {output_path}")
    

# Function 2: Fetching data from a url and writing to a .csv file
def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with file_path.open('w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        print(f"CSV data saved to {file_path}")

def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the CSV content (assuming it's in a suitable format)
        csv_data = [row for row in csv.reader(response.text.splitlines())]
        # Call your write function to save the parsed CSV content
        write_csv_file(folder_name, filename, csv_data)
    else:
        print(f"Failed to fetch CSV data: {response.status_code}")


# Function 3: Fetching data from a url and writing to a .xlsx file
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


# Function 4: Fetching data from a url and writing to a JSON file
def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with file_path.open('w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)  # Save JSON data with pretty printing
        print(f"JSON data saved to {file_path}")

def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200 and response.headers['Content-Type'] == 'application/json':
        # Parse the JSON content
        json_data = response.json()
        write_json_file(folder_name, filename, json_data)
    else:
        print(f"Failed to fetch JSON data or incorrect content type: {response.status_code}")