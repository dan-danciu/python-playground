from multiprocessing import Process, Queue
import time
import os

def info(title):
    if 'start' in title:
        print(f'{title}:\n\tmodule name: {__name__}\n\tparent process: {os.getppid()}\n\tprocess id: {os.getpid()}')
    else:
        print(f'{title}\n\tthread time: {time.thread_time()}')


def f(q):
    info('function f start')
    q.put([42, None, 'hello'])
    info('function f end')

def g(q):
    info('function g start')
    print(q.get())
    info('function g end')

if __name__ == '__main__':
    info('main line start')
    q = Queue()
    p = Process(target=f, args=(q,))
    r = Process(target=g, args=(q,))
    p.start()
    r.start()
    p.join()
    info('main line end')
