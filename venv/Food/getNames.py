from pathlib import Path

import os
directories_in_curdir = filter(os.path.isdir, os.listdir(os.curdir))
#print(directories_in_curdir)
d=[]
for x in directories_in_curdir:
	d.append(x)
	print(x)
print(d)
	