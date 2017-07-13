import _thread
import time
import threading
counter = 0
lock = threading.Lock()
def counter_work(name, delay):
	global lock
	global counter
	while counter < 1000:
		time.sleep(delay)
		lock.acquire()
		counter += 1
		print(counter,name)
		lock.release()
_thread.start_new_thread(counter_work, ("Thread 1",1))
_thread.start_new_thread(counter_work, ("Thread 2",1))
_thread.start_new_thread(counter_work, ("Thread 3",1))
_thread.start_new_thread(counter_work, ("Thread 4",1))
_thread.start_new_thread(counter_work, ("Thread 5",1))
_thread.start_new_thread(counter_work, ("Thread 6",1))
_thread.start_new_thread(counter_work, ("Thread 7",1))
_thread.start_new_thread(counter_work, ("Thread 8",1))
while counter < 1000:
	pass
