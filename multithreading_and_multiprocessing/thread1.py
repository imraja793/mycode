import time
import threading

starting_time = time.perf_counter()


def do_something():
    print("sleeping for 1 sec")
    time.sleep(1)
    print("done sleeping")


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()
t1.join()
t2.join()

# do_something()
# do_something()


finish_time = time.perf_counter()

print(f" {round(finish_time - starting_time, 2)} seconds taken to execute")
