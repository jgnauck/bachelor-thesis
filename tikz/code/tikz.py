import os
import pandas as pd
from openai import OpenAI
from tqdm import tqdm

# Configuration
#Qwen
CSV_INPUT = "qwenn_captions_200.csv"
CSV_OUTPUT = "qwenn_tikz.csv"

#BLIP
#CSV_INPUT = "blip_captions_200.csv"
#CSV_OUTPUT = "blip_tikz.csv"

#gpt4o-mini
#CSV_INPUT = "gpt_captions_200.csv"
#CSV_OUTPUT = "gpt_tikz.csv"

#LLaVA
#CSV_INPUT = "llava_captions_200.csv"
#CSV_OUTPUT = "llava_tikz.csv"

API_KEY = "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"
MODEL = "gpt-4o-mini" 
MAX_SAMPLES = 51

# Initialize client
client = OpenAI(api_key=API_KEY)

# Load CSV
df = pd.read_csv(CSV_INPUT, header=None, names=["Sample", "Caption"])
df = df.head(MAX_SAMPLES)

tikz_documents = []

# Prompt
system_prompt = (
    "You are a LaTeX TikZ expert. For each prompt, return ONLY the TikZ code block. "
    "Do not include explanations, LaTeX preambles, or any text outside \\begin{tikzpicture} ... \\end{tikzpicture}."
)

# Wrap tikz code with latex code
def wrap_tikz_code(tikz_code: str) -> str:
    return f"""\\documentclass[tikz,border=10pt]{{standalone}}
    \\usepackage{{tikz}}
    \\usetikzlibrary{{arrows.meta, positioning, shapes.geometric}}
    
    \\begin{{document}}
    {tikz_code}
    \\end{{document}}"""

# Process each caption
for caption in tqdm(df["Caption"], desc="Generating TikZ"):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": caption}
            ],
            temperature=0.5,
            max_tokens=1000,
            stop=["\\end{tikzpicture}"] 
        )
        content = response.choices[0].message.content.strip()

        
        if not content.strip().endswith(r"\end{tikzpicture}"):
            content += "\n\\end{tikzpicture}"

    except Exception as e:
        content = f"Error: {str(e)}"

    full_latex = wrap_tikz_code(content)
    tikz_documents.append(full_latex)

# Add TikZ code to DataFrame
df["LaTeX_Document"] = tikz_documents

# Save to output CSV
df.to_csv(CSV_OUTPUT, index=False)