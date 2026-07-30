# We're going to use Python's standard logging library instead of print().
# In production, services typically write structured logs to files and/or stdout.

import logging

def get_logger(logger_name: str):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    return logging.getLogger(logger_name)

