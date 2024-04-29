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
        Process a list of 50 headlines with associated dates to determine the sentiment and excitement levels for each headline.

        Input Format: A CSV file or a structured list where each row contains:

        Date: The publication date of the headline.
        Headline: The text of the headline.
        Processing Steps:

        Read Input Data: The model reads the data from the CSV file or the structured list, ensuring each headline is associated with its publication date.
        Sentiment Analysis: For each headline, calculate the sentiment score ranging from -5 (very negative) to +5 (very positive).
        Excitement Analysis: For each headline, calculate the excitement score ranging from 0 (least exciting) to 10 (most exciting).
        Output Format: A structured list where each row contains: 

        Date: The date of the headline.
        Headline: The headline text.
        Sentiment Score: The calculated sentiment score for the headline.
        Excitement Score: The calculated excitement score for the headline.
        Example Input:

        Time,Headline
        18-Jul-20	Johnson is asking Santa for a Christmas recovery
        18-Jul-20	‘I now fear the worst’: four grim tales of working life upended by Covid-19
        Example Output:


        Time,Headline,Sentiment Score,Excitement Score
        8-Jul-20	Johnson is asking Santa for a Christmas recovery, 4, 8
        18-Jul-20	‘I now fear the worst’: four grim tales of working life upended by Covid-19, -3, 7
        REMEMBER ONLY TO OUTPUT THE HEADINES, NO ADDITIONNAL TEXT. ALSO NEVER WRITE COMMAS , NEVER WRITE COMMAS
        """
         },
        {"role": "user", "content": query}
    ]
    )

    return completion.choices[0].message.content
