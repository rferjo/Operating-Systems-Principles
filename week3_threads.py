"""
A multithreaded program that uses three threads to display messages.
"""

import threading


def functionOne():
    """
    Displays a message from the first function.
    """
    print("Function One is running in a thread.")


def functionTwo():
    """
    Displays a message from the second function.
    """
    print("Function Two is running in a thread.")


def functionThree():
    """
    Displays a message from the third function.
    """
    print("Function Three is running in a thread.")


def main():
    """
    Entry point of the program. Creates, starts, and joins threads.
    """

    # Create thread objects and connect them to functions
    one_thread = threading.Thread(target=functionOne, name="one-thread")
    two_thread = threading.Thread(target=functionTwo, name="two-thread")
    three_thread = threading.Thread(target=functionThree, name="three-thread")

    # Start each thread
    one_thread.start()
    two_thread.start()
    three_thread.start()

    # Wait for all threads to finish
    one_thread.join()
    two_thread.join()
    three_thread.join()

    print("All threads have finished running.")


if __name__ == "__main__":
    main()
    