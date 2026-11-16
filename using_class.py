from collections import deque
class MyQueue:
    def __init__(self):
        self.queue=deque()
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.popleft()
    def peek(self):
        if not self.queue:
            return None
        return self.queue[0]
    def display(self):
        print(self.queue)

q=MyQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.dequeue())
q.display()
print(q.peek())

