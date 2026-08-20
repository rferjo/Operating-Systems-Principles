'''
This program demonstrates how a semaphore limits how
many threads can enter a shared section at once.

Fill out the part with # TODO
'''

import multiprocessing
import time
import random

#set number of max processes that can run at a time
max_concurrentprocesses = 4

#set total number of processes being run
total_processes = 10


#initialize semaphore
semaphore = multiprocessing.Semaphore(max_concurrentprocesses)


#create time function to display current time on call
def current_time():
    curr_time = time.localtime()
    current_time = time.strftime("%H:%M:%S", curr_time)
    return current_time


#create function that would use semaphore to manage processes
def processing(process_id):
    print(f"{current_time()} [WAIT] Process {process_id} is waiting for semaphore")

    #only allow limited number of processes at once
    with semaphore:

        print(f"{current_time()} [ACQUIRE] Process {process_id} has acquired semaphore")

        #simulate process doing work
        time.sleep(random.randint(1,5))

    print(f"{current_time()} [RELEASE] Process {process_id} has released semaphore")


if __name__ == "__main__":

    #print how many processes the semaphore will run at one time
    print("Semaphore has been initialized with the value of:", max_concurrentprocesses)

    #create multiprocess list to store all processes
    multiprocess = []

    for i in range(total_processes):

        m = multiprocessing.Process(target=processing, args=(i,))
        multiprocess.append(m)
        m.start()


    #loop through each process in the list to join in order
    #to wait for each process to finish before printing all done statement
    for m in multiprocess:
        m.join()

    print("All processes are done!")