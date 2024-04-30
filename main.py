from csv_processing import truncate_csv_by_date
from openai_client import query_gpt
from plotting import plot_data

TARGET_DATE = "16-Aug-19"
headlines = truncate_csv_by_date("guardian_headlines.csv", TARGET_DATE)

print(headlines)

data = query_gpt(headlines)

# Add Time,Headlines,Sentiment Score,Excitement Score as first line to the data
data = "Time,Headline,Sentiment,Excitement\n" + data

print(data)
plot_data(data, TARGET_DATE)

