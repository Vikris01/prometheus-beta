import pytest
from src.palindrome import is_palindrome

def test_is_palindrome():
    # Basic palindromes
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    
    # Case-insensitive palindromes
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaceCar") == True
    
    # Palindromes with punctuation
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    
    # Non-palindromes
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    
    # Empty string and single character
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    
    # Numeric palindromes
    assert is_palindrome("12321") == True
    assert is_palindrome("1 22 1") == True
    
    # Mixed alphanumeric palindromes
    assert is_palindrome("a1b2c3c2b1a") == True
    assert is_palindrome("a1b2c3d4") == False

def test_is_palindrome_edge_cases():
    # Whitespace-only string
    assert is_palindrome("  ") == True
    
    # Special characters only
    assert is_palindrome("!@#$%^&*()") == True
    
    # Mixed case with special characters
    assert is_palindrome("A man, a Plan, a Canal: Panama!") == True