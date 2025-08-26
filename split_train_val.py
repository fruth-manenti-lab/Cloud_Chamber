import os
import shutil
import random

# --- CONFIG ---
all_patches_folder = "dataset/all_patches"  # all patches should be here
train_folder = "dataset/train"
val_folder = "dataset/val"
val_ratio = 0.2  # 20% of patches for validation

# --- Ensure folders exist ---
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)

# --- Gather all patches ---
# Move all existing patches from train/ back to all_patches_folder (optional)
for folder in [train_folder, val_folder]:
    if os.path.exists(folder):
        for f in os.listdir(folder):
            if f.endswith((".png", ".jpg", ".jpeg")):
                shutil.move(os.path.join(folder, f), all_patches_folder)

# List all patch files
all_files = [f for f in os.listdir(all_patches_folder) if f.endswith((".png", ".jpg", ".jpeg"))]
if len(all_files) == 0:
    print("No patches found in all_patches folder!")
    exit()

# Shuffle files randomly
random.shuffle(all_files)

# Split into train and val
num_val = int(len(all_files) * val_ratio)
val_files = all_files[:num_val]
train_files = all_files[num_val:]

# Move files to respective folders
for f in train_files:
    shutil.move(os.path.join(all_patches_folder, f), os.path.join(train_folder, f))

for f in val_files:
    shutil.move(os.path.join(all_patches_folder, f), os.path.join(val_folder, f))

print(f"Total patches: {len(all_files)}")
print(f"Training patches: {len(train_files)}")
print(f"Validation patches: {len(val_files)}")
