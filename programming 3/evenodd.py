import sys 
count = 0

for c in sys.argv[1]:
	count += 1

if count % 2 == 0:
	mid = count // 2
	print(sys.argv[1][mid:])
else:
	print (sys.argv[1][0]+sys.argv[1][-1])