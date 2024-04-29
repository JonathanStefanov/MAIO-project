import pandas as pd
from io import StringIO
import numpy as np

def truncate_csv_by_date(file_path, target_date):
    """
    Reads a CSV, finds a specific date, and creates a string of CSV formatted text for lines around the specified date,
    sampling three headlines per day for 7 days before and after the target date.

    Args:
    file_path (str): Path to the input CSV file.
    target_date (str): The date to search for in the format 'd-MMM-yy' (e.g., '4-Jul-20').

    Returns:
    str: CSV formatted string containing the required rows.
    """
    # Read the CSV file without date parsing to inspect the date formats
    df = pd.read_csv(file_path)
    
    # Attempt to convert the 'Time' column to datetime, coercing errors
    df['Time'] = pd.to_datetime(df['Time'], format='%d-%b-%y', errors='coerce')

    # Check for any rows where 'Time' is NaT due to parsing errors
    if df['Time'].isnull().any():
        print("There are dates that could not be parsed. They have been set to NaT.")

    # Define the target date in datetime format
    target_datetime = pd.to_datetime(target_date, format='%d-%b-%y', errors='coerce')
    
    if pd.isna(target_datetime):
        print("Target date is invalid or could not be parsed.")
        return None

    # Calculate date ranges
    start_date = target_datetime - pd.DateOffset(days=7)
    end_date = target_datetime + pd.DateOffset(days=7)

    # Filter the DataFrame for the 15-day range
    mask = (df['Time'] >= start_date) & (df['Time'] <= end_date)
    date_range_df = df.loc[mask]

    # Sample up to 3 random entries per day
    sampled_df = date_range_df.groupby('Time').apply(lambda x: x.sample(min(len(x), 3))).reset_index(drop=True)
    
    # Convert DataFrame to CSV formatted string
    output = StringIO()
    sampled_df.to_csv(output, index=False)
    return output.getvalue()
