from collections import deque
def reverse(queue,k):
    stack=[]
    for i in range(k):
        stack.append(queue.popleft())
    while stack:
        queue.append(stack.pop())
    for i in range(len(queue)-k):
        queue.append(queue.popleft())
    return queue
q = deque([10, 20, 30, 40, 50])

reverse(q, 3)

print(q)