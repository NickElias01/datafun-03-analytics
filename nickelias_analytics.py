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
import logging

# External library imports (requires virtual environment)
import requests
import pandas as pd

# Local module imports   
import nickelias_project_setup
import utils_nickelias


# Configure logging to replace print statements and track program execution
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Write data to a text file.
def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        # Try opening the file and writing the data to it
        with file_path.open('w', encoding='utf-8') as file:
            file.write(data)
        logging.info(f"Text data saved to {file_path}") # Log successful write operation
    except IOError as e:
        logging.error(f"Error writing text file {file_path}: {e}")

# Fetch data from a URL and write it to a text file.
def fetch_and_write_txt_data(folder_name, filename, url, verify=True):
    """Fetch data from a URL and write it to a text file."""
    try:
        # Fetch the data from the URL, with SSL verification enabled
        response = requests.get(url, verify=True)  # Enable SSL verification
        response.raise_for_status()  # Raise HTTPError for bad responses
        response.encoding = 'utf-8'  # Ensure the response is interpreted as UTF-8
        write_txt_file(folder_name, filename, response.text) # Save the fetched data to a text file
    except requests.RequestException as e:
        # Log any errors encountered during data fetching
        logging.error(f"Failed to fetch data from {url}: {e}")

# Process text data: count words and unique words, then save summary.
def process_text_data(folder_name, input_filename, output_filename):
    
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        # Try opening the file and reading its contents
        with file_path.open('r', encoding='utf-8') as file:
            text = file.read()
    except IOError as e:
        # Log any errors encountered during file reading and exit the function
        logging.error(f"Error reading text file {file_path}: {e}")
        return

    try:
        # Extract words from the text and count occurrences
        words = re.findall(r'\b\w+\b', text.lower())
        unique_words = set(words)
        word_count = Counter(words)
        total_words = len(words)
        unique_word_count = len(unique_words)

        # Write the summary of word counts to the output file
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding='utf-8') as output_file:
            output_file.write(f"Total Words: {total_words}\n")
            output_file.write(f"Unique Words: {unique_word_count}\n")
            output_file.write(f"\nWord Frequency:\n")
            for word, count in word_count.most_common():
                output_file.write(f"{word}: {count}\n")
        logging.info(f"Text processing complete. Results saved to {output_path}")
    except Exception as e:
        logging.error(f"Error processing text data: {e}")

# Write data to a CSV file.
def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        logging.info(f"CSV data saved to {file_path}")
    except IOError as e:
        logging.error(f"Error writing CSV file {file_path}: {e}")

# Fetch data from a URL and write it to a CSV file.
def fetch_and_write_csv_data(folder_name, filename, url, verify=True):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        # Parse the CSV data and save it to a file
        csv_data = [row for row in csv.reader(response.text.splitlines())]
        write_csv_file(folder_name, filename, csv_data)
    except requests.RequestException as e:
        logging.error(f"Failed to fetch CSV data from {url}: {e}")
    except csv.Error as e:
        logging.error(f"Error processing CSV data: {e}")

# Process CSV data: count rows and summarize columns.
def process_csv_data(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        row_count = 0
        column_summaries = []
        data = []

        with file_path.open('r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader) # Read the header row
            column_summaries = ['Column Summary:'] + headers

            for row in reader:
                row_count += 1 # Count rows
                data.append(tuple(row))

        # Summarize each column by counting non-empty entries
        column_counts = [0] * len(headers)
        for row in data:
            for i, value in enumerate(row):
                if value:
                    column_counts[i] += 1

        # Write the summary to the output file
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding='utf-8') as output_file:
            output_file.write(f"Total Rows: {row_count}\n")
            output_file.write(f"\nColumn Summaries:\n")
            for header, count in zip(headers, column_counts):
                output_file.write(f"{header}: {count} entries\n")
        logging.info(f"CSV processing complete. Results saved to {output_path}")
    except IOError as e:
        logging.error(f"Error reading or writing CSV file: {e}")
    except csv.Error as e:
        logging.error(f"Error processing CSV data: {e}")


# Write data to an Excel file.
def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('wb') as file:
            file.write(data)
        logging.info(f"Excel data saved to {file_path}")
    except IOError as e:
        logging.error(f"Error writing Excel file {file_path}: {e}")

# Fetch data from a URL and write it to an Excel file.
def fetch_and_write_excel_data(folder_name, filename, url, verify=True):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        write_excel_file(folder_name, filename, response.content)
    except requests.RequestException as e:
        logging.error(f"Failed to fetch Excel data from {url}: {e}")

# Process Excel data: summarize rows, columns, and numeric statistics.
def process_excel_data(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        df = pd.read_excel(file_path)
        summary = {
            'Total Rows': len(df),
            'Total Columns': len(df.columns),
            'Column Names': list(df.columns),
            'Numeric Column Statistics': df.describe().to_string()
        }

        # Write the summary to the output file
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding='utf-8') as output_file:
            output_file.write(f"Summary of Excel Data:\n")
            for key, value in summary.items():
                if isinstance(value, str):
                    output_file.write(f"{key}:\n{value}\n\n")
                else:
                    output_file.write(f"{key}: {value}\n")
        logging.info(f"Excel data processing complete. Results saved to {output_path}")
    except IOError as e:
        logging.error(f"Error reading Excel file {file_path}: {e}")
    except pd.errors.EmptyDataError:
        logging.error(f"Excel file is empty or not readable: {file_path}")
    except pd.errors.ExcelFileError as e:
        logging.error(f"Error reading Excel file {file_path}: {e}")


# Write data to a JSON file.
def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        logging.info(f"JSON data saved to {file_path}")
    except IOError as e:
        logging.error(f"Error writing JSON file {file_path}: {e}")

# Fetch data from a URL and write it to a JSON file.
def fetch_and_write_json_data(folder_name, filename, url, verify=True):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        if response.headers['Content-Type'] == 'application/json':
            json_data = response.json()
            write_json_file(folder_name, filename, json_data)
        else:
            logging.warning(f"Incorrect content type for JSON data: {response.headers['Content-Type']}")
    except requests.RequestException as e:
        logging.error(f"Failed to fetch JSON data from {url}: {e}")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON data: {e}")

# Process JSON data: count items and summarize keys in JSON objects.
def process_json_data(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        with file_path.open('r', encoding='utf-8') as file:
            json_data = json.load(file)

        # Summarize the JSON data by counting the top-level keys and their types
        summary = {'Number of Items': len(json_data)}

        if isinstance(json_data, list) and len(json_data) > 0 and isinstance(json_data[0], dict):
            summary['Keys in JSON objects'] = list(json_data[0].keys())

        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding='utf-8') as output_file:
            output_file.write(f"Summary of JSON Data:\n")
            for key, value in summary.items():
                if isinstance(value, str):
                    output_file.write(f"{key}:\n{value}\n\n")
                else:
                    output_file.write(f"{key}: {value}\n")
        logging.info(f"JSON data processing complete. Results saved to {output_path}")
    except IOError as e:
        logging.error(f"Error reading JSON file {file_path}: {e}")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON data: {e}")


# Main function to demonstrate module capabilities.
def main():

    # Print byline from imported module
    print(f"Byline: {utils_nickelias.byline}")
    
    # Define the prefix for the folders
    prefix = 'data-'

    # Define the folder names for each data type
    folder_names = ['txt', 'csv', 'excel', 'json']

    # Create folders using the prefixed naming
    result = nickelias_project_setup.create_prefixed_folders(folder_names, prefix)
    print(result)

    # Define the base directory relative to the script's location
    base_dir = pathlib.Path(__file__).parent.joinpath('data')

    # Define URLs for data fetching
    txt_url = 'https://www.gutenberg.org/files/1513/1513-0.txt'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv'
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'
    json_url = 'http://api.open-notify.org/astros.json'

    # Define filenames for data storage
    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls'
    json_filename = 'data.json'

    # Define full paths for each folder
    txt_folder = pathlib.Path(base_dir).joinpath(f'{prefix}txt')
    csv_folder = pathlib.Path(base_dir).joinpath(f'{prefix}csv')
    excel_folder = pathlib.Path(base_dir).joinpath(f'{prefix}excel')
    json_folder = pathlib.Path(base_dir).joinpath(f'{prefix}json')

    # Fetch and write data to files
    fetch_and_write_txt_data(txt_folder, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder, json_filename, json_url)

    # Process the fetched data
    process_text_data(txt_folder, txt_filename, 'results_txt.txt')
    process_csv_data(csv_folder, csv_filename, 'results_csv.txt')
    process_excel_data(excel_folder, excel_filename, 'results_xls.txt')
    process_json_data(json_folder, json_filename, 'results_json.txt')

    print("Data fetching and processing complete.")


if __name__ == "__main__":
    main()