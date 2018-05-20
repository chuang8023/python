#!/usr/bin/env python
# -*-coding:UTF-8 -*-
import os
"""os.walk()方法用于通过再目录树种游走输出在目录中的文件名，向上或者向下
格式：os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
top：需要遍历的目录地址，返回一个三元组(root,dirs,files)
root：指当前正在遍历的这个文件夹本身地址
dirs：一个list，该文件夹中所有的目录的名字（不包括子目录）
files：一个list，该文件夹中所有文件(不包括子目录)
"""
for root,dirs,files in os.walk('/tmp'):
	print(os.path.join(dirs))
os.walk('/tmp')
