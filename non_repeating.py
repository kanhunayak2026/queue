from collections import deque
def first_non_repeating(stream):
    queue=deque()
    freq={}
    for ch in stream:
        freq[ch]=freq.get(ch,0)+1
        queue.append(ch)
        while queue and freq[queue[0]]>1:
            queue.popleft()
        if queue:
            print(queue[0])
        else:
            print(-1)
first_non_repeating("aabc")