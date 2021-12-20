import datetime
import time

t1 = datetime.datetime.now()
time.sleep(5)
print(datetime.datetime.now() - t1)

t2 = time.time()
time.sleep(3)
print(time.time() - t2)