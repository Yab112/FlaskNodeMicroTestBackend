import re
import os
from dotenv import load_dotenv
from groq import Groq
import json
from utils.db_utils import store_data
from datetime import datetime

load_dotenv()

def data_extraction(text):
    prompt = f"""
    Extract key information from this PDF text about the client and insurance details.
    Format the extracted information as a JSON object. Include fields like name, 
    email, phone, address, education, experience, skills, etc.

    Text: {text}
    """
    
    # Initialize the Groq client with your API key
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))  

    # Model and parameters setup
    model = "llama-3.3-70b-versatile"
    temperature = 1
    max_tokens = 1024
    top_p = 1
    stop = None
    messages = [{"role": "user", "content": prompt}]
    
    # Make the request for completion
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_completion_tokens=max_tokens,
        top_p=top_p,
        stream=True,
        stop=stop
    )

    # Process the response from Groq's streaming API
    extracted_text = ""
    for chunk in completion:
        extracted_text += chunk.choices[0].delta.content or ""
    # print(extracted_text,"response from llama mode; ****************8888")
    return extracted_text

def json_from_text(text):
    """
    Converts extracted text into JSON by cleaning the unnecessary part before JSON data.
    """
    # Use a regex to find the JSON portion in the response text
    json_match = re.search(r'```json\n(.*?)\n```', text, re.DOTALL)
    if json_match:
        # Extract the JSON part and return the parsed data
        json_data = json_match.group(1)
        try:
            return json.loads(json_data)
        except json.JSONDecodeError:
            return None
    return None

def preprocess_and_store_data(text):
    """
    Preprocesses the extracted text, organizes it, and stores it in the database.
    """
    # Extract data using LLM model (assuming `data_extraction` is a function that provides the model's response)
    extracted_text = data_extraction(text)
    

    # Convert extracted text to JSON after cleaning
    json_data = json_from_text(extracted_text)

    
    if json_data:
        store_data('processed_data', json_data)  # Store in MongoDB
        return True
    return False
