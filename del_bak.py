#-*- coding:utf-8 -*-
import os
import sys
WIN = sys.platform.startswith('win')
if WIN:
    path_sprit = '\\'
else:
    path_sprit = '/'

def del_bak(path):
    '''
    :param path: Absolute path to the target project folder
    :return: no return
    '''
    for i in os.listdir(path):
        path2 = os.path.join(path, i)
        if os.path.isdir(path2): # 如果为文件夹，则进入递归
            del_bak(path2)
        else:
            if len(i.split('.')) == 3:
                if 'bak' in i.split('.')[2]:
                    dir = path+path_sprit+i
                    print(dir)
                    os.remove(dir)


# tochange(path)
if __name__ == '__main__':
    print('Please provide an absolute path parameter.')
    try:
        path = sys.argv[1]
        print(("Let's look in %s." % path))
    except:
        print("Error, You Need Offer A Filepath!!! ")
    del_bak(path)

