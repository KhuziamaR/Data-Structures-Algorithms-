from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
def reverse_string(string):
    stack = Stack()
    result=""
    count = 0
    for char in string:
        stack.push(char)
        count+=1
    for char in range(count):
        result+= stack.pop()
    return result

string = '91-DIVOC ereuqnoc lliw eW'
# print(reverse_string(string))

def is_balanced(string):
    p = Stack()
    p2 = Stack()
    b = Stack()
    b2 = Stack()
    i = Stack()
    i2 = Stack()
    for char in string:
        if char == '(':
            p.push(char)
        if char == ')':
            p2.push(char)
        if char == '{':
            b.push(char)
        if char == '}':
            b2.push(char)
        if char == '[':
            i.push(char)
        if char == ']':
            i2.push(char)
        if i.size() == i2.size() and p.size() == p2.size() and b.size() == b2.size():
            return True
        return False

# print(is_balanced("({a+b})"))
# print(is_balanced("((a+b))")

