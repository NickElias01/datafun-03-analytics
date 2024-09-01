''' 
Module: Elias Analytics - Reusable Module for My Data Analytics Projects

This module contains functions for creating a set of project folders.
'''

import pathlib
import utils_nickelias
import time

# Create a path object
project_path = pathlib.Path.cwd()
# Define the new subfolder path
data_path = project_path.joinpath('data')
# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)



# Function 1 (For item in range): Generate folders for a given range (e.g., years).
def create_folders_for_range(start_year: int, end_year:int) -> str:
    try:
        # Validating the range
        if start_year > end_year:
            raise ValueError("Start year must be less than or equal to end year.")
        
        created_folders = [] # A list to keep track of the created folders

        for year in range (start_year, end_year + 1):
            folder_path = data_path.joinpath(str(year))

            # Check if the folder already exists
            if not folder_path.exists():
                folder_path.mkdir()
                created_folders.append(str(year))

        # Condense output into a single line
        if created_folders:
            num_folders = len(created_folders)
            return f"{num_folders} new folders created for range {start_year} - {end_year}."
        else:
            return "No new folders were created as they already exist."
    
    # Checking for errors
    except ValueError as ve:
        return f"Value Error: {ve}"
    except PermissionError:
        return "Permission Error: You do not have the required permissions to create folders."
    except OSError as oe:
        return f"OSError: An error occurred while creating folders: {oe}"
    except Exception as e:
        return f"Unexpected error: {e}"



# Function 2 (For item in list): Create folders from a list of names.
def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> str:
    errors = [] #List to collect any errors
    created_folders = [] # List to keep track of created folders

    processed_list = [] # Process the folder names
    for folder_name in folder_list:
        # Apply transformations if specified
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "_")
        processed_list.append(folder_name)
    
    # Create a path for the new folder
    for folder_name in processed_list:
        folder_path = data_path.joinpath(folder_name)

        # Check if the folder already exists
        if not folder_path.exists():
            try:
                folder_path.mkdir()
                created_folders.append(folder_name)
                print(f"Folder '{folder_name}' created successfully.")
            except Exception as e:
                errors.append(f"An error occurred while creating the folder '{folder_name}': {e}")

    # Returning folder creation message
    if created_folders:
        return "Folders created successfully: " + ", ".join(created_folders)
    else:
        return "No new folders were created as they already exist."



# Function 3 (List Comprehension): Create prefixed folders by 
#   transforming a list of names and combining each with a prefix (e.g., "data-").
def create_prefixed_folders(folder_list : list, prefix : str) -> str:
    errors = [] # List to collect any errors
    created_folders = []  # List to keep track of created folders

    # Ensure list of folders is not empty
    if not folder_list:
        return "The list of folder names is empty."
    
    for folder_name in folder_list:
        # Create a path for the new folder with the prefix
        folder_path = data_path.joinpath(f"{prefix}{folder_name}")

        # Check if the folder already exists
        if not folder_path.exists():
            try:
                folder_path.mkdir()
                created_folders.append(f"{prefix}{folder_name}")
            except Exception as e:
                errors.append(f"Error creating folder '{prefix}{folder_name}': {e}")
    
    # Returning folder creation message
    if created_folders:
        return "Prefixed folders created successfully: " + ", ".join(created_folders)
    else:
        return "No new prefixed folders were created as they already exist."
    

# Function 4 (While Loop): Create a new folder every 1 second for given duration 
def create_folders_periodically(duration_secs: int) -> None:
    interval = 1  # The fixed interval between folder creations in seconds
    start_time = time.time()
    end_time = start_time + duration_secs
    folder_index = 1  # Start folder creation at folder_1
    folders_created = 0  # Initialize folder count

    while time.time() < end_time:
        folder_name = f"folder_{folder_index}"
        folder_path = data_path.joinpath(folder_name)

        # Attempt to create the folder, increment the folder count if creation is successful
        try:
            folder_path.mkdir()
            folders_created += 1  
        except FileExistsError:
            # Folder already exists, no message printed
            pass
        except Exception as e:
            print(f"An error occurred while creating the folder '{folder_name}': {e}")
            break  # Stop creating folders if an unexpected error occurs

        # Pause the function for the value of interval in seconds
        time.sleep(interval)
        folder_index += 1  # Increment the folder index after each attempt

    # Returning folder creation message
    print(f"{folders_created} new folders created in {duration_secs} seconds")



def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {utils_nickelias.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    result = create_folders_for_range(start_year=2020, end_year=2025)
    print(result)

    # Call function 2 to create folders given a list
    folder_names = ['folder a', 'folder b', 'folder c']
    create_folders_from_list(folder_names, to_lowercase=True, remove_spaces=True)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json', 'xml']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)


if __name__ == '__main__':
    main()