import logging
LOG_FILENAME = 'db_logs.log'

def prepare_logger(file_path : str = LOG_FILENAME) -> logging.RootLogger:
    '''
    return logger object. Helps not to init logger each time in each module
    # Logging HOWTO -> 
    # https://docs.python.org/3/howto/logging.html
    
    :Parameters:
    
    input
        - :file_path: path to file with logs
    return
        - :logger: ready to use in custom module logger object
    '''
    logging.basicConfig(filename=file_path, level=logging.DEBUG, 
                    format="%(asctime)s %(levelname)s: %(message)s", datefmt='%m-%d-%Y %I:%M:%S %z')
    logger = logging.getLogger()
    return logger