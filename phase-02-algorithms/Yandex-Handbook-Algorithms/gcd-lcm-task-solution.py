# def gcd(a, b):
#     if a == 0 or b == 0:
#         return max(a, b)
#     return gcd(b, a % b)


# a, b = map(int, input().split())
# print(gcd(a, b))


# def gcd(a, b):
#     if a == 0 or b == 0:
#         return max(a, b)
#     return gcd(b, a % b)


# a, b = map(int, input().split())
# lcm = a * b // gcd(a, b)
# print(lcm)


# def fibonacci(n):
#     table = [0, 1]

#     while table[-1] <= n:
#         table.append(table[-1] + table[-2])

#     if table[-1] <= n:
#         return table[-2], table[-1]

#     return table[-3], table[-2]


# n = int(input())
# a, b = fibonacci(n)
# print(a, b)


# from fractions import Fraction

# a, b = map(int, input().split())
# c, d = map(int, input().split())

# fract1 = Fraction(a, b)
# fract2 = Fraction(c, d)

# fract = fract1 + fract2

# print(fract.numerator, fract.denominator)


# def gcd(a, b):
#     if a == 0 or b == 0:
#         return max(a, b)
#     return gcd(b, a % b)


# a, b, c = map(int, input().split())
# if a == 0 or b == 0 or c == 0:
#     if a == 0 and b == 0 and c == 0:
#         print('YES')
#     else:
#         print('NO')
# if c % gcd(abs(a), abs(b)) == 0:
#     print('YES')
# else:
#     print('NO')
