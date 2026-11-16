from collections import deque
def interval_queue(queue):
    n=len(queue)
    first_half=deque()
    for i in range(n//2):
        first_half.append(queue.popleft())
    while first_half:
        queue.append(first_half.popleft())
        queue.append(queue.popleft())
    return queue

q = deque([10, 20, 30, 40, 50, 60])

interval_queue(q)

print(q)