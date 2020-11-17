import math
from sys import stdin

n, k = map(int, stdin.readline().split())

baggages = [int(stdin.readline()) for _ in range(n)]

def get_baggae_num(baggages, weight, truck_num):
    # weight に対して詰める数の荷物数を返す（全部詰めるのであれば n になる）

    trucks = [0 for _ in range(truck_num)]
    truck_num = 0
    count = 0
    for index, item in enumerate(baggages):
        trucks[truck_num] += item

        # 1つの荷物で重さを超える場合は終わり
        if trucks[truck_num] > weight:
            break

        # 次の荷物を足し合わせて重さ以上だったら次のトラックへ
        if index != n-1 and trucks[truck_num] + baggages[index+1] > weight:
            if truck_num < k-1:
                truck_num += 1
            else:
                break
        count += 1
    return count


# 純粋に最低の重さを 0 から増やしていくと O(答えの重さn) になって間に合わない
# なので、答えの重さを調べるために二部探索をする
max_wight = 0
left = 0
right = n * 10000
mid = (left + right) // 2
while left <= right:
    baggage_num = get_baggae_num(baggages, mid, k)
    if baggage_num == n:
        # mid が正解のときに保管しておく必要があるのでここで代入する（-1されたら困る）
        max_wight = mid
        right = mid - 1
    else:
        left = mid + 1
    mid = (left + right) // 2

print(max_wight)
