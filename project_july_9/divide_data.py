import os
import shutil
import random
from pathlib import Path

# Define paths
input_data_path = '/home/bhumika-avadutha/Downloads/four'
output_dir = '/home/bhumika-avadutha/Desktop'

# Create output directories if they don't exist
train_dir = os.path.join(output_dir, 'train')
test_dir = os.path.join(output_dir, 'test')
valid_dir = os.path.join(output_dir, 'valid')
for dir_path in [train_dir, test_dir, valid_dir]:
    Path(dir_path).mkdir(parents=True, exist_ok=True)

# List all files in the input directory
files = os.listdir(input_data_path)
random.shuffle(files)  # Shuffle files randomly

# Calculate split sizes
total_files = len(files)
train_split = int(0.8 * total_files)
test_split = int(0.1 * total_files)

# Assign files to respective splits
train_files = files[:train_split]
test_files = files[train_split:train_split + test_split]
valid_files = files[train_split + test_split:]

# Copy files to respective directories
for fname in train_files:
    shutil.copy(os.path.join(input_data_path, fname), os.path.join(train_dir, fname))
for fname in test_files:
    shutil.copy(os.path.join(input_data_path, fname), os.path.join(test_dir, fname))
for fname in valid_files:
    shutil.copy(os.path.join(input_data_path, fname), os.path.join(valid_dir, fname))

print("Data splitting completed successfully.")