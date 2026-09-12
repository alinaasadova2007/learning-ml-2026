# from collections import deque


# q = int(input())
# d = deque([])
# result = []

# for _ in range(q):
#     data = list(map(int, input().split()))
#     if data[0] == 1:
#         d.append(data[1])
#         result.append(d[0])
#     elif data[0] == 2:
#         if len(d) == 0:
#             result.append(-1)
#         else:
#             d.popleft()
#             if len(d) == 0:
#                 result.append(-1)
#             else:

#                 result.append(d[0])

# for res in result:
#     print(res)


# import sys

# read = sys.stdin.buffer.readline
# q = int(read())
# d = deque()
# result = []
# for _ in range(q):
#     data = list(map(int, read().split()))
#     command = data[0]
#     if command == 1:
#         d.appendleft(data[1])
#         result.append(f'{d[0]} {d[-1]}')

#     elif command == 2:
#         d.append(data[1])
#         result.append(f'{d[0]} {d[-1]}')

#     elif command == 3:
#         if not d:
#             result.append('-1')
#         else:
#             d.popleft()
#             if not d:
#                 result.append('-1')
#             else:
#                 result.append(f'{d[0]} {d[-1]}')
#     else:
#         if not d:
#             result.append('-1')
#         else:
#             d.pop()
#             if not d:
#                 result.append('-1')
#             else:
#                 result.append(f'{d[0]} {d[-1]}')

# sys.stdout.write('\n'.join(result))


# import sys
# import heapq

# read = sys.stdin.buffer.readline
# n, k = map(int, read().split())

# answer = []

# servers = [(0, i) for i in range(1, k + 1)]
# heapq.heapify(servers)

# for _ in range(n):
#     t, d = map(int, read().split())
#     ready_time, server_index = heapq.heappop(servers)
#     start = max(t, ready_time)
#     finish = start + d
#     answer.append(str(finish))
#     heapq.heappush(servers, (finish, server_index))

# sys.stdout.write(' '.join(answer))


# from collections import deque


# n = int(input())
# s = deque(input())

# result = ''

# while s:
#     if s[0] < s[-1] or s[0] == s[-1]:
#         result += s[0]
#         s.popleft()
#     elif s[0] > s[-1]:
#         result += s[-1]
#         s.pop()

# print(result)


# n = int(input())
# a = list(map(int, input().split()))
# if n == 1:
#     print(a[0])
# else:
#     left = [(i - 1) % n for i in range(n)]
#     right = [(i + 1) % n for i in range(n)]
#     alive = n
#     current = 0
#     last_leader = current
#     while alive > 2:
#         last_leader = current
#         l = left[current]
#         r = right[current]
#         candidates = [current, l, r]
#         weakest_index = min(candidates, key=lambda index: a[index])
#         strongest_index = max(candidates, key=lambda index: a[index])

#         l = left[weakest_index]
#         r = right[weakest_index]
#         right[l] = r
#         left[r] = l

#         alive -= 1
#         if alive > 2:
#             current = strongest_index
#         else:
#             if weakest_index == last_leader:
#                 last_leader = strongest_index

#     neighbour = right[last_leader]
#     print(a[last_leader], a[neighbour])
