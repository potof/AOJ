from collections import deque
word = input()

area_list = []  # / に対応する \ の index とその時の面積
que = deque([]) # \ の index を入れていく

for i in range(len(word)):
    if word[i] == "\\":
        que.append(i)
    elif word[i] == "/":
        if len(que) > 0:
            from_i = que.pop()
            area = i - from_i
            while len(area_list) > 0 and area_list[-1][0] > from_i:
                area += area_list[-1][1]
                area_list.pop(-1)
            area_list.append([from_i, area])


area_sum = list(i[1] for i in area_list)
print(sum(area_sum))
print(len(area_list), *area_sum)
