import logging
import time


def our_logger(name='Default', filename='logs.log'):
    """
    :param name: logger name
    :param filename: logs will be saved in this file
    :return: none
    logger instantiation example:
    our_logger(name='optimization', filename='optimization.log')
    logger = (logging.getLogger('optimization'))
    logger usage example:
    logger.debug(f'Total gain is {total_gain}')
    logger.debug(f'Total runtime: {total_program_time} [seconds]')
    logger.debug('-----------------------------------')
    logger output example (for the above usage examples):
    [2022-05-01 11:49:12,582 [UTC];optimization;DEBUG]:Total gain is 2015.5
    [2022-05-01 11:49:12,583 [UTC];optimization;DEBUG]:Total runtime: 0:00:04.550108 [seconds]
    [2022-05-01 11:49:12,584 [UTC];optimization;DEBUG]:-----------------------------------
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s [UTC];%(name)s;%(levelname)s]:%(message)s')
    logging.Formatter.converter = time.gmtime
    log_filename = f"logs/{filename}"
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)
    file_handler = logging.FileHandler(filename, mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)