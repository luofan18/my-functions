#! /usr/bin/env python
'''Define some function which are frequently used'''

import os, shutil
import numpy as np

def clear_dir(path):
    '''remove all files and subfolders under a diretory'''
    
    if not os.path.isdir(path):
        return
    for the_file in os.listdir(path):
        file_path = os.path.join(path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
            
def remove_dir(path):
    '''remove a directory and all content inside it'''
    
    shutil.rmtree(path)
    
def print_scale(name, scale):
    '''print a scale variable'''
    
    print ('{} is {}'.format(name, scale))

def print_shape(name, np_array):
    '''print the shape of np array'''
    
    print ('### {} shape is ###'.format(name))
    print (np_array.shape)
    
def print_np_array(name, np_array):
    '''print np array'''
    
    print ('### np array {} is ###'.format(name))
    print (np_array)
            
if __name__ == '__main__':
    pass
