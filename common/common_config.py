import os


def delete_all_files(file_path):
    if os.path.exists(file_path):
        for filename in os.listdir(file_path):
            temp_filepath = os.path.join(file_path, filename)
            os.remove(temp_filepath)
