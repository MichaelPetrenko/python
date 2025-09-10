from threading import Thread
import time

def parser(site_name):
    time.sleep(2)
    print(site_name)
    return site_name

start_time = time.time()
t1 = Thread(target=parser, args=("Site 1",))
t2 = Thread(target=parser, args=("Site 2",))

t1.start()
t2.start()

rs1 = t1.join()
rs2 = t2.join()

print(rs1, rs2)
print("asdasd")
print("--- %s seconds ---" % (time.time() - start_time))