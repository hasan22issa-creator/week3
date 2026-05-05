import time


class Timer:

    def __enter__(self):
        # This runs the moment we enter the "with" block
        # We record the start time
        self.start = time.perf_counter()
        return self  # returning self lets us use "as t" to access the timer later

    def __exit__(self, exc_type, exc_val, exc_tb):
        # This runs automatically when the "with" block ends — even if there's an error
        self.elapsed = time.perf_counter() - self.start
        print(f"[TIMER] Done! Took {self.elapsed:.6f} seconds")
        return False  # False means: don't hide any errors that happened inside



# Basic usage
with Timer():
    # Simulate some work — squaring a million numbers
    result = [n ** 2 for n in range(1_000_000)]

# Capturing the timer object so we can use elapsed time later
with Timer() as t:
    time.sleep(0.2)  # Pretend we're doing something that takes 0.2 seconds

print(f"We can still access the time after: {t.elapsed:.4f}s")