import concurrent.futures
import time

starting_time = time.perf_counter()

def do_something(n):
    print(f"sleeping for {n} sec")
    time.sleep(n)
    return f"done sleeping {n} sec"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs]
    #
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    results = executor.map(do_something, secs)


finish_time = time.perf_counter()

print(f" {round(finish_time - starting_time, 2)} seconds taken to execute")

