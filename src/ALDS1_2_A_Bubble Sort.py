
_ = input()
a = list(map(int, input().split()))

def bubble_sort(a):
    count = 0
    length = len(a)
    for i in range(length - 1):
        for j in range((length - i) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
    return a, count

sorted_a, count = bubble_sort(a)
print(*sorted_a)
print(count)
