from multiprocessing import Pool
import os
from itertools import product
import fnmatch
from PIL import Image
import shutil
import sys
import time
import timeit


def resize(file, npath1, npath2):
    info(f'{file} start')
    file_name, ext = file.split('.')

    file = npath1+'\\'+file
    im = Image.open(file)

    Hpixel = im.size[0]/(10)
    Wpixel = im.size[1]/(10)
    new_file = npath2+'\\'+file_name+'.'+ext
    im.resize((int(Hpixel),int(Wpixel))).save(new_file, "JPEG")
    nim = Image.open(new_file)
    print ('\tresized image')
    print ('\t\tOld Size: ' ,im.size)
    print ('\t\tNew size: ' ,nim.size)
    im.close()
    nim.close()
    info(f'{file} end')

def info(title):
    if 'start' in title:
        print(f'{title}:\n\tmodule name: {__name__}\n\tparent process: {os.getppid()}\n\tprocess id: {os.getpid()}')
    else:
        print(f'{title}\n\tthread time: {time.thread_time()}')


if __name__ == '__main__':
    start = timeit.default_timer()
    path = 'D:\\'
    os.chdir(path)


    try:
        path1  = sys.argv[1]
        path2 = 'resized_'+sys.argv[1]
    except IndexError:
        print("\nPlease enter a directory.\nUsage example: python img_resize.py 'directory'\n\n\n")
        quit()
    npath1 = path+path1
    npath2 = path+path2

    if not os.path.exists(path2):
        os.makedirs(path2)

    files_list = []

    for file in os.listdir(path1):
        if fnmatch.fnmatch(file,'*.jpg'):
            files_list.append(file)
    with Pool(4) as pool:
        pool.starmap(resize, product(files_list, [npath1], [npath2]))
    stop = timeit.default_timer()
    print ('\n\nExiting main thread!! Time: ', stop - start)
