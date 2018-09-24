from multiprocessing.dummy import Pool
import threading
import os
import fnmatch
from PIL import Image
import shutil
import sys
import time
import timeit


def resize(file):
    print(f'Resizing {file} in thread {threading.get_ident()}')
    file_name, ext = file.split('.')
    os.chdir(npath1)
    im = Image.open(file)

    Hpixel = im.size[0]/(10)
    Wpixel = im.size[1]/(10)
    new_file = file_name+'t.jpg'
    im.resize((int(Hpixel),int(Wpixel))).save(new_file, "JPEG")
    nim = Image.open("%st.jpg" %file_name)
    print ('\tresized image')
    print ('\t\tOld Size: ' ,im.size)
    print ('\t\tNew size: ' ,nim.size)
    im.close()
    nim.close()
    os.chdir(npath1)
    shutil.copy2(new_file, npath2)
    print ('\tmoved image')
    os.chdir(npath2)
    if fnmatch.fnmatch(new_file,'*t.jpg'):
        os.rename(new_file, file_name+'.jpg')
        print ('\trenamed image')
    os.chdir(npath1)
    new_path = npath1+'\\'+new_file
    if fnmatch.fnmatch(new_file,'*t.jpg'):
        os.remove(new_path)
        print ('\tremoved copy')

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
        pool.map(resize, files_list)
    stop = timeit.default_timer()
    print ('\n\nExiting main thread!! Time: ', stop - start)
