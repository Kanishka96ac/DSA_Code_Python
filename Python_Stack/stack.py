'''
push() --- Add element to the stack
pop() --- remove the top element , And return removed element value
peek() --- return the top element of the stack
isEmpty() --- Boolean result (empty or not)
isFull --- Boolean result (if maxSize =5 , then full or not)
delete() --- Delete the stack
'''

class Stack:
    def __init__(self):
        self.list=[]
        
    def __str__(self):
        return str(self.list)
        
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def push(self, value):
        return self.list.append(value)
        
    def pop(self):
        if self.isEmpty():
            return "The Stack is Empty"
        else:
            return self.list.pop()
        
    def delete(self):
            self.list = None
    
    def peek(self):
        if self.isEmpty():
            return "The Stack is Empty"
        else:
            return self.list[-1]
    
myStack = Stack()

myStack.push(5)
myStack.push(2)
myStack.push(3)
myStack.push(4)
print(myStack)
print(myStack.peek())
print(myStack.peek())
print(myStack.peek())
print(myStack.peek())
print(myStack.pop())
print(myStack.pop())

print(myStack.pop())
print(myStack.pop())
print(myStack.pop())

print('removed :',myStack)

print(myStack.isEmpty())