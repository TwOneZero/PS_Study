
import heapq as hq
import sys

pq = []

for _ in range(int(input())) :
  x = int(sys.stdin.readline())
  if x:
    #튜플로 저장
    hq.heappush(pq, (abs(x), x))
  # x = 0
  else: 
    if pq :
      print(hq.heappop(pq)[1])
    else:
      print(0)
