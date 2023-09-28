"""
Implementing queue using stacks
A stack is a data type which follows LIFO (Last In, First Out), in this, data is added like a stack of books, each time
a new one is added, it is placed on top of the previous ones.
Here we are going to use this to implement a queue data type, which follows FIFO (First In, First Out). In this, the 
data is added like a queue, one after the other, and the first one to be taken out will always be the first 
data that was added into it

"""

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    #Addign a new value into the queue
    def en_queue(self, x):
        self.s1.append(x)

    #Popping out the firstmost value added to the 'Queue'
    def de_queue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            return -1
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
        else:
            return self.s2.pop() 
        

if __name__=="__main__":
    q = Queue()
    q.en_queue(1)
    q.en_queue(2)
    q.en_queue(3)
    q.en_queue(4)

    q.de_queue()
    q.de_queue()
