import os
import pandas as pd


def load_data():
    # Get the current script's directory
    current_script_directory = os.path.dirname(__file__)

    # Navigate to the parent directory
    parent_directory = os.path.abspath(
        os.path.join(current_script_directory, '..'))

    # Specify the name of the data folder
    data_folder_name = 'data'

    # Specify the path to the data folder
    data_folder_path = os.path.join(parent_directory, data_folder_name)

    # Initialize an empty DataFrame to store the combined data
    combined_data = pd.DataFrame()

    # Iterate through each file in the data folder
    for root, dirs, files in os.walk(data_folder_path):
        for file in files:
            file_path = os.path.join('..', 'data', file)
            df = pd.read_csv(file_path)
            # add date time from file name
            date_str = file.split('_')[-1].replace('.csv', '')
            df['date'] = pd.to_datetime(date_str, format="%Y-%m-%d")
            combined_data = combined_data._append(df, ignore_index=True)

    return combined_data
