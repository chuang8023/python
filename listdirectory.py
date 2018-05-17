#!/usr/bin/env python
import os
for root,dirs,files in os.walk('/tmp'):
	print(os.path.join(dirs))
os.walk('/tmp')

