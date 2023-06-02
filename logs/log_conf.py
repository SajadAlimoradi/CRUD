import colorlog
import logging


# Configure logging with colorlog
class LogCrud:
    @staticmethod
    def log_establish(log_file: str = 'logs/log.log') -> logging.Logger:
        """
        Establishes and returns a configured logger with colorlog.

        Args:
            log_file (str): Path to the log file.

        Returns:
            logging.Logger: Configured logger object.
        """
        # Create a file handler

        file_handler = logging.FileHandler(log_file)
        # Create a formatter for the file logs
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='[%Y-%m-%d] [%H:%M:%S]')# noqa
        # Set the formatters for the handlers
        file_handler.setFormatter(file_formatter)

        handler = colorlog.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter(
            '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
            datefmt='[%Y-%m-%d] [%H:%M:%S]',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            },
            style='%'
        ))

        logger = colorlog.getLogger()
        if not logger.hasHandlers():
            logger.addHandler(handler)
            logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
