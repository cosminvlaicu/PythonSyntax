q = []

q.append(1)
q.append(2)
q.append(3)

while q:
    print(q.pop(0))



# priority queue
import heapq

print("HEAPQ")
q = []

heapq.heappush(q, 1)
heapq.heappush(q, 2)
heapq.heappush(q, 3)
heapq.heappush(q, 0)
heapq.heappush(q, -1)


while q:
    print(heapq.heappop(q))