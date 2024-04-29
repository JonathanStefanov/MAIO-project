import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from io import StringIO

def plot_data(data):
    # Sample data in CSV format

    # Create DataFrame
    try:
        df = pd.read_csv(StringIO(data), parse_dates=['Time'])
        print(df)
    except pd.errors.ParserError as e:
        print("Parsing error:", e)
        # Group by Time and calculate mean of Sentiment and Excitement
    grouped = df.groupby('Time').agg({'Sentiment': 'mean', 'Excitement': 'mean'}).reset_index()

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(grouped['Time'], grouped['Sentiment'], label='Average Sentiment', marker='o')
    plt.plot(grouped['Time'], grouped['Excitement'], label='Average Excitement', marker='o')
    plt.title('Sentiment and Excitement Scores by Time')
    plt.xlabel('Time')
    plt.ylabel('Score')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
