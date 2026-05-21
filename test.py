from dotenv import load_dotenv
import os

load_dotenv()

print("Gemini:", bool(os.getenv("GEMINI_KEY")))
print("HF:", bool(os.getenv("HF_TOKEN")))