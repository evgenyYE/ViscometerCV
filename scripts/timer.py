import time


def execution_time_plotter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print(f"Time: {total}")
        return rv

    return wrapper
