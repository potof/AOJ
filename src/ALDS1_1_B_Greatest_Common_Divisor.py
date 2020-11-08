
x, y = map(int, input().split())

# 愚直に作ってみる
# 大きい方から 1 ずつ減らしてチェックしていく
def gcd1(x, y):
    start = x
    if y > x:
        start = y

    while start > 0:
        if x % start == 0 and y % start == 0:
            return start
        start -= 1

# print(gcd1(x, y))

# ユークリッドの互除法
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

print(gcd(x, y))

# ライブラリを使う
def gcd2(a, b):
    import math
    return math.gcd(a, b)

# print(gcd2(x, y))
