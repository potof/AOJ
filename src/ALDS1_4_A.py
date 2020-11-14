
n = input()
list_s = list(set(input().split()))
q = input()
list_t = list(set(input().split()))

ans = 0
for t in list_t:
    if list_s.count(t) > 0:
        ans += 1

print(ans)
