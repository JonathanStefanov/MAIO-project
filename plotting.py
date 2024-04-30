import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

def plot_data(data, target_date):
    try:
        # Convert string data to a DataFrame
        df = pd.read_csv(StringIO(data), parse_dates=['Time'])
        
    except pd.errors.ParserError as e:
        print("Error in data format. Attempting to ignore bad lines.")
        # Attempt to filter out incorrect rows
        data_clean = StringIO('\n'.join([line for line in data.split('\n') if len(line.split(',')) == 4]))
        df = pd.read_csv(data_clean, parse_dates=['Time'])

    # Ensure that Time column is a datetime object
    if df['Time'].dtype != '<M8[ns]':  # Check if 'Time' column is not datetime type
        df['Time'] = pd.to_datetime(df['Time'], errors='coerce')  # Coerce errors to handle invalid formats

    # Convert Sentiment and Excitement columns to numeric, ignoring non-numeric rows
    df['Sentiment'] = pd.to_numeric(df['Sentiment'], errors='coerce')
    df['Excitement'] = pd.to_numeric(df['Excitement'], errors='coerce')
    
    # Drop rows where datetime conversion or numeric conversion failed
    df.dropna(subset=['Time', 'Sentiment', 'Excitement'], inplace=True)

    # Group by Time and calculate mean of Sentiment and Excitement
    grouped = df.groupby('Time').agg({'Sentiment': 'mean', 'Excitement': 'mean'}).reset_index()

    # Parse the target date string into datetime format
    target_datetime = pd.to_datetime(target_date, format='%d-%b-%y', errors='coerce')
    if pd.isna(target_datetime):
        print("Target date is invalid or could not be parsed.")
        return

    # Plotting
    plt.figure(figsize=(20, 5))

    # Plot Sentiment
    plt.subplot(1, 2, 1)
    plt.plot(grouped['Time'], grouped['Sentiment'], label='Average Sentiment', marker='o')
    plt.axhline(0, color='red', linestyle='--')
    plt.axvline(x=target_datetime, color='black', linestyle='--')
    plt.title('Average Sentiment Scores by Time')
    plt.xlabel('Time')
    plt.ylabel('Sentiment Score')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    # Plot Excitement
    plt.subplot(1, 2, 2)
    plt.plot(grouped['Time'], grouped['Excitement'], label='Average Excitement', marker='o')
    plt.axvline(x=target_datetime, color='black', linestyle='--')
    plt.title('Average Excitement Scores by Time')
    plt.xlabel('Time')
    plt.ylabel('Excitement Score')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Example usage:
# plot_data(data, TARGET_DATE)
