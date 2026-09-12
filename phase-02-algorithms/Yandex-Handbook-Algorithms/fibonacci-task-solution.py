# n = int(input())


# def fibonacci(n):
#     if n <= 1:
#         return n
#     previous = 0
#     current = 1
#     for i in range(n-1):
#         old_previous = previous
#         previous = current
#         current = old_previous + previous
#     return current


# print(fibonacci(n))


# def last_char(n):
#     if n <= 1:
#         return n
#     f = [0] * (n + 1)
#     f[0] = 0
#     f[1] = 1
#     for i in range(2, n + 1):
#         f[i] = (f[i - 1] + f[i - 2]) % 10
#     return f[i]


# n = int(input())
# print(last_char(n))


# def fibonacci(n):
#     if n <= 1:
#         return n
#     previous = 0
#     current = 1
#     for i in range(n-1):
#         old_previous = previous
#         previous = current
#         current = old_previous + previous
#     return current


# def pisano_period(m):
#     current = 0
#     next = 1
#     period = 0
#     while True:
#         old_next = next
#         next = (current + next) % m
#         current = old_next
#         period += 1
#         if current == 0 and next == 1:
#             return period


# def remainder(n, m):
#     period = pisano_period(m)
#     num = n % period
#     res = fibonacci(num) % m
#     return res


# n, m = map(int, input().split())
# print(remainder(n, m))


# def fibonacci(n):
#     if n <= 1:
#         return n
#     previous = 0
#     current = 1
#     for _ in range(n-1):
#         old_previous = previous
#         previous = current
#         current = old_previous + previous
#     return current


# def last_char_sum(n):
#     num = (n + 2) % 60
#     res = (fibonacci(num) - 1) % 10
#     return res


# n = int(input())

# print(last_char_sum(n))


# def fibonacci(n):
#     if n <= 1:
#         return n
#     previous = 0
#     current = 1
#     for _ in range(n - 1):
#         old_previous = previous
#         previous = current
#         current = old_previous + previous
#     return current


# def last_char_sum(n):
#     num = (n + 2) % 60
#     res = (fibonacci(num) - 1) % 10
#     return res


# def part_sum(n, m):
#     res = (last_char_sum(n) - last_char_sum(m - 1)) % 10
#     return res


# m, n = map(int, input().split())
# print(part_sum(n, m))


# def fibonacci(n):
#     table = [1, 2]
#     while table[-1] <= n:
#         table.append(table[-1] + table[-2])
#     if table[-1] > n:
#         table.pop()
#     return table


# n = int(input())
# table = fibonacci(n)
# kanon = [0] * len(table)

# total = n
# for i in range(len(table)-1, -1, -1):
#     if total >= table[i]:
#         total -= table[i]
#         kanon[i] = 1


# last_one = len(kanon) - 1
# for i in range(len(kanon) - 1, -1, -1):
#     if kanon[i] == 1:
#         last_one = i
#         break

# print(''.join(map(str, kanon[last_one::-1])))
