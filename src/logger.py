import logging
LOG_FILENAME = 'db_logs.log'

def prepare_logger(file_path : str = LOG_FILENAME) -> logging.RootLogger:
    '''
    return logger object. Helps not to init logger's config and naive import logging each time in each module
    # Logging HOWTO -> 
    # https://docs.python.org/3/howto/logging.html
    
	* Now works with RootLogger, not Handlers.
	
    :Parameters:
    
    input
        - :file_path: path to file with logs
    return
        - :logger: logger object which is ready to use in custom module
    '''
    logging.basicConfig(filename=file_path, level=logging.DEBUG, 
                    format="%(asctime)s %(levelname)s: %(message)s", datefmt='%m-%d-%Y %I:%M:%S %z')
    logger = logging.getLogger()
    return logger