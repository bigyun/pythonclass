#!/usr/bin/python
# coding: utf-8
import os,optparse
import os
from glob import glob #用到了这个模块
import sys
import commands

class Search_File():
    def __init__(self,file,file_dir):
        self.file = file
        self.file_dir = file_dir
    def get_all_file(self):
        file_list = []
        if self.file_dir is None:
            raise Exception("floder_path is None")
        for dirpath,dirnames,filenames in os.walk(self.file_dir):
            for name in filenames:
                file_list.append(dirpath+'/'+name)
        return file_list
    def is_file_contain(self):
        datas =  self.get_all_file()
        for files in datas:
            if self.file in files:
                print files




if __name__ == '__main__':
    files = Search_File('pys','/data/django')
    print files.is_file_contain()
