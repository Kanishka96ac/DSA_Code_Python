'''
First In First Out (FIFO)

enqueue() --- Add element to the Queue
dequeue() --- remove element from the Queue 
peek() --- return the first element of the Queue
isEmpty() --- Boolean result (empty or not)
isFull --- Boolean result (if maxSize =5 , then full or not)
deleteQueue() --- Delete the Queue
'''

class Queue:
    
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        return str(self.queue)
    
    def isEmpty(self):
        if self.queue == []:
            return True
        else: 
            return False
        
    def enqueu(self, value):
        return self.queue.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            return self.queue[0]
        
    def delete(self):
        self.queue = None
            
myQueue = Queue()
print(type(myQueue))