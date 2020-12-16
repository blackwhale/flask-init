import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(funcName)s:%(lineno)d] %(message)s'
)
def get_logger():
    logger = logging.getLogger(__name__)
    return logger