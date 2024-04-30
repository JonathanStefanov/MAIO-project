import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
def query_gpt(query: str):
        
    load_dotenv()

    # Initialize the OpenAI client using the API key from environment variables
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    # Create a chat completion
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": 
         """
        You are a NLP that analyses the sentiment and excitement analysis of 50 news headlines while adhering to CSV formatting standards. The output should use commas as column separators, and headlines must be free of commas to ensure data integrity.

        Input Format:

        CSV file or structured list: Each row contains a publication date and the text of a headline.
        Processing Steps:

        Read Input Data: Extract headlines and their associated publication dates.
        Remove Commas from Headlines: Replace all commas in the headlines with spaces or other suitable characters to avoid formatting issues in CSV output.
        Sentiment Analysis: Assign a sentiment score to each headline, ranging from -5 (very negative) to +5 (very positive).
        Excitement Analysis: Determine an excitement score for each headline, from 0 (least exciting) to 10 (most exciting).
        Output Format:

        Format the output as a CSV where each row contains:
        Date: Publication date of the headline.
        Headline: Modified headline text with all commas removed.
        Sentiment Score: Numerical sentiment score.
        Excitement Score: Numerical excitement score.
        Example Input:

        Date,Headline
        2023-04-30,"Exciting developments in AI technology, says expert"
        2023-04-30,"Market crashes, investors worried"
        Example Output:

        Date,Headline,Sentiment Score,Excitement Score
        2023-04-30,Exciting developments in AI technology says expert,3,8
        2023-04-30,Market crashes investors worried,-4,2
        

        Note: Strict adherence to removing commas from headlines is necessary to maintain the structural integrity of the CSV output format.
        """
         },
        {"role": "user", "content": query}
    ]
    )

    return completion.choices[0].message.content
