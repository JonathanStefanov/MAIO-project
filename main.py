from csv_processing import truncate_csv_by_date
from openai_client import query_gpt
from plotting import plot_data
headlines = truncate_csv_by_date("guardian_headlines.csv", "4-Jul-20")

data = query_gpt(headlines)

# Add Time,Headlines,Sentiment Score,Excitement Score as first line to the data
data = "Time,Headline,Sentiment,Excitement\n" + data

print(data)
plot_data(data)

