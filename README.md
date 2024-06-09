# DBS Bank Project (MAIO)
This repository contains the code for the DBS Bank project, part of the Management of AI in Organizations course. The project focuses on analyzing and visualizing sentiment and excitement from news headlines using different AI models.

## Overview
The Python script included in this repository performs several key functions:

1. **CSV Processing**: The script starts by truncating a CSV file containing news headlines to include only those up to a specified date, using the `truncate_csv_by_date` function from the `csv_processing` custom module.

2. **Data Querying**: It then queries sentiment analysis models from different sources:
   - Initially, the script used the `query_gpt` function from the `openai_client` custom module to fetch AI-generated sentiment data.
   - Currently, it uses the `query_gemini` function from the `gemini_client` custom module to fetch the data.

3. **Data Manipulation**: After fetching the data, the script counts the number of lines and adds a header to the data for better understanding and structure.

4. **Data Visualization**: Finally, it visualizes the sentiment and excitement scores over time using the `plot_data` function from the `plotting` custom module.
