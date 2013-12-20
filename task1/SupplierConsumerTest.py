import threading

__author__ = 'olgashulga'

from threading import Thread
import time



class Store():
    count = 0
    FULL=20
    lock = threading.Lock()

    def conectCount(self,val,name):
        self.lock.acquire()
        print str(name)+" blocked Store."
        self.count=self.count+val
        print self.count
        print str(name)+" unblocked Store"
        self.lock.release()

    def put(self,name):

        if self.count < self.FULL:
            self.conectCount(1,name)
        else:
            print "Store is full."


    def get(self,name):

        if self.count > 0:
            self.conectCount(-1,name)
        else:
            print "Store is empty."



class Consumer(Thread):

    product = 0

    def __init__(self, name,store):
        Thread.__init__(self, name=name)
        self.store = store

    def run(self):



        while self.product < 20:
            self.store.get(self.name)
           # time.sleep(0.7)
            self.product += 1


class Supplier(Thread):

    product =20

    def __init__(self, name,store):
        Thread.__init__(self, name=name)
        self.store = store

    def run(self):



        while self.product > 0:
            self.store.put(self.name)
            #time.sleep(0.2)
            self.product -= 1



store = Store()
consumer = Consumer('consumer',store)
supplier = Supplier('supplier',store)
consumer.start()

supplier.start()

consumer.join()
supplier.join()



print "Main script done."