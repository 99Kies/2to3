#-*- coding:utf-8 -*-
import os
import sys
WIN = sys.platform.startswith('win')
if WIN:
    path_sprit = '\\'
else:
    path_sprit = '/'

def py2to3(path):
    '''
    :param path: Absolute path to the target project folder
    :return: no return
    '''
    for i in os.listdir(path):
        path2 = os.path.join(path, i)
        if os.path.isdir(path2): # 如果为文件夹，则进入递归
            py2to3(path2)
        else:
            if 'py' == i.split('.')[1] and len(i.split('.')) == 2: # 如果不为文件夹并且为python文件则进行转换
                dir = path+path_sprit+i
                print(dir)
                print(os.system(r'python 2to3.py -w %s' % dir))
                # Make the conversion if you through: pip install 2to3 .can use: os.system(r'2to3 -w %s' % dir）


if __name__ == '__main__':
    print('Please provide an absolute path parameter.')
    try:
        path = sys.argv[1]
        print(("Let's look in %s." % path))
    except:
        print("Error, You Need Offer A Filepath!!! ")
    py2to3(path)

