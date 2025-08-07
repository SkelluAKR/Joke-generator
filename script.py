import google.generativeai as genai
import random
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)  
model = genai.GenerativeModel('models/gemini-1.5-flash')


topics = ["chickens", "bananas", "space cats", "pirates", "toasters"]
styles = ["punny", "silly", "cringeworthy", "absurd", "kid-friendly", "witty"]

def generate_joke():
  topic = random.choice(topics)
  style = random.choice(styles)
  prompt = f"Tell me a {style} joke about {topic}."

  response = model.generate_content(prompt)
  return response.text.strip()

for _ in range(3):
  print("🤣", generate_joke(), "\n")
