#-*- coding:utf-8 -*-
import os
import sys

from del_bak import del_bak

WIN = sys.platform.startswith('win')
if WIN:
    path_sprit = '\\'
else:
    path_sprit = '/'

CODE = '''print 123'''

filename = 'test_.py'

def test_file(path):
    '''
    :param path: Absolute path to the target project folder
    :return: no return
    '''
    for i in os.listdir(path):
        path2 = os.path.join(path, i)
        if os.path.isdir(path2): # 如果为文件夹，则进入递归
            file_name = path2+path_sprit+filename
            with open(file_name, 'w') as file:
                file.write(CODE)
            print(file_name)
            test_file(path2)
        else:
            print(path2)
            with open(path2, 'w') as file:
                file.write(CODE)


            
# tochange(path)
if __name__ == '__main__':
    print("to rebuild the testfile")
    del_bak('./test')
    test_file('./test')

