import os

def get_files_info(working_directory, directory=None):
    # Default directory to working_directory if not provided
    if directory is None:
        directory = working_directory

    # Convert to absolute paths
    abs_working_directory = os.path.abspath(working_directory)
    if os.path.isabs(directory):
        abs_directory = os.path.abspath(directory)
    else:
        abs_directory = os.path.abspath(os.path.join(working_directory, directory))

    # Ensure the directory is within the working directory
    if os.path.commonpath([abs_working_directory, abs_directory]) != abs_working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Check if the directory is valid
    if not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'

    try:
        # Build the directory contents string
        contents = []
        for entry in os.scandir(abs_directory):
            entry_info = f"- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}"
            contents.append(entry_info)
        return "\n".join(contents)
    except Exception as e:
        return f"Error: {str(e)}"