__author__ = 'olgashulga'

import threading

def writer(x,event_for_wait,event_for_set):
    for i in xrange(10):
        event_for_wait.wait()
        event_for_wait.clear()
        print x
        event_for_set.set()

event1 = threading.Event()
event2 = threading.Event()
event3 = threading.Event()

thread1 = threading.Thread(target=writer, args=(0, event1, event2))
thread2 = threading.Thread(target=writer, args=(1, event2, event3))
thread3 = threading.Thread(target=writer, args=(2, event3, event1))


thread1.start()
thread2.start()
thread3.start()

event1.set()

thread1.join()
thread2.join()
thread3.join()