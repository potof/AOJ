from sys import stdin

n = int(stdin.readline())

list = [None for _ in range(n)]

for i in range(n):
    command, item = stdin.readline().split()

    if command == "find":
        if item in list:
            print("yes")
        else:
            print("no")
    else:
        list[i] = item