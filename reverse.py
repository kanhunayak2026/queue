from collections import deque
def reverse_queue(queue):
    stack=[]
    while queue:
        stack.append(queue.popleft())
    while stack:
        queue.append(stack.pop())
    return queue
q = deque([10, 20, 30, 40])

reverse_queue(q)

print(q)