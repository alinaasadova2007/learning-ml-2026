# from collections import deque


# q = int(input())
# d = deque()
# result = []

# for _ in range(q):
#     data = list(map(int, input().split()))
#     command = data[0]
#     if command == 1:
#         d.append(data[1])
#         result.append(d[-1])
#     elif command == 2:
#         d.pop()
#         if not d:
#             result.append(-1)
#         else:
#             result.append(d[-1])

# for res in result:
#     print(res)


# from collections import deque
# n = int(input())
# a = list(map(int, input().split()))

# stack = deque()
# answer = []
# for x in a:
#     visible = 0
#     hidden = 0
#     while stack and stack[-1][0] < x:
#         visible += stack[-1][1] + 1
#         hidden += stack[-1][1] + 1
#         stack.pop()

#     if stack and stack[-1][0] == x:
#         stack[-1][1] += hidden + 1

#     else:
#         stack.append([x, hidden])

#     answer.append(visible)

# print(' '.join(map(str, answer)))


# from collections import deque


# n = int(input())
# k = int(input())
# a = list(map(int, input().split()))
# total = 0
# stack = deque()

# for i in range(n):
#     if stack and stack[0] <= i - k:
#         stack.popleft()
#     while stack and a[stack[-1]] >= a[i]:
#         stack.pop()
#     stack.append(i)
#     if i >= k - 1:
#         total += a[stack[0]]

# print(total)


# from collections import deque


# s = list(input())

# open_s = ['(', '{', '[']
# close_s = [')', '}', ']']
# stack = deque()
# solution = True
# for simbol in s:
#     if simbol in open_s:
#         stack.append(simbol)
#     elif simbol in close_s:
#         if stack and close_s.index(simbol) == open_s.index(stack[-1]):
#             stack.pop()
#         else:
#             solution = False
#             break

# if solution:
#     print('YES')
# else:
#     print('NO')


# from collections import deque


# n = int(input())
# a = list(map(int, input().split()))

# d = deque()
# start = 0
# answer = 0

# for i in range(n):
#     if a[i] % 2 != 0:
#         d.append(i)
#     else:
#         if not d:
#             start = i + 1
#         else:
#             d.pop()
#             if not d:
#                 answer = max(answer, i - start + 1)
#             else:
#                 answer = max(answer, i - d[-1])

# print(answer)
