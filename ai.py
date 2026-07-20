import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the .env file
load_dotenv()

# Read the API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Create the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_design(room_type, style, budget, color):

    prompt = f"""
You are an expert interior designer.

Design a beautiful {room_type}.

Requirements:
- Style: {style}
- Budget: ₹{budget}
- Preferred Color: {color}

Provide:
1. Theme Overview
2. Wall Paint Suggestions
3. Furniture Recommendations
4. Lighting Ideas
5. Flooring Suggestions
6. Curtains
7. Decorative Items
8. Space Saving Tips
9. Estimated Budget Allocation
10. Final Professional Recommendation

Give the response in markdown.
"""

    response = model.generate_content(prompt)

    return response.text