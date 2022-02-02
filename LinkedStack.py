class Element:
    def __init__(self, essence):
        self.essence = essence
        self.next = None
        self.MAX_SIZE = 1024
    def __str__(self):
        if self != None:
            return str(self.essence)

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return 'Empty Stack!'
        indexer = self.top
        result = "Top -> "
        while indexer:
            result += str(indexer.essence) + "\n"
            indexer = indexer.next
        result += "Bottom"
        return result

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size >= 1024

    def getSize(self):
        return self.size

    def push(self, value):
        if self.isEmpty():
            elem = Element(value)
            self.top = elem
            elem.next = None
            self.size += 1
        elif self.isFull():
            return "Stack is full!\nSize is 1024 elements."
        else:
            elem = Element(value)
            elem.next = self.top
            self.top = elem
            self.size += 1
        print("Added " + str(elem) + " to the stack.")
        
    def pop(self):
        if self.isEmpty():
            raise Exception("Used pop function on an empty stack!")
        trash = self.top
        self.top = self.top.next
        self.size -= 1
        print("Popped " + str(trash) + " from the stack.")
        return trash.essence

