from sys import stdin

n, k = map(int, stdin.readline().split())

baggages = [int(stdin.readline()) for _ in range(n)]
baggages.sort(reverse=True)

trucks = [0 for _ in range(k)]
truck_num = 0
turn = True
for index, baggage in enumerate(baggages):
    trucks[truck_num] += baggage
    if turn:
        if truck_num == k-1:
            turn = False
        elif index != n-1:
            tmp_truck = trucks[truck_num] + baggages[index + 1]
            next_truck = trucks[truck_num + 1]
            if tmp_truck > next_truck:
                truck_num += 1
    else:
        if truck_num == 0:
            turn = True
        elif index != n-1:
            tmp_truck = trucks[truck_num] + baggages[index + 1]
            next_truck = trucks[truck_num - 1]
            if tmp_truck > next_truck:
                truck_num -= 1

# print(trucks)
print(max(trucks))
