import pandas as pd

import logging
LOG_FILENAME = 'db_logs.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, 
                    format="%(asctime)s %(levelname)s: %(message)s", datefmt='%m-%d-%Y %I:%M:%S %z')
logger = logging.getLogger()