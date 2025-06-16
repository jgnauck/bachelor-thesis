# Bachelor Thesis
This repository contains code and data for the Bachelor Thesis:
**"Caption Quality Comparison with the DaTikZ Dataset"**.

## Project Structure
```
[bachelor-thesis]/
├── Caption Analysis/
│   └── Evaluation_Sheet.xlsx
├── generated images/
│   ├── BLIP/
│   ├── LLaVA/
│   ├── Original Caption/
│   ├── Qwen/
│   ├── Revised Descriptions/
│   └── gpt/
├── large scale/
│   ├── code/
│   │   └── large_scale.py
│   ├── images/
│   └── large_scale_captions.csv
├── model captions/
│   ├── code/
│   │   ├── load_blip.py
│   │   ├── load_gpt4omini.py
│   │   ├── load_llava.py
│   │   └── load_qwen.py
│   ├── blip2_captions_200.csv
│   ├── gpt_captions_200.csv
│   ├── llava_captions_200.csv
│   └── qwen_captions_200.csv
├── sample dataset/
│   ├── code/
│   │   └── sample_dataset.py
│   ├── images/
│   └── descriptions.csv
├── tikz/
│   ├── code/
│   │   └── tikz.py
│   ├── blip_tikz.csv
│   ├── description_tikz.csv
│   ├── gpt_tikz.csv
│   ├── llava_tikz.csv
│   ├── original_tikz.csv
│   └── qwen_tikz.csv
├── Bachelor Thesis.pdf
└── README.md
```

## Scripts
```
| Script              | Description                                        
|---------------------|----------------------------------------------------
| `sample_dataset.py` | Generates a filtered 200-sample subset from the DaTikZ-v3 dataset              
| `load_blip.py`      | Generates image captions for the sample dataset using BLIP-2              
| `load_llava.py`     | Generates image captions for the sample dataset using LLaVA 1.5           
| `load_qwen.py`      | Generates image captions for the sample dataset using Qwen2.5-VL          
| `load_gpt4omini.py` | Generates image captions for the sample dataset using GPT-4o-mini         
| `large_scale.py`    | Generates 2000 captions using Qwen2.5-VL             
| `tikz.py`           | Converts captions into LaTeX TikZ code using GPT-4o     
```

## CSV Files
```
| File                      | Description                                        
|---------------------------|----------------------------------------------------
| `Evaluation_Sheet.xlsx`    | Results from the manual classification framework             
| `large_scale_captions.csv`| Descriptions for 2000 images generated using Qwen2.5-VL           
| `blip2_captions_200.csv`  | Captions generated using BLIP-2 for the 200 sample images        
| `gpt_captions_200.csv`    | Captions generated using GPT-4o-mini for the 200 sample images          
| `llava_captions_200.csv`  | Captions generated using LLaVA 1.5 for the 200 sample images      
| `qwen_captions_200.csv`   | Captions generated using Qwen2.5-VL for the 200 sample images              
| `descriptions.csv`        | Original and revised descriptions for each image in the sample dataset 
| `blip_tikz.csv`           | TikZ code generated from BLIP-2 captions (50 images)            
| `gpt_tikz.csv`            | TikZ code generated from GPT-4o-mini captions (50 images)        
| `description_tikz.csv`    | TikZ code generated from our manually revised captions (50 images)          
| `llava_tikz.csv`          | TikZ code generated from LLaVA 1.5 captions (50 images)       
| `original_tikz.csv`       | TikZ code generated from original (unmodified) captions (50 images)              
| `qwen_tikz.csv`           | TikZ code generated from Qwen2.5-VL captions (50 images)    
```

## Installation Instructions
Install required packages via 'pip':
```bash
pip install torch transformers openai pandas tqdm pillow datasets
```

## OpenAI API Key Setup
Some scripts (load_gpt4omini.py, tikz.py) use the OpenAI API. To run these, set your API key as an environment variable:
```
set OPENAI_API_KEY=your-api-key
```

## Thesis
This project was developed as part of the Bachelor Thesis "Caption Quality Comparison with the DaTikZ Dataset" at University of Mannheim. Please refer to Bachelor Thesis.pdf for methodology and detailed analysis.