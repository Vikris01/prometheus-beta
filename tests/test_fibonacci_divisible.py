import pytest
from src.fibonacci_divisible import generate_modified_fibonacci

def test_generate_modified_fibonacci_basic():
    # Basic test to check sequence generation
    result = generate_modified_fibonacci(5)
    assert len(result) == 5
    assert result[0] == 1
    assert result[1] == 1

def test_divisibility_by_three():
    # Check that from 3rd number, sum of previous two is divisible by 3
    result = generate_modified_fibonacci(10)
    for i in range(2, len(result)):
        assert (result[i-2] + result[i-1]) % 3 == 0, f"Failed at index {i}"

def test_single_element():
    # Test with single element
    result = generate_modified_fibonacci(1)
    assert result == [1]

def test_two_elements():
    # Test with two elements
    result = generate_modified_fibonacci(2)
    assert result == [1, 1]

def test_invalid_input():
    # Test invalid input
    with pytest.raises(ValueError):
        generate_modified_fibonacci(0)
    
    with pytest.raises(ValueError):
        generate_modified_fibonacci(-1)

def test_sequence_properties():
    # Additional tests to verify sequence properties
    result = generate_modified_fibonacci(7)
    assert len(result) == 7
    
    # Check first two elements
    assert result[:2] == [1, 1]
    
    # Additional divisibility checks
    for i in range(2, len(result)):
        assert (result[i-2] + result[i-1]) % 3 == 0, f"Divisibility failed at index {i}"