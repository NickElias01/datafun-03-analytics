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

def process_csv_data(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    
    # Initialize variables
    row_count = 0
    column_summaries = []
    data = []
    
    # Read CSV file and process data
    with file_path.open('r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Extract header row
        column_summaries = ['Column Summary:'] + headers  # Initialize column summaries
        
        for row in reader:
            row_count += 1
            data.append(tuple(row))  # Convert each row to a tuple
    
    # Analyze data (example: count entries per column)
    column_counts = [0] * len(headers)
    for row in data:
        for i, value in enumerate(row):
            if value:  # Count non-empty values
                column_counts[i] += 1
    
    # Write the results to an output text file
    output_path = pathlib.Path(folder_name).joinpath(output_filename)
    with output_path.open('w', encoding='utf-8') as output_file:
        output_file.write(f"Total Rows: {row_count}\n")
        output_file.write(f"\nColumn Summaries:\n")
        for header, count in zip(headers, column_counts):
            output_file.write(f"{header}: {count} entries\n")
    
    print(f"CSV processing complete. Results saved to {output_path}")


# Function 3: Fetching data from a url and writing to a .xlsx file
def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name,filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

def process_excel_data(folder_name, input_filename, output_filename):
    # Read the Excel file
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    df = pd.read_excel(file_path)
    
    # Perform analysis
    summary = {}
    summary['Total Rows'] = len(df)
    summary['Total Columns'] = len(df.columns)
    summary['Column Names'] = list(df.columns)
    
    # Example of calculating basic statistics for numeric columns
    numeric_summary = df.describe().to_string()
    summary['Numeric Column Statistics'] = numeric_summary
    
    # Write the analysis to an output text file
    output_path = pathlib.Path(folder_name).joinpath(output_filename)
    with output_path.open('w', encoding='utf-8') as output_file:
        output_file.write(f"Summary of Excel Data:\n")
        for key, value in summary.items():
            if isinstance(value, str):
                output_file.write(f"{key}:\n{value}\n\n")
            else:
                output_file.write(f"{key}: {value}\n")
    
    print(f"Excel data processing complete. Results saved to {output_path}")


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

def process_json_data(folder_name, input_filename, output_filename):
    # Read the JSON file
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    with file_path.open('r', encoding='utf-8') as file:
        json_data = json.load(file)
    
    # Extract relevant information
    summary = {}
    summary['Number of Items'] = len(json_data)
    
    # Example: Extracting and summarizing information from the JSON data
    if isinstance(json_data, list):
        if len(json_data) > 0 and isinstance(json_data[0], dict):
            keys = json_data[0].keys()
            summary['Keys in JSON objects'] = list(keys)
    
    # Write the summary to an output text file
    output_path = pathlib.Path(folder_name).joinpath(output_filename)
    with output_path.open('w', encoding='utf-8') as output_file:
        output_file.write(f"Summary of JSON Data:\n")
        for key, value in summary.items():
            if isinstance(value, str):
                output_file.write(f"{key}:\n{value}\n\n")
            else:
                output_file.write(f"{key}: {value}\n")
    
    print(f"JSON data processing complete. Results saved to {output_path}")