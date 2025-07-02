import os

from google.genai import types


schema_write_file_content = types.FunctionDeclaration(
    name="write_file_content",
    description="Writes content to a file, constrained to the working directory. Includes checks to ensure the file path is within the working directory and creates directories if they do not exist. If the file already exists, it will be overwritten.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write the content to, relative to the working directory. ",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file. If the file does not exist, it will be created.",
            ),
        },
        required=["file_path", "content"],
    ),
)

def write_file(working_directory, file_path, content):
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