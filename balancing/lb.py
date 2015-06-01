
import psutil
import time 



print("Hello world !");

print(psutil.cpu_times())

while (True):
	print(psutil.cpu_times_percent(interval=1))
	time.sleep(1)
