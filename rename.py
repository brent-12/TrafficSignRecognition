import os

def rename_files_in_folder(folder_path):
    # List all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Sort files to ensure consistent ordering
    files.sort()
    
    # Rename each file
    for i, filename in enumerate(files, start=1):
        # Format the index with two digits (e.g., 01, 02, ..., 10, 11, ...)
        index_str = f"{i:02d}"
        
        # Create the new filename
        new_filename = f"000000_00000_000{index_str}"
        
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        
        # Full path for old and new filenames
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename + file_extension)
        
        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f"Renamed '{filename}' to '{new_filename + file_extension}'")

# Usage example:
folder_path = './test'
rename_files_in_folder(folder_path)