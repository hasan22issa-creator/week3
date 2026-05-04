from decorators import log_call

from comprehensions import squares

from filter_tasks import filter_tasks, tasks

from timer import Timer

import time
 
 
def run_decorators():

 
    @log_call

    def add(a, b):

        return a + b
 
    @log_call

    def greet(name, greeting="Hello"):

        return f"{greeting}, {name}!"
 
    add(10, 5)

    greet("Hasan", greeting="Hey")
 
 
def run_comprehensions():


    print("Squares:", squares)

 
 
 
def run_filter_tasks():


 
    open_tasks = filter_tasks(tasks, status="open")

    print("Open tasks:")

    for t in open_tasks:

        print(f"  - {t['title']} (owner: {t['owner']})")
 
    hasan_tasks = filter_tasks(tasks, owner="Hasan")

    print("\nHasan's tasks:")

    for t in hasan_tasks:

        print(f"  - {t['title']} (status: {t['status']})")
 
    ali_open = filter_tasks(tasks, status="open", owner="Ali")

    print("\nAli's open tasks:")

    for t in ali_open:

        print(f"  - {t['title']}")
 
 
def run_timer():

 
    with Timer():

        result = [n ** 2 for n in range(1_000_000)]
 
    with Timer() as t:

        time.sleep(0.2)
 
    print(f"We can still access the time after: {t.elapsed:.4f}s")
 
 
if __name__ == "__main__":

    run_decorators()

    run_comprehensions()

    run_filter_tasks()

    run_timer()
 