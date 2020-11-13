from collections import deque

n , time = map(int, input().split())
l = [list(input().split()) for _ in range(n)]
proc_que = deque(l)

duration_time = 0

while proc_que:
    duration_time += time
    proc = proc_que.popleft()
    if int(proc[1]) <= time:
        duration_time -= time - int(proc[1])
        print(proc[0], duration_time)
    else:
        proc_que.append([proc[0], int(proc[1])-time])
