import os

def get_file_content(working_directory, file_path):
    
    # Convert to absolute paths
    abs_working_directory = os.path.abspath(working_directory)
    if os.path.isabs(file_path):
        abs_file_path = os.path.abspath(file_path)
    else:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Ensure the file is within the working directory
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # Check if the file exists
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_file_path, 'r') as file:
            content = file.read()
        if len(content) > 10000:
            content = content[:10000] + f'[...File "{file_path}" truncated at 10000 characters]'
        return content
    except Exception as e:
        return f"Error: {str(e)}"