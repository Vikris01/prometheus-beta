import pytest
from src.string_validator import is_digits_only

def test_is_digits_only_valid():
    """Test that strings with only digits return True."""
    assert is_digits_only("12345") == True
    assert is_digits_only("0") == True
    assert is_digits_only("9876543210") == True

def test_is_digits_only_invalid():
    """Test that strings with non-digit characters return False."""
    assert is_digits_only("123a45") == False
    assert is_digits_only("12 345") == False
    assert is_digits_only("-123") == False
    assert is_digits_only("") == False
    assert is_digits_only(".123") == False

def test_is_digits_only_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_digits_only(12345)
    
    with pytest.raises(TypeError):
        is_digits_only(None)
    
    with pytest.raises(TypeError):
        is_digits_only(["123"])