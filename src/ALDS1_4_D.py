import math
from sys import stdin

n, k = map(int, stdin.readline().split())

baggages = [int(stdin.readline()) for _ in range(n)]

def get_baggae_num(baggages, weight, truck_num):
    trucks = [0 for _ in range(truck_num)]
    truck_num = 0
    count = 0
    for index, item in enumerate(baggages):
        trucks[truck_num] += item

        if trucks[truck_num] > weight:
            break

        if index != n-1 and trucks[truck_num] + baggages[index+1] > weight:
            if truck_num < k-1:
                truck_num += 1
            else:
                break
        count += 1
    return count


max_wight = 0
left = 0
right = n * 10000
mid = (left + right) // 2
while left <= right:
    baggage_num = get_baggae_num(baggages, mid, k)
    if baggage_num == n:
        max_wight = mid
        right = mid - 1
    else:
        left = mid + 1
    mid = (left + right) // 2

print(max_wight)
