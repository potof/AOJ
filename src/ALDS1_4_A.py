
n = input()
list_s = list(map(int, input().split()))
q = input()
list_t = list(map(int, input().split()))

ans = 0
for i in list(set(list_t)):
    for j in list(set(list_s)):
        if i == j:
            ans += 1
            continue

print(ans)
