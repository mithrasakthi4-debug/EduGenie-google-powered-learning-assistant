import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY not found")
    exit()

client = genai.Client(api_key=api_key)

print("Testing Gemini...")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain photosynthesis in two simple sentences."
)

print("\nGemini Response:")
print(response.text)