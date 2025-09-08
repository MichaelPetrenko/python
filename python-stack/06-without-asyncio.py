# Without async
import time
from turtle import pen

def parser(sitename):
    for page in range(0, 10):
        print(sitename, page)
        time.sleep(2)

if __name__ == '__main__':
    start_time = time.time()
    for site in ["site1", "site2", "site3"]:
        parser(site)

    print("--- %s seconds ---" % (time.time() - start_time))