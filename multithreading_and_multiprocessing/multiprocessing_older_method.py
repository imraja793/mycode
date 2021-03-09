import multiprocessing
import time

starting_time = time.perf_counter()


def do_something(seconds):
    print("sleeping for 1 sec")
    time.sleep(seconds)
    print("done sleeping")


if __name__ == '__main__':

    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()
    finish_time = time.perf_counter()

    print(f" {round(finish_time - starting_time, 2)} seconds taken to execute")

