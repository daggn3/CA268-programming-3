def set_stuff(a,b):
	inter = set.intersection(a,b)
	c = []
	for i in a:
		c.append(a[i])
	for j in b:
		c.append(b[j])
	union = c - inter
	return union,a.subset(b),a.superset(b) 