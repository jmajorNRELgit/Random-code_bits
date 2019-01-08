import threading
from time import sleep


def workerThread1():
    """
    This is where we handle the asynchronous I/O. For example, it may be
    a 'select(  )'. One important thing to remember is that the thread has
    to yield control pretty regularly, by select or otherwise.
    """
    while True:
        # To simulate asynchronous I/O, we create a random number at
        # random intervals. Replace the following two lines with the real
        # thing.

        sleep(1)
        print('Foo')

def workerThread2():
    """
    This is where we handle the asynchronous I/O. For example, it may be
    a 'select(  )'. One important thing to remember is that the thread has
    to yield control pretty regularly, by select or otherwise.
    """
    while True:
        # To simulate asynchronous I/O, we create a random number at
        # random intervals. Replace the following two lines with the real
        # thing.

        sleep(3)
        print('Bar')

thread1 = threading.Thread(target=workerThread1)
thread1.daemon = True
thread1.start(  )

thread2 = threading.Thread(target=workerThread2)
thread2.daemon = True
thread2.start(  )

while True:
    sleep(2)
    print('Spam')