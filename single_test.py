from get_connect_time import get_connect_time
import time
from time import strftime, localtime
import logging

logging.basicConfig(filename='connect.log', level=logging.INFO)
logging_str = strftime("[%Y-%m-%d %H:%M:%S]: ",
                       localtime(time.time())) + get_connect_time()
logging.info(logging_str)
print(logging_str)
