import os

def rename_images_in_folder(folder_path):
    # Get all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out non-image files (optional, adjust according to your needs)
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    image_files = [f for f in files if any(f.lower().endswith(ext) for ext in image_extensions)]
    
    # Sort files if you want them renamed in a specific order
    image_files.sort()

    # Rename each image file
    for index, filename in enumerate(image_files, 1):
        # Construct the old file path and the new file name
        old_file_path = os.path.join(folder_path, filename)
        new_file_name = f"{index}{os.path.splitext(filename)[1]}"  # Keeps the original extension
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_file_name}")

# Specify the folder where the images are located
folder_path = "./train"

# Call the function
rename_images_in_folder(folder_path)