import sys

def insertion_sort(lst):
	com = 0
	moves = 0
	for todo in range(1, len(lst)):
		tobeinserted = lst[todo]
		moves += 1

		i = todo
		while i > 0 and tobeinserted < lst[i-1]:
			lst[i] = lst[i-1]

			moves += 1
			compare += 1
			i -= 1

		lst[i] = tobeinserted  # Found the place for this item, plonk it in

		if i > 0:
			com += 1
			moves += 1

		else:
			moves += 1

	return com, moves

def main():
	# Read each test case
	line = "a b c d e"
	items = line.strip().split()
	
	orig = list(items)

	result = insertion_sort(items)
	if items != sorted(orig):
		print("The list is not sorted.")
	else:
		print(result)

if __name__ == "__main__":
	main()