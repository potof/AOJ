import sys
from collections import deque

n = int(input())
ans = deque([])

for i in range(n):
    l = list(sys.stdin.readline().split())

    if l[0] == "insert":
        ans.appendleft(l[1])
    elif l[0] == "delete":
        try:
            ans.remove(l[1])
        except:
            pass
    elif l[0] == "deleteFirst":
        ans.popleft()
    elif l[0] == "deleteLast":
        ans.pop()
print(*ans)
