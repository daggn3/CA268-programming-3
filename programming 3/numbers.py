def get_counts(lst):
	counts = [0] * 10
	for i in lst:
		if len(i) <= 9:
			counts[len(i.strip())] += 1
	return counts