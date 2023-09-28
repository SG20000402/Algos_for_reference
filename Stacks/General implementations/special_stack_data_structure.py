"""
Design and Implement Special Stack Data Structure
Design a stack data stucture which supports all stack operations
i.e. push(), pop(), is_empty(), is_full(), and get_min().
All of these operations must be O(1)
"""

class stack:
    def __init__(self):
        self.array = []
        self.top = -1
        self.max = 100
        self.min = None

    def push(self, val):
        self.array.append(val)
        self.top += 1
        if not self.min:
            self.min = val
        else:
            self.min = min(self.min, val)

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
            return
        return self.array.pop()

    
    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def is_full(self):
        if self.top == self.max-1:
            return True
        else:
            return False

    def is_min(self):
        return self.min
    

if __name__=="__main__":
    
    s = stack()
    print("Is the stack empty: ", s.is_empty())

    s.push(3)
    s.push(4)
    s.push(2)
    s.push(1)
    s.push(9)
    s.push(7)
    s.push(8)

    print(s.pop())
    print("Min value is: ", s.is_min())
    print("Is the stack empty: ", s.is_empty())
    print("Is the stack full?: ", s.is_full())

