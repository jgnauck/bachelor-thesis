from datasets import load_dataset
import random
import pandas as pd

# Generate a filtered 200-sample subset from the DaTikZ-v3 dataset
# approx, 72.5% arxiv, 27,5% non-arxiv
# save as CSV and pickle

ds = load_dataset("nllg/datikz-v3", split="train")

# Print available columns
print("Available columns:", ds.column_names)

#Filter valid entries with non-empty captions
ds_list = ds.to_list()
print(f"Total dataset size: {len(ds_list)}")
filtered_data = [item for item in ds_list if 'caption' in item and isinstance(item['caption'], str) and item['caption'].strip() != ""]


print(f"Total dataset size after filtering: {len(filtered_data)}")


# Separate entries by origin
arxiv_entries = [item for item in filtered_data if item.get("origin") == "arxiv"]
other_entries = [item for item in filtered_data if item.get("origin") != "arxiv"]

# Define sample sizes
sample_size = 200
arxiv_sample_size = min(int(sample_size * 0.725), len(arxiv_entries))
other_sample_size = sample_size - arxiv_sample_size

# Random sampling
random.seed(42)
arxiv_sample = random.sample(arxiv_entries, arxiv_sample_size)
other_sample = random.sample(other_entries, other_sample_size)

# Combine and shuffle
final_sample = arxiv_sample + other_sample
random.shuffle(final_sample)

# Save
df_sample = pd.DataFrame(final_sample)
df_sample.to_pickle("DaTikZ_Sample_filtered.pkl")
df_sample.to_csv("DaTikZ_Sample_filtered.csv", index=False)


# Show distribution
print("\nSample origin distribution:")
print(df_sample["origin"].value_counts())
