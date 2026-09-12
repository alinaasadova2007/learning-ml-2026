# my_set = set()
# q = int(input())
# result = []
# for _ in range(q):
#     action, x = map(int, input().split())
#     if action == 1:
#         my_set.add(x)
#     elif action == 2:
#         if x in my_set:
#             result += [1]
#         else:
#             result += [0]

# for i in result:
#     print(i)

# n = int(input())
# result = set()
# for _ in range(n):
#     data = list(map(int, input().split()))
#     result.update(data[1:])

# print(len(result))

# n = int(input())
# result = set(list(map(int, input().split()))[1:])
# for _ in range(n-1):
#     result &= set(list(map(int, input().split()))[1:])

# print(len(result))

# n = int(input())
# frequency = {}
# sets = []
# solution = True
# for _ in range(n):
#     data = list(map(int, input().split()))
#     for i in data[1:]:
#         if i in frequency:
#             frequency[i] += 1
#         else:
#             frequency[i] = 1
#     sets.append(set(data[1:]))

# for value in frequency.values():
#     if value != 1 and value != n:
#         solution = False

# if not solution:
#     print('NO')
# else:
#     p = []
#     c = len([x for x in frequency if frequency[x] == n])
#     for s in sets:
#         p.append(len([x for x in s if frequency[x] == 1]))
#     print('YES')
#     print(c)
#     print(' '.join(map(str, p)))


# n = int(input())
# a = list(map(int, input().split()))
# prev = set()
# all_values = set()

# for x in a:
#     current = set()
#     current.add(x)
#     for p in prev:
#         current.add(p | x)
#     all_values.update(current)
#     prev = current

# print(len(all_values))
