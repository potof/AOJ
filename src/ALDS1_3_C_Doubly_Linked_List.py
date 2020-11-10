
n = int(input())
ans = []

for i in range(n):
    l = list(input().split())

    if l[0] == "insert":
        ans.insert(0, l[1])
    elif l[0] == "delete" and l[1] in ans:
        del ans[ans.index(l[1])]
    elif l[0] == "deleteFirst":
        del ans[0]
    elif l[0] == "deleteLast":
        del ans[-1]
print(*ans)
