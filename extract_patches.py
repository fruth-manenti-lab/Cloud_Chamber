import cv2
import os

# --- CONFIG ---
input_folder = "images_resized/train"  # folder with resized images
patch_size = 160
stride = 80  # overlap between patches
output_folder = "dataset/train/all_patches"

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# --- MAIN LOOP ---
for filename in os.listdir(input_folder):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)
        if img is None:
            continue

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
        h, w = gray.shape

        patch_count = 0
        # Sliding window
        for y in range(0, h - patch_size + 1, stride):
            for x in range(0, w - patch_size + 1, stride):
                patch = gray[y:y+patch_size, x:x+patch_size]
                patch_name = f"{os.path.splitext(filename)[0]}_patch_{patch_count}.png"
                cv2.imwrite(os.path.join(output_folder, patch_name), patch)
                patch_count += 1

print("All patches extracted with sliding window!")
