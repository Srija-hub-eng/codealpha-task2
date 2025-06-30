import os
import shutil

source_folder = 'C:/Users/srija/Downloads'
destination_folder = 'C:/Users/srija/Pictures/JPGs'

os.makedirs(destination_folder, exist_ok=True)

print("Checking for .jpg files in", source_folder)

for file_name in os.listdir(source_folder):
    if file_name.lower().endswith('.jpg'):
        print(f"Found JPG file: {file_name}")
        source_path = os.path.join(source_folder, file_name)
        dest_path = os.path.join(destination_folder, file_name)

        # Handle filename conflict
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(file_name)
            counter = 1
            while os.path.exists(dest_path):
                new_name = f"{base}_{counter}{ext}"
                dest_path = os.path.join(destination_folder, new_name)
                counter += 1

        shutil.move(source_path, dest_path)
        print(f"Moved: {file_name} → {os.path.basename(dest_path)}")
