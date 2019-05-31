import time
from time import strftime, localtime
import logging
from get_connect_time import get_connect_time

fetch_hours = 4
fetch_period_min = 1
fetch_times = fetch_hours * 60 // fetch_period_min
fetch_period_sec = fetch_period_min * 60
logging.basicConfig(filename='connect.log', level=logging.INFO)
for k in range(fetch_times):
    logging_str = strftime("[%Y-%m-%d %H:%M:%S]: ", localtime(time.time())) + get_connect_time()
    print(logging_str)
    logging.info(logging_str)
    time.sleep(fetch_period_sec)
