import os
import logging
import pytest
import tempfile
from src.keystroke_logger import KeystrokeLogger

def test_keystroke_logger_initialization():
    """Test logger initialization with default parameters."""
    logger = KeystrokeLogger()
    assert logger is not None
    assert logger.mask_sensitive is True

def test_custom_log_file():
    """Test logger initialization with a custom log file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = os.path.join(tmpdir, 'custom.log')
        logger = KeystrokeLogger(log_file=log_file)
        assert os.path.exists(log_file)

def test_log_keystroke_single_character():
    """Test logging a single character keystroke."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = os.path.join(tmpdir, 'keystroke.log')
        logger = KeystrokeLogger(log_file=log_file)
        
        logger.log_keystroke('a')
        
        with open(log_file, 'r') as f:
            log_content = f.read()
            assert 'KEY: a' in log_content

def test_log_keystroke_non_printable():
    """Test logging a non-printable key."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = os.path.join(tmpdir, 'keystroke.log')
        logger = KeystrokeLogger(log_file=log_file)
        
        logger.log_keystroke('ENTER')
        
        with open(log_file, 'r') as f:
            log_content = f.read()
            assert 'KEY: [ENTER]' in log_content

def test_log_input_masked():
    """Test logging an input with masking."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = os.path.join(tmpdir, 'input.log')
        logger = KeystrokeLogger(log_file=log_file, mask_sensitive=True)
        
        logger.log_input('password123')
        
        with open(log_file, 'r') as f:
            log_content = f.read()
            assert 'INPUT: ***********' in log_content

def test_log_input_unmasked():
    """Test logging an input without masking."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = os.path.join(tmpdir, 'input.log')
        logger = KeystrokeLogger(log_file=log_file, mask_sensitive=False)
        
        logger.log_input('hello world')
        
        with open(log_file, 'r') as f:
            log_content = f.read()
            assert 'INPUT: hello world' in log_content

def test_log_keystroke_error_cases():
    """Test error handling for invalid keystroke inputs."""
    logger = KeystrokeLogger()
    
    with pytest.raises(ValueError):
        logger.log_keystroke(None)

def test_log_input_error_cases():
    """Test error handling for invalid input strings."""
    logger = KeystrokeLogger()
    
    with pytest.raises(ValueError):
        logger.log_input('')
    
    with pytest.raises(ValueError):
        logger.log_input(None)