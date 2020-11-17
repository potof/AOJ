import math
from sys import stdin

n, k = map(int, stdin.readline().split())

baggages = [int(stdin.readline()) for _ in range(n)]

trucks = [0 for _ in range(k)]
truck_num = 0
search_flg = True

max_baggage = math.ceil(sum(baggages) / k)

while search_flg:

    # 荷物を足し合わせる
    for index, item in enumerate(baggages):
        trucks[truck_num] += item
        if index != n-1 and trucks[truck_num] + baggages[index+1] > max_baggage:
            if truck_num < k-1:
                truck_num += 1
            else:
                truck_num = 0
                trucks = [0 for _ in range(k)]
                max_baggage += 1
                search_flg = True
                break
        search_flg = False

# print(trucks)
print(max(trucks))
