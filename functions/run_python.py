import os
import subprocess

from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python file that the file_path points to, constrained to the working directory. The function includes checks to ensure the file is within the working directory and is an actual python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to run the python script, relative to the working directory. ",
            ),
        },
    ),
)


def run_python_file(working_directory, file_path):

    # Convert to absolute paths
    abs_working_directory = os.path.abspath(working_directory)
    if os.path.isabs(file_path):
        abs_file_path = os.path.abspath(file_path)
    else:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Ensure the file is within the working directory
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # Check if the file exists and is a regular file
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        # Run the Python file with a timeout of 30 seconds
        result = subprocess.run(
            ['python', abs_file_path],
            capture_output=True,
            text=True,
            cwd=abs_working_directory,
            timeout=30
        )
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        output = []

        if stdout:
            output.append(f"STDOUT: {stdout}")
        if stderr:
            output.append(f"STDERR: {stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not output:
            return "No output produced."

        return "\n".join(output)
    except subprocess.TimeoutExpired:
        return "Error: Execution timed out after 30 seconds."
    except Exception as e:
        return f"Error: executing Python file: {e}"