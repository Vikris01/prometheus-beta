import logging
import os
from typing import Optional, Union

class KeystrokeLogger:
    """
    A secure keystroke logging utility with configurable logging options.
    
    Provides methods to log keystrokes while maintaining user privacy and 
    allowing flexible logging configurations.
    """
    
    def __init__(self, 
                 log_file: Optional[str] = None, 
                 log_level: int = logging.INFO,
                 mask_sensitive: bool = True):
        """
        Initialize the KeystrokeLogger.
        
        Args:
            log_file (Optional[str]): Path to the log file. 
                                      If None, logs to a default location.
            log_level (int): Logging level (default: logging.INFO)
            mask_sensitive (bool): Mask potentially sensitive input (default: True)
        """
        # Ensure log directory exists
        if log_file:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(log_file) or os.getcwd(), exist_ok=True)
        else:
            # Default log file in user's home directory
            default_log_dir = os.path.join(os.path.expanduser('~'), '.logs')
            os.makedirs(default_log_dir, exist_ok=True)
            log_file = os.path.join(default_log_dir, 'keystroke.log')
        
        # Ensure the log file exists
        open(log_file, 'a').close()
        
        # Configure logging
        logging.basicConfig(
            filename=log_file, 
            level=log_level, 
            format='%(asctime)s - %(message)s'
        )
        
        self.mask_sensitive = mask_sensitive
        self.log_file = log_file
    
    def log_keystroke(self, key: Union[str, int]) -> None:
        """
        Log a single keystroke.
        
        Args:
            key (Union[str, int]): The key or key code to log
        
        Raises:
            ValueError: If the key is None or empty
        """
        if key is None:
            raise ValueError("Cannot log None key")
        
        # Convert key to string
        key_str = str(key)
        
        # Mask sensitive keys if configured
        if self.mask_sensitive:
            if len(key_str) == 1 and key_str.isprintable():
                # Log printable characters
                logging.info(f"KEY: {key_str}")
            else:
                # Log special keys with brackets
                logging.info(f"KEY: [{key_str}]")
        else:
            # Log all keys without masking
            logging.info(f"KEY: {key_str}")
    
    def log_input(self, input_string: str) -> None:
        """
        Log an entire input string, with optional masking.
        
        Args:
            input_string (str): The input string to log
        
        Raises:
            ValueError: If input is None or empty
        """
        if not input_string:
            raise ValueError("Cannot log empty input")
        
        if self.mask_sensitive:
            # Mask potentially sensitive inputs
            masked_input = '*' * len(input_string)
            logging.info(f"INPUT: {masked_input}")
        else:
            logging.info(f"INPUT: {input_string}")