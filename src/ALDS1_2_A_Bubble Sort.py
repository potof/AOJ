
n = int(input())
a = list(map(int, input().split()))

def bubble_sort(a, n):
    flag = True
    count = 0
    while flag:
        flag = False
        for i in range(n-1, 0, -1):
            if a[i] < a[i-1]:
                tmp = a[i]
                a[i] = a[i-1]
                a[i-1] = tmp
                flag = True
                count += 1
    return a, count

sorted_a, count = bubble_sort(a, n)
print(*sorted_a)
print(count)
