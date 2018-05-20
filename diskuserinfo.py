#!/usr/bin/env python
# -*- coding:UTF-8 -*-
####涉及到文件操作、join方法用于将序列中的元素以指定的字符连接生成一个新的字符串,格式：str.join()
import time
import os
new_time = time.strftime("%Y-%m-%d")
disk_status = str(os.popen('df -h').readlines())
str1 = "".join(disk_status)
f = open(new_time + '.log','a+')
f.write(disk_status)
f.flush()
f.close() 
