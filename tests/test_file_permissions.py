import os
import pytest
import stat
from src.file_permissions import change_file_permissions

def test_change_file_permissions(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Initial check of default permissions
    initial_mode = test_file.stat().st_mode & 0o777
    assert initial_mode != 0o755  # Ensure it's not already 0o755
    
    # Change permissions
    result = change_file_permissions(str(test_file), 0o755)
    assert result is True
    
    # Verify new permissions
    new_mode = test_file.stat().st_mode & 0o777
    assert new_mode == 0o755

def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        change_file_permissions("nonexistent_file.txt", 0o644)

def test_invalid_file_path():
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o644)

def test_invalid_mode():
    test_file = os.path.join(os.path.dirname(__file__), "test_file_permissions.py")
    
    # Test negative mode
    with pytest.raises(ValueError):
        change_file_permissions(test_file, -1)
    
    # Test mode out of range
    with pytest.raises(ValueError):
        change_file_permissions(test_file, 0o1000)

def test_invalid_mode_type():
    test_file = os.path.join(os.path.dirname(__file__), "test_file_permissions.py")
    
    with pytest.raises(TypeError):
        change_file_permissions(test_file, "0o755")