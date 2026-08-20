"""
    Class:   CS-510
    Author:  Rebecca Ferjo
    Date:    May 21, 2026

    Description: This program demonstrates operating system performance and
                 optimization concepts by displaying disk, CPU, memory,
                 threading, and error-handling information.
"""

import os
import psutil
import sys
import threading


def printBlankLines(lines: int):
    for i in range(lines):
        print("")


def printMsg1(num):
    print("Thread 1 cubed: {}".format(num * num * num))
    print("Thread 1 ID: {}".format(threading.get_ident()))


def printMsg2(num):
    print("Thread 2 squared: {}".format(num * num))
    print("Thread 2 ID: {}".format(threading.get_ident()))


def bytes_to_gb(size_bytes: int) -> float:
    """Convert bytes into gigabytes for readable output."""
    return size_bytes / (1024 ** 3)


def getFileDiskUsageStatistics() -> None:
    """Display disk usage statistics and information about a sample file."""
    print("Getting Disk Statistics")
    print("-----------------------")
    file_name = "./projecttwo.txt"

    try:
        # Create the required sample file if it does not already exist.
        if not os.path.exists(file_name):
            with open(file_name, "w", encoding="utf-8") as file:
                file.write("Sample file for CS 510 Project Two disk usage testing.\n")
                file.write("This file is used to demonstrate file statistics.\n")

        disk_usage = psutil.disk_usage(".")
        print("Disk Usage:")
        print("  Total Disk Space: {:.2f} GB".format(bytes_to_gb(disk_usage.total)))
        print("  Used Disk Space:  {:.2f} GB".format(bytes_to_gb(disk_usage.used)))
        print("  Free Disk Space:  {:.2f} GB".format(bytes_to_gb(disk_usage.free)))
        print("  Percent Used:     {}%".format(disk_usage.percent))

        file_stats = os.stat(file_name)
        print("\nFile Information:")
        print("  File Name:        {}".format(file_name))
        print("  File Size:        {} bytes".format(file_stats.st_size))
        print("  Absolute Path:    {}".format(os.path.abspath(file_name)))
        print("  Last Modified:    {}".format(file_stats.st_mtime))

        with open(file_name, "r", encoding="utf-8") as file:
            print("  File Contents:    {}".format(file.readline().strip()))

    except OSError as error:
        print("A disk or file error occurred: {}".format(error))

    printBlankLines(2)


def getMemoryStatistics() -> None:
    """Display physical and virtual memory statistics using psutil."""
    print("Getting Memory Statistics")
    print("-------------------------")

    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()

    print("Virtual Memory:")
    print("  Total Memory:     {:.2f} GB".format(bytes_to_gb(virtual_memory.total)))
    print("  Used Memory:      {:.2f} GB".format(bytes_to_gb(virtual_memory.used)))
    print("  Available Memory: {:.2f} GB".format(bytes_to_gb(virtual_memory.available)))
    print("  Percent Used:     {}%".format(virtual_memory.percent))

    print("\nSwap Memory:")
    print("  Total Swap:       {:.2f} GB".format(bytes_to_gb(swap_memory.total)))
    print("  Used Swap:        {:.2f} GB".format(bytes_to_gb(swap_memory.used)))
    print("  Free Swap:        {:.2f} GB".format(bytes_to_gb(swap_memory.free)))
    print("  Percent Used:     {}%".format(swap_memory.percent))

    printBlankLines(2)


def getCpuStatistics() -> None:
    """Display CPU usage, count, frequency, and active process information."""
    print("Getting CPU Statistics")
    print("----------------------")

    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count_logical = psutil.cpu_count(logical=True)
    cpu_count_physical = psutil.cpu_count(logical=False)
    cpu_freq = psutil.cpu_freq()

    print("CPU Information:")
    print("  CPU Usage:        {}%".format(cpu_percent))
    print("  Logical CPUs:     {}".format(cpu_count_logical))
    print("  Physical CPUs:    {}".format(cpu_count_physical))

    if cpu_freq is not None:
        print("  Current Frequency: {:.2f} MHz".format(cpu_freq.current))
        print("  Maximum Frequency: {:.2f} MHz".format(cpu_freq.max))

    print("\nCurrent Process Information:")
    current_process = psutil.Process(os.getpid())
    print("  Process ID:       {}".format(current_process.pid))
    print("  Process Name:     {}".format(current_process.name()))
    print("  Process Status:   {}".format(current_process.status()))
    print("  Process CPU %:    {}".format(current_process.cpu_percent(interval=0.1)))
    print("  Process Memory:   {:.2f} MB".format(current_process.memory_info().rss / (1024 ** 2)))

    printBlankLines(2)


def showThreadingExample() -> None:
    """Create, run, and destroy two threads that call different functions."""
    print("Demonstrating Threading")
    print("-----------------------")

    thread_one = threading.Thread(target=printMsg1, args=(3,), name="CubeThread")
    thread_two = threading.Thread(target=printMsg2, args=(4,), name="SquareThread")

    print("Creating threads:")
    print("  {} created.".format(thread_one.name))
    print("  {} created.".format(thread_two.name))

    print("\nStarting threads:")
    thread_one.start()
    thread_two.start()

    print("\nWaiting for threads to finish:")
    thread_one.join()
    print("  {} has finished and was destroyed.".format(thread_one.name))

    thread_two.join()
    print("  {} has finished and was destroyed.".format(thread_two.name))

    print("Done With Threading!")

    printBlankLines(2)


def showErrorHandling() -> None:
    """Cause a divide-by-zero error and handle it without stopping the program."""
    print("Demonstrating Error Handling")
    print("----------------------------")

    try:
        numerator = 10
        denominator = 0
        print("Attempting to divide {} by {}.".format(numerator, denominator))
        res = numerator / denominator

    except ZeroDivisionError as error:
        print("Error caused: {}".format(error))
        print("You can't divide by zero!")

    except MemoryError:
        print("Memory Error!")

    else:
        print("Result is", res)

    finally:
        print("Execution complete.")

    printBlankLines(2)


def main() -> int:
    print("Starting Program")
    print("=============================")

    getFileDiskUsageStatistics()

    getCpuStatistics()

    getMemoryStatistics()

    showThreadingExample()

    showErrorHandling()

    return 0


if __name__ == '__main__':
    sys.exit(main())
