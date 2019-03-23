class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):

        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += ptr.item + ""
            ptr = ptr.next

        return tmp_str

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            return item

    def is_empty(self):
        return self.head == None

    def count(self):
        count = 0
        ptr = self.head
        while ptr != None:
            count += 1
            ptr = ptr.next

        return count

    def contains(self, arg):
        ptr = self.head
        while ptr != None:
            if ptr.item == arg:
                return True
            else:
                ptr = ptr.next
        return False

    def after(self, arg):
        ptr = self.head
        while ptr != None:
            if ptr.item == arg:
                return ptr.next.item
            ptr = ptr.next

    def before(self, arg):
        ptr = self.head
        previous = None
        while ptr != None:
            if ptr.item == arg:
                return previous
            previous = ptr.item
            ptr = ptr.next

    def append(self, item):
        ptr = self.head
        if ptr != None:
            while ptr.next:
                ptr = ptr.next
            ptr.next = Node(item, ptr.next)
        else:
            self.head = Node(item, self.head)

    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += ptr.item + " "
            ptr = ptr.next

        return tmp_str

    def rotate(self):
        self.append(self.head.item)
        self.remove()
