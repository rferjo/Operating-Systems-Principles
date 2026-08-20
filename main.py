"""
Module Four Activity
Author: Rebecca Ferjo

This program displays CPU and memory information
using the psutil library.
"""

import psutil


def get_cpu_usage():
    """
    Retrieve the current CPU utilization percentage.
    """
    return psutil.cpu_percent(interval=1)


def get_cpu_count():
    """
    Retrieve the total number of logical CPU cores.
    """
    return psutil.cpu_count(logical=True)


def get_memory_stats():
    """
    Retrieve the system's memory usage statistics.
    """

    # Convert bytes to gigabytes for easier readability
    bytes_per_gb = 1024 ** 3

    memory = psutil.virtual_memory()

    total = memory.total / bytes_per_gb
    used = memory.used / bytes_per_gb
    available = memory.available / bytes_per_gb

    return total, used, available


def display_resource_report():
    mem_total, mem_used, mem_available = get_memory_stats()

    print("\n===== SYSTEM RESOURCE REPORT =====")
    print(f"CPU Usage:          {get_cpu_usage():.1f}%")
    print(f"CPU Cores:          {get_cpu_count()}")
    print(f"Total Memory:       {mem_total:.2f} GB")
    print(f"Memory Used:        {mem_used:.2f} GB")
    print(f"Memory Available:   {mem_available:.2f} GB")
    print("==================================\n")


def main():
    display_resource_report()


if __name__ == "__main__":
    main()