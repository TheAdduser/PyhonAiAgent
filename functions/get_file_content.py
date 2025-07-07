import os

def get_file_content(working_directory, file_path):
    try:

        if not file_path.startswith(working_directory):
            raise ValueError(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        elif os.path.isdir(file_path):
            raise ValueError(f'Error: File not found or is not a regular file: "{file_path}"')
        
        MAX_CHARS = 10000

        with open(file_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f'Error: {str(e)}'