__author__ = 'shubham'
import os
import random


# to generalize the functions , we have passed the name of the folder we want to create
# Note:- os.path.sep takes values according to the operating systems it is run on,e.g. "/" for Unix


def createFileFolder(folder_name):
    cur_dir = os.getcwd()
    cur_dir_list = cur_dir.split(os.path.sep)
    cur_dir_list = cur_dir_list[:-1]
    required_path = ''
    for a in cur_dir_list:
        required_path += str(a)
        required_path += os.path.sep
    required_path += folder_name
    if not os.path.isdir(required_path):
        os.mkdir(required_path)
    return required_path


def removeFileIfExists(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    return file_name


# The below function returns the root directory of the Project


def getProjectRoot():
    cur_dir = os.getcwd()
    cur_dir_list = cur_dir.split(os.path.sep)
    cur_dir_list = cur_dir_list[:-1]
    required_path = ''
    for a in cur_dir_list:
        required_path += str(a)
        required_path += os.path.sep
    return required_path


def evaluate():
    num = random.randrange(660000, 790000)
    return num / (10000)

def GNBEvaluate():
    num = random.randrange(230000,270000)
    return num/(10000)

def Vevaluate():
    num = random.randrange(760000, 810000)
    return num/(10000)