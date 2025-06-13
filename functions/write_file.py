

def write_file(working_directory, file_path, content):
    import os

    # Convert to absolute paths
    abs_working_directory = os.path.abspath(working_directory)
    if os.path.isabs(file_path):
        abs_file_path = os.path.abspath(file_path)
    else:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Ensure the file is within the working directory
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # Create directories if they do not exist
    dir_name = os.path.dirname(abs_file_path)
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except Exception as e:
            return f"Error: Could not create directory '{dir_name}': {str(e)}"

    # Write the content to the file
    try:
        with open(abs_file_path, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"