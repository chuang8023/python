# coding = utf-8
#! /usr/bin/env python
import os
import sys

if os.getuid() == 0:
    pass
else:
    print ("��ǰ�û�����root�û�������root�û�ִ�нű�").encode('gbk')
    sys.exit(1)

#version=input("������python�汾(2.7|3.5)")
#if version == '2.7':
#    url = 'https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz'
#elif version == '3.5':
#    url =  'https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz'
#else:
#    print("������İ汾���������ʵ")
#    sys.exit(1)
#
#cmd = 'wget' +url
#res = os.system(cmd)
#if res != 0:
#    print("����Դ���ʧ�ܣ���������")
#    sys.exit(1)
#
#
#if version == '2.7':
#    package_name = 'Python-2.7.12'
#else:
#    package_name = 'Pthon-3.5.2'
#cmd = 'tar xf' +package_name+'.tgz'
#res = os.system(cmd)
