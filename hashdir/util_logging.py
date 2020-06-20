import logging


def adjust_logger():
    logger = logging.getLogger()
    logger_handler = logging.StreamHandler()
    logger.addHandler(logger_handler)
    logger_handler.setFormatter(logging.Formatter("\n%(levelname)s: %(message)s"))
    logger.setLevel(logging.INFO)
    return logger


def get_log_level(log_level_str):
    if log_level_str == "error":
        return logging.ERROR
    if log_level_str == "info":
        return logging.INFO
    if log_level_str == "debug":
        return logging.DEBUG
    return logging.ERROR
