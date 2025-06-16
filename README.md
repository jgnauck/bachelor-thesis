# Thesis Project 
This repository contains code and data for my Bachelor Thesis:
**"Caption Quality Comparison with the DaTikZ Dataset"**.

## Project Structure
```
Caption Analysis/
├── model captions/
│ ├── code/
│ │ ├── load_blip.py
│ │ ├── load_llava.py
│ │ ├── load_qwen.py
│ │ └── load_gpt4omini.py
│ ├── blip2_captions_200.csv
│ ├── gpt_captions_200.csv
│ ├── llava16_captions_200.csv
│ └── qwen_captions_200.csv

├── large scale/
│ ├── code/
│ │ └── large_scale.py
│ ├── images/
│ └── qwen_4001_6000.csv

├── sample dataset/
│ ├── code/
│ │ └── sample_dataset.py
│ ├── images/
│ └── description.csv

├── tikz/
│ ├── code/
│ │ └── tikz.py
│ ├── qwen_tikz.csv
│ ├── blip_tikz.csv
│ ├── gpt_tikz.csv
│ └── llava_tikz.csv

├── Bachelor Thesis.pdf
└── README.md
```


## Scripts
```
| Script              | Description                                        |
|---------------------|----------------------------------------------------|
| `sample_dataset.py`    | Generates a filtered 200-sample subset from the DaTikZ-v3 dataset              |
| `load_blip.py`      | Generates image captions for the sample dataset using BLIP-2              |
| `load_llava.py`     | Generates image captions for the sample dataset using LLaVA 1.5           |
| `load_qwen.py`      | Generates image captions for the sample dataset using Qwen2.5-VL          |
| `load_gpt4omini.py` | Generates image captions for the sample dataset using GPT-4o-mini         |
| `large_scale.py`    | Generates 2000 captions using Qwen2.5-VL             |
| `tikz.py`           | Converts captions into LaTeX TikZ code using GPT-4o     |
```

## Installation Instructions
Install required packages via 'pip':
```bash
pip install torch transformers openai pandas tqdm pillow datasets
```

## OpenAI API Key Setup
Some scripts (load_gpt4omini.py, tikz.py) use the OpenAI API. To run these, set your API key as an environment variable:
On Windows:
```
set OPENAI_API_KEY=your-api-key
```

## Thesis
This project was developed as part of my Bachelor Thesis at University of Mannheim. Please refer to Bachelor Thesis.pdf for methodology and detailed analysis.