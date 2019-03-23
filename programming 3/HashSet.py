from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)
        check = 0
        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList()    # Need a new linked list for this entry
        else:
            check = 1

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)
        if check:
            return index, item

    def average_bucket_length(self):
        lst = []
        for bucket in self.table:
            if bucket != None:
                lst.append(len(bucket))
        return sum(lst)/len(lst)

    def min_max_bucket_length(self):
        lst = []
        for bucket in self.table:
            if bucket != None:
                lst.append(len(bucket))
                mx = max(lst)
                mn = min(lst)
        return mn,mx

    def __iter__(self):
        table =[]
        ptr = None
        for i in range(0, len(self.table)):
            if self.table[i]:
                ptr = self.table[i].head
                while ptr != None:
                    table.append(ptr.item)
                    ptr = ptr.next
        return iter(sorted(table))