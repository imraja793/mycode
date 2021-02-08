from threading import Thread
from time import sleep

def wish(name):
    for _ in range(10):
        # we have used flush = True to get the desired output it will
        # flush any dependencies and firstly print Good Evening: then smith
        print('Good Evening:', end='', flush=True)
        sleep(5)

        print(name)

wish('Smith')
