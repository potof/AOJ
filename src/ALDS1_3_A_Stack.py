
ans = []
for s in input().split():
    if s in ["+", "-", "*"]:
        v2 = ans.pop()
        v1 = ans.pop()
        ans.append(str(eval(v1 + s + v2)))
    else:
        ans.append(s)
print(*ans)