import os


def remove_files_without_extension(directory, target_extension=".jpg"):
    """
    Remove files in the specified directory that do not have the target extension.

    Parameters:
    - directory (str): The path to the directory containing the files.
    - target_extension (str): The target file extension to keep. Default is ".jpg".
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check if the file is a regular file and does not have the target extension
        if os.path.isfile(file_path) and not filename.endswith(target_extension):
            try:
                os.remove(file_path)
                print(f"Removed: {filename}")
            except Exception as e:
                print(f"Error removing {filename}: {str(e)}")


remove_files_without_extension(
    'C:/Users/Aravind/PROJECTS/Waste-Classification/Data/archive (2)/TRAIN/E', target_extension=".jpg")
remove_files_without_extension(
    'C:/Users/Aravind/PROJECTS/Waste-Classification/Data/archive (2)/TRAIN/O', target_extension=".jpg")
remove_files_without_extension(
    'C:/Users/Aravind/PROJECTS/Waste-Classification/Data/archive (2)/TRAIN/R', target_extension=".jpg")
remove_files_without_extension(
    'C:/Users/Aravind/PROJECTS/Waste-Classification/Data/archive (2)/TEST/E', target_extension=".jpg")
remove_files_without_extension(
    'C:/Users/Aravind/PROJECTS/Waste-Classification/Data/archive (2)/TEST/O', target_extension=".jpg")
remove_files_without_extension(
    'C:/Users/Aravind/PROJECTS/Waste-Classification/Data/archive (2)/TEST/R', target_extension=".jpg")
