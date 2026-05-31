import pandas as pd
import os
from groq import Groq

# 1. Initialize the AI Engine (You will need a free Groq API Key)
# Make sure to set your key in your terminal: export GROQ_API_KEY="your_key"
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 2. The Competitive Landscape (Simulating our Option A Dataset)
print("Ingesting Competitive Market Data...")
market_data = [
    {"brand": "Opti-Fit", "description": "High protein whey isolate for muscle recovery. 20g protein, low carb, keto-friendly. Boosts energy."},
    {"brand": "MaxPower", "description": "Clean energy protein bar. 22g of high protein. Zero sugar, low carb, great for post-workout recovery."},
    {"brand": "PureGains", "description": "Guilt-free protein powder. Keto-friendly, low sugar, high protein formula for rapid muscle recovery."},
    {"brand": "KetoCrunch", "description": "The ultimate keto-friendly protein snack. Low carb, zero sugar, high protein for sustained energy."},
    {"brand": "IronBite", "description": "Post-workout muscle recovery bar. 25g protein, low sugar, clean energy, guilt-free snacking."}
    # In a production app, this would be pd.read_csv('sports_nutrition.csv') with 800+ rows
]
df = pd.DataFrame(market_data)
market_text_corpus = " ".join(df['description'].tolist())

# 3. Define the New Product Concept (What the Brand Manager wants to launch)
new_product_idea = """
A plant-based protein bar formulated with Ashwagandha and Lion's Mane mushroom. 
Designed for post-workout physical recovery and sustained mental clarity without cortisol spikes.
"""

# 4. The ValueForge Prompt (The Mathematical Whitespace Logic)
prompt = f"""
You are the ValueForge AI Logic Engine. Analyze the 'Market Data' below to identify saturated marketing claims. 
Then, evaluate the 'New Product Concept' and calculate a 'Differentiation Score' (0-100) relative to a base market score of 50.

    Market Data (Top 50 Competitors):e

New Product Concept:
{new_product_idea}

Provide your analysis in the following strict format:
1. Saturated Claims: (List the top 3 overused phrases)
2. Whitespace Identified: (Unique positioning angles)
3. Differentiation Score: (Score out of 100)
4. SHAP Feature Attribution (Mathematical Breakdown):
   - Base Market Score: 50
   - [Feature 1]: (+/- X points) because...
   - [Feature 2]: (+/- X points) because...
   - Final Score: [Matches Differentiation Score]
   (Note: SHAP values must mathematically sum up from the Base Score of 50 to the Final Score).
"""

print("\nRunning ValueForge Algorithm via Llama 3...")
# 5. Call the LLM
response = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}],
    model="llama-3.1-8b-instant", 
)

print("\n--- VALUEFORGE STRATEGY REPORT ---")
print(response.choices[0].message.content)