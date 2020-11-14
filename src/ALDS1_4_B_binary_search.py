

def binary_search(list, key):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        if key == list[mid]:
            return 1
        elif key < list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return 0


n = input()
list_s = list(set(map(int, input().split())))
list_s.sort()
q = input()
list_t = list(set(map(int, input().split())))

ans = 0
for key in list_t:
    ans += binary_search(list_s, key)

print(ans)
