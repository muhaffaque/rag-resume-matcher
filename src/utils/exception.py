import sys
from src.utils.logger import get_logger

logger = get_logger(__name__)

class CustomException(Exception):
    def __init__(self, error_message: str):
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown file"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown line"
        detailed_message = f"Error in {file_name} at line {line_number}: {error_message}"
        logger.error(detailed_message)
        super().__init__(detailed_message)
        self.error_message = detailed_message

    def __str__(self):
        return self.error_message


    