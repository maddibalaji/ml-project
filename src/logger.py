import logging
import os
from datetime import datetime
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_paths = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_paths, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_paths, LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO,format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s')
if __name__=="__main__":
    logging.info("Logging has started") 
