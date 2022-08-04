# N , L = map(int, input().split())
# coord = [False] * 1001
# count = 0


# for i in map(int, input().split()):
#   coord[i] = True

# point = 0
# while point < 1001:
#   if coord[point] :
#     count+=1
#     point+= L
#   else:
#     point +=1 

# print(count)

#!!!!!!만약 물새는 곳이 억단위 라면? 
# flag 를 써서 하는 것은 메모리, 시간 비효율적
# 원하는 곳만 저장해야한다. 


N , L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

spot = 0
count = 0
while spot < len(arr):
  # 간격이 테이프 길이보다 작을 동안 뛰어넘을 인덱스를 반영 
  idx = 0 
  diff = 0
  tmpArr = arr[spot:]
  while idx < len(tmpArr) - 1:
    if diff + tmpArr[idx + 1] -tmpArr[idx] < L:
      diff = diff + tmpArr[idx + 1] -tmpArr[idx]
      idx  += 1
    else:
      break
  spot = spot + idx + 1
  count += 1 

print(count)
    
