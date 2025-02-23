import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a given file.

    Args:
        file_path (str): The path to the file whose permissions are to be modified.
        mode (int): The new file mode/permissions (e.g., 0o755 for rwxr-xr-x).

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permission to modify the file.
        TypeError: If the inputs are of incorrect type.
        ValueError: If the mode is not a valid permission value.
    """
    # Type checking
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("mode must be an integer")
    
    # Validate file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Validate mode is a valid octal permission
    if mode < 0 or mode > 0o777:
        raise ValueError("Invalid file mode. Must be between 0 and 0o777")
    
    try:
        # Change file permissions
        os.chmod(file_path, mode)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to modify {file_path}")
    except Exception as e:
        raise OSError(f"Error changing file permissions: {str(e)}")
    
    return True  # Indicate successful permission change