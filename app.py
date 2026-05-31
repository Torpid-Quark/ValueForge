import streamlit as st
import pandas as pd
import os
import re
from groq import Groq

# Set up page styling using standard 'st' alias
st.set_page_config(page_title="ValueForge // Ai Palette", page_icon="⚡", layout="wide")

st.title("⚡ ValueForge: AI Product Differentiation Engine")
st.caption("Ai Palette Taskforce Internal Prototype — Powered by Llama 3.1 & Groq")
st.divider()

# 1. Initialize API Client safely
api_key = os.environ.get("GROQ_API_KEY", "")
if not api_key:
    st.error("Groq API Key not found. Please set the environment variable or enter it below.")
    api_key = st.text_input("Enter Groq API Key:", type="password")

# 2. Sidebar: Dynamic Industry & Competitive Landscape Ingestion
with st.sidebar:
    st.header("📦 Competitive Landscape Ingestion")
    
    # Let the user define the target category dynamically
    target_category = st.text_input("Target Industry / Category:", value="Sports Nutrition / Fitness Bars")
    
    st.subheader("Competitor Context Dataset")
    # Default initial dataset (Fitness Bars) that the user can freely overwrite in the UI
    default_market_corpus = (
        "Opti-Fit: High protein whey isolate for muscle recovery. 20g protein, low carb, keto-friendly. Boosts energy.\n"
        "MaxPower: Clean energy protein bar. 22g of high protein. Zero sugar, low carb, great for post-workout recovery.\n"
        "PureGains: Guilt-free protein powder. Keto-friendly, low sugar, high protein formula for rapid muscle recovery.\n"
        "KetoCrunch: The ultimate keto-friendly protein snack. Low carb, zero sugar, high protein for sustained energy.\n"
        "IronBite: Post-workout muscle recovery bar. 25g protein, low sugar, clean energy, guilt-free snacking."
    )
    
    market_text_corpus = st.text_area(
        "Paste Competitor Data (Brand: Description per line):", 
        value=default_market_corpus, 
        height=250
    )
    st.info(f"Context anchor set to analyze the '{target_category}' sector.")

# 3. Main Interface: User Input Space
st.subheader("💡 Launch Evaluation Engine")
default_concept = "A plant-based protein bar formulated with Ashwagandha and Lion's Mane mushroom. Designed for post-workout physical recovery and sustained mental clarity without cortisol spikes."
user_concept = st.text_area("Enter your proposed product concept & marketing direction:", value=default_concept, height=120)

if st.button("Run ValueForge Evaluation Matrix", type="primary"):
    if not api_key:
        st.warning("Please provide a valid Groq API key first.")
    elif not market_text_corpus.strip():
        st.warning("Please provide competitor market data in the sidebar to anchor the analysis.")
    else:
        with st.spinner(f"Executing structural text parsing for the {target_category} market..."):
            try:
                client = Groq(api_key=api_key)
                
                # Updated prompt utilizing the dynamic target_category variable
                prompt = f"""
                You are the ValueForge AI Logic Engine specialized in the '{target_category}' sector. 
                Analyze the 'Market Data' below to identify saturated marketing claims or industry clichés within this specific sector. 
                Then, evaluate the 'New Product Concept' and determine its impact on a base market score of 50 based on how well it finds whitespace or succumbs to existing tropes.

                Market Data for {target_category}:
                {market_text_corpus}

                New Product Concept:
                {user_concept}

                Provide your analysis in the following strict format:
                1. Saturated Claims: (List the top 3 overused phrases in this specific category)
                2. Whitespace Identified: (Unique positioning angles relevant to this category)
                3. SHAP Feature Attribution (Mathematical Breakdown):
                   - Base Market Score: 50
                   - [Feature 1]: SCORE: [integer] because...
                   - [Feature 2]: SCORE: [integer] because...
                   - [Feature 3]: SCORE: [integer] because...

                CRITICAL INSTRUCTION FOR SHAP VALUES: 
                The integer values next to SCORE can be positive (e.g., SCORE: 15), negative (e.g., SCORE: -20), or zero (e.g., SCORE: 0). 
                Do not perform or display any final mathematical additions or totals yourself. Just output the three individual feature scores.
                """
                
                response = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.1-8b-instant",
                    temperature=0.0, # Zero variance. Forces deterministic evaluation.
                )
                
                report = response.choices[0].message.content
                
                # Resilient Python Math Parsing (Catches variations like [SCORE: -25] or SCORE: -25)
                base_score = 50
                raw_matches = re.findall(r'(?:score|SCORE)[:\s\[]*([-\d]+)', report)
                
                feature_scores = []
                for match in raw_matches:
                    try:
                        feature_scores.append(int(match))
                    except ValueError:
                        continue
                
                # Fallback safety in case parsing misses a score
                while len(feature_scores) < 3:
                    feature_scores.append(0)
                
                # Compute final score programmatically in Python using the first 3 extracted values
                final_calculated_score = base_score + sum(feature_scores[:3])
                final_calculated_score = max(0, min(100, final_calculated_score)) # Clamp bounds
                
                st.success("Analysis Complete!")
                
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.metric(label="Differentiation Score", value=f"{final_calculated_score} / 100")
                with col2:
                    if final_calculated_score >= 75:
                        st.markdown("🟢 **High Whitespace Resonance:** Excellent differentiation potential. Low risk of immediate brand dilution.")
                    elif final_calculated_score >= 40:
                        st.warning("🟡 **Moderate Market Overlap:** Some unique vectors found, but positioning remains highly vulnerable.")
                    else:
                        st.error("🔴 **High Homogeneity Risk:** Critical structural overlap with existing market players. Total repositioning required.")
                
                st.divider()
                st.subheader("📋 Comprehensive Strategic Evaluation")
                st.markdown(report)
                
                # Append clean math explicitly to the bottom
                st.markdown("---")
                st.markdown(f"**Engine Math Verification:** Base ({base_score}) + Features ({', '.join([str(x) for x in feature_scores[:3]])}) = **{final_calculated_score}**")
                
            except Exception as e:
                st.error(f"Execution Error: {str(e)}")