class MyQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def enqueue(self,value):
        self.stack1.append(value)
    def dequeue(self):
        if not self.stack1 and not self.stack2:
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
q=MyQueue()
q.enqueue(4)
q.enqueue(10)
q.enqueue(70)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

