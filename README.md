# ValueForge: AI Product Differentiation Engine

**ValueForge** is a production grade, product agnostic enterprise tool designed to mathematically calculate and evaluate consumer product differentiation against competitive market density before manufacturing. 

Built as an internal prototype for brand strategy and product management, this engine transforms qualitative market saturation into quantitative, actionable whitespace metrics.

## Core Architecture & Data Science

Traditional LLM wrappers suffer from non-determinism and mathematical hallucination. ValueForge solves this through a decoupled, deterministic architecture:

* **Dual-Layer Semantic Parsing:** Merges **Contextual Ingestion** (live, user-uploaded competitor baselines) with **Parametric Memory** (Llama 3.1's pre-trained knowledge of global market tropes) to identify genuine market whitespace.
* **Explainable AI (SHAP-Inspired Attribution):** Moves beyond black-box scoring. Every concept is broken down into isolated feature vectors, penalizing saturated clichés (negative integers) and rewarding unique positioning (positive integers) against a strict baseline score of 50.
* **Deterministic Math Guardrails:** LLM variance is clamped (`temperature=0.0`). A resilient native Python Regular Expression (Regex) pipeline extracts isolated feature impact scores and programmatically computes the final arithmetic, entirely eliminating AI arithmetic hallucinations.

## Key Features

* **Universal Scope Parsing:** Dynamically switches focus across distinct industries (from Sports Nutrition to SaaS to Reproductive Wellness) without requiring backend code changes.
* **Interactive UI:** Built on Streamlit for real-time brand manager dashboarding.
* **Homogeneity Warning System:** Automatically flags concepts that fall below acceptable differentiation thresholds to prevent brand dilution.

## Tech Stack

* **Frontend UI:** Streamlit (Dynamic layout compilation)
* **LLM Orchestration:** Llama 3.1 (8B Instant) via Groq API
* **Statistical Logic & Regex:** Native Python (`re`, `pandas`)

## 📦 Installation & Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/Torpid-Quark/ValueForge.git](https://github.com/Torpid-Quark/ValueForge.git)
cd ValueForge
