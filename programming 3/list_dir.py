from __future__ import print_function
import sys
import os 
if len(sys.argv) == 2:
	path = sys.argv[1]
else:
	path ="."


files=os.listdir(path)

for name in files:
	print(name)
	full_path = os.path.join(path,name)
	print(full_path)