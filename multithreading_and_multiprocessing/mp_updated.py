import concurrent.futures
import time

starting_time = time.perf_counter()


def do_something_new(seconds):
    print(f"sleeping for {seconds} sec")
    time.sleep(seconds)
    return f"done sleeping{seconds}"


def mainidea():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]

        results = [executor.submit(do_something_new, sec) for sec in secs]

        for f in concurrent.futures.as_completed(results):
            print(f.result())


if __name__ == '__main__':
    mainidea()
    finish_time = time.perf_counter()

    print(f" {round(finish_time - starting_time, 2)} seconds taken to execute")








