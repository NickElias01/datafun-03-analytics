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
import utils_nickelias      
import nickelias_project_setup 


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def write_txt_file(folder_name, filename, data):
    """Write data to a text file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', encoding='utf-8') as file:
            file.write(data)
        logging.info(f"Text data saved to {file_path}")
    except IOError as e:
        logging.error(f"Error writing text file {file_path}: {e}")

def fetch_and_write_txt_data(folder_name, filename, url):
    """Fetch data from a URL and write it to a text file."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        write_txt_file(folder_name, filename, response.text)
    except requests.RequestException as e:
        logging.error(f"Failed to fetch data from {url}: {e}")

def process_text_data(folder_name, input_filename, output_filename):
    """Process text data: count words and unique words, then save summary."""
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        with file_path.open('r', encoding='utf-8') as file:
            text = file.read()
    except IOError as e:
        logging.error(f"Error reading text file {file_path}: {e}")
        return

    try:
        words = re.findall(r'\b\w+\b', text.lower())
        unique_words = set(words)
        word_count = Counter(words)
        total_words = len(words)
        unique_word_count = len(unique_words)

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

def write_csv_file(folder_name, filename, data):
    """Write data to a CSV file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        logging.info(f"CSV data saved to {file_path}")
    except IOError as e:
        logging.error(f"Error writing CSV file {file_path}: {e}")

def fetch_and_write_csv_data(folder_name, filename, url):
    """Fetch data from a URL and write it to a CSV file."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        csv_data = [row for row in csv.reader(response.text.splitlines())]
        write_csv_file(folder_name, filename, csv_data)
    except requests.RequestException as e:
        logging.error(f"Failed to fetch CSV data from {url}: {e}")
    except csv.Error as e:
        logging.error(f"Error processing CSV data: {e}")

def process_csv_data(folder_name, input_filename, output_filename):
    """Process CSV data: count rows and summarize columns."""
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        row_count = 0
        column_summaries = []
        data = []

        with file_path.open('r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            column_summaries = ['Column Summary:'] + headers

            for row in reader:
                row_count += 1
                data.append(tuple(row))

        column_counts = [0] * len(headers)
        for row in data:
            for i, value in enumerate(row):
                if value:
                    column_counts[i] += 1

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

def write_excel_file(folder_name, filename, data):
    """Write data to an Excel file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('wb') as file:
            file.write(data)
        logging.info(f"Excel data saved to {file_path}")
    except IOError as e:
        logging.error(f"Error writing Excel file {file_path}: {e}")

def fetch_and_write_excel_data(folder_name, filename, url):
    """Fetch data from a URL and write it to an Excel file."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        write_excel_file(folder_name, filename, response.content)
    except requests.RequestException as e:
        logging.error(f"Failed to fetch Excel data from {url}: {e}")

def process_excel_data(folder_name, input_filename, output_filename):
    """Process Excel data: summarize rows, columns, and numeric statistics."""
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        df = pd.read_excel(file_path)
        summary = {
            'Total Rows': len(df),
            'Total Columns': len(df.columns),
            'Column Names': list(df.columns),
            'Numeric Column Statistics': df.describe().to_string()
        }

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

def write_json_file(folder_name, filename, data):
    """Write data to a JSON file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        logging.info(f"JSON data saved to {file_path}")
    except IOError as e:
        logging.error(f"Error writing JSON file {file_path}: {e}")

def fetch_and_write_json_data(folder_name, filename, url):
    """Fetch data from a URL and write it to a JSON file."""
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

def process_json_data(folder_name, input_filename, output_filename):
    """Process JSON data: count items and summarize keys in JSON objects."""
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        with file_path.open('r', encoding='utf-8') as file:
            json_data = json.load(file)

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