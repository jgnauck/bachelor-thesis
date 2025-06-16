# Thesis Project 
This repository contains code and data for my Bachelor Thesis:
**"Caption Quality Comparison with the DaTikZ Dataset"**

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

```md
## Scripts

| Script              | Description                                        |
|---------------------|----------------------------------------------------|
| `load_blip.py`      | Generates image captions using BLIP-2              |
| `load_llava.py`     | Generates image captions using LLaVA 1.5           |
| `load_qwen.py`      | Generates image captions using Qwen2.5-VL          |
| `load_gpt4omini.py` | Generates image captions using GPT-4o-mini         |
| `large_scale.py`    | Processes a large image set using Qwen             |
| `tikz.py`           | Converts captions into LaTeX TikZ using GPT-4o     |
```

## Installation Instructions
Install required packages via 'pip':
```bash
pip install torch transformers openai pandas tqdm pillow
```