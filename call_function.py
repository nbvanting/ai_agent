from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python import schema_run_python_file, run_python_file
from functions.write_file_content import schema_write_file, write_file

from config import WORKING_DIRECTORY


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)


def call_function(function_call_part, verbose=False):
    """
    Calls the specified function with the provided arguments.
    
    Args:
        function_call_part (types.FunctionCallPart): The function call part containing the function name and arguments.
        verbose (bool): If True, prints additional information about the function call.
    
    Returns:
        str: The result of the function call.
    """
    function_name = function_call_part.name
    if verbose:
        print(f"Calling function: {function_name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")
    
    # Call the function based on its name
    if function_name == "get_files_info":
        function_result = get_files_info(
            working_directory=WORKING_DIRECTORY,
            **function_call_part.args
        )
    elif function_name == "get_file_content":
        function_result = get_file_content(
            working_directory=WORKING_DIRECTORY,
            **function_call_part.args
        )
    elif function_name == "run_python_file":
        function_result = run_python_file(
            working_directory=WORKING_DIRECTORY,
            **function_call_part.args
        )
    elif function_name == "write_file":
        function_result = write_file(
            working_directory=WORKING_DIRECTORY,
            **function_call_part.args
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
    
