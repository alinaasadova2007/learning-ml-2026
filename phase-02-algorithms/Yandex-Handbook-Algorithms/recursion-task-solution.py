# k = 0
# result = []


# def hanoi_towers(n, from_peg, to_peg):
#     global k
#     global result
#     if n == 1:
#         k += 1
#         result.append([from_peg, to_peg])
#         return from_peg, to_peg
#     k += 1
#     unused_peg = 6 - from_peg - to_peg
#     hanoi_towers(n-1, from_peg, unused_peg)
#     result.append([from_peg, to_peg])
#     hanoi_towers(n-1, unused_peg, to_peg)


# n = int(input())
# hanoi_towers(n, 1, 3)
# print(k)
# for res in result:
#     print(' '.join(map(str, res)))


# n = int(input())

# f = [0] * (n + 1)

# f[1] = 1

# for i in range(2, n + 1):
#     min_moves = 10 ** 18
#     for k in range(1, i):
#         moves = 2 * f[k] + (2 ** (i - k)) - 1
#         if moves < min_moves:
#             min_moves = moves

#     f[i] = min_moves

# print(f[n])

# def code(a, b, k):
#     m = 10 ** k
#     if b == 0:
#         return 1 % m
#     t = code(a, b // 2, k)
#     t = (t * t) % m
#     if b % 2 != 0:
#         t = (t * a) % m
#     return t


# a, b, k = map(int, input().split())

# result = code(a, b, k)
# print(str(result).zfill(k))


# n, k = map(int, input().split())
# result = []


# def num(number):
#     if len(number) == n:
#         result.append(number)
#         return

#     if len(number) == 0:
#         for i in range(1, 10):
#             num(str(i))

#     else:
#         last = int(number[-1])
#         for i in range(10):
#             if abs(last - i) == k:
#                 num(number + str(i))


# num('')
# for res in sorted(result):
#     print(res)


# n = int(input())


# def recursive_sum(remaining, max_allowed, terms):
#     if remaining == 0:
#         print('+'.join(terms))
#         return

#     for x in range(min(max_allowed, remaining), 0, -1):
#         terms.append(str(x))
#         recursive_sum(remaining - x, x, terms)
#         terms.pop()


# recursive_sum(n, n, [])
