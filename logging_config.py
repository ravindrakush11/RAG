import sys
import logging

def setup_logging(log_file_path='streamlit_logs.log'):
    # Configure the logger
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Create a StreamHandler to write to stdout
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setLevel(logging.INFO)

    # Create a FileHandler to write to a log file with timestamps
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Get the root logger and add the handlers
    logger = logging.getLogger()
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

# Call the setup_logging function when this module is imported
setup_logging()
