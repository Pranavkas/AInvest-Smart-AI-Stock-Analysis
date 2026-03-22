# import os

# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(api_key=os.getenv("AIzaSyBgfF0tLKqzybJEO0Vn3HmmoF2XOhYAmfI"))

# def get_llm():
#     return genai.GenerativeModel("gemini-1.5-flash")
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("AIzaSyBgfF0tLKqzybJEO0Vn3HmmoF2XOhYAmfI"))

def get_llm():
    return client