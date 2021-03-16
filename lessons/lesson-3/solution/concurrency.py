from threading import active_count as count
from time import sleep	

def get_number_of_threads():
    return count()

def wait_until_threshold_reached(threshold):
    sleep(1)
    threads = count()
    while threads > threshold:
        threads = count()
        print('still waiting for %d threads' % threads)
        sleep(1)

