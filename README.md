# ValueForge: Product Differentiation Engine

**ValueForge** is a production-grade, product-agnostic engine designed to calculate and evaluate consumer product differentiation against competitive market density prior to manufacturing. 

Built as an internal tool for brand strategy and product planning, this engine converts qualitative market positioning into quantitative whitespace metrics.

## Core Architecture & Data Science

Standard wrapper applications frequently suffer from non-deterministic outputs and calculation errors. ValueForge avoids this through a decoupled execution architecture:

* **Dual-Layer Semantic Parsing:** Combines live, user-provided competitor baselines with dynamic parametric memory via the Groq API to evaluate market saturation patterns.
* **Explainable Feature Attribution:** Every submitted product concept is broken down into feature vectors, penalizing overused tropes with negative values and scoring unique positioning features against a baseline value of 50.
* **Deterministic Math Engine:** Model temperature is locked (`temperature=0.0`). A regex pipeline extracts numerical feature impact values and computes final arithmetic using native Python routines to eliminate calculation errors.

## Key Features

* **Universal Scope Parsing:** Supports category switching (from sports nutrition to software services) without structural modifications to the underlying logic.
* **Dynamic Model Handling:** Automatically queries and ingests active Groq models at runtime to prevent API deprecation failures.
* **Interactive Interface:** Built with Streamlit for real-time comparative analysis and dashboarding.
* **Homogeneity Threshold Warnings:** Flags concepts that fall below predefined positioning thresholds to mitigate brand overlap risks.

## Tech Stack

* **Frontend Interface:** Streamlit
* **Model Orchestration:** Groq API (Llama 3.3 / Llama 3.1)
* **Logic & Parsing:** Python (`re`, `pandas`)

## Installation & Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/Torpid-Quark/ValueForge.git](https://github.com/Torpid-Quark/ValueForge.git)
cd ValueForge
```

### 2. Install Dependencies
Make sure Python is installed, then run:

```bash
pip install streamlit pandas groq
```

### 3. Set Up Environment Variables
Set your Groq API key in your terminal session before launching the application:

Windows (PowerShell):
```powershell
$env:GROQ_API_KEY="your_actual_api_key_here"
```

Mac/Linux:
```bash
export GROQ_API_KEY="your_actual_api_key_here"
```

### 4. Run the Engine

```bash
python -m streamlit run app.py
```

### 5. Usage Workflow

1. **Define the Market:** Open the sidebar and set your Target Industry (e.g., "Skincare / Anti-Aging").
2. **Select Model:** Choose an active Groq model from the dropdown.
3. **Anchor Context:** Input competitor product claims to set the local evaluation baseline.
4. **Evaluate Concept:** Input your product concept in the main interface and run the evaluation matrix to calculate the differentiation score.
