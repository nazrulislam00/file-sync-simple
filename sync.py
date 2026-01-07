import os
import shutil

SOURCE_DIR = "source"
TARGET_DIR = "target"

os.makedirs(TARGET_DIR, exist_ok=True)

for filename in os.listdir(SOURCE_DIR):
    src = os.path.join(SOURCE_DIR, filename)
    dst = os.path.join(TARGET_DIR, filename)

    if os.path.isfile(src) and not os.path.exists(dst):
        shutil.copy(src, dst)
        print(f"Copied: {filename}")

print("Sync completed")
