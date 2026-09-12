# import heapq


# q = int(input())
# queue = []
# result = []

# for _ in range(q):
#     data = list(map(int, input().split()))
#     command = data[0]
#     if command == 1:
#         heapq.heappush(queue, -1 * data[1])
#         result.append(-1 * queue[0])
#     elif command == 2:
#         if not queue:
#             result.append(-1)
#         else:
#             heapq.heappop(queue)
#             if not queue:
#                 result.append(-1)
#             else:
#                 result.append(-1 * queue[0])

# for res in result:
#     print(res)


# import heapq


# n = int(input())
# workers = [0, 0]
# heapq.heapify(workers)

# questions = []

# for _ in range(n):
#     d, w = map(int, input().split())
#     heapq.heappush(questions, (-1 * w, d))

# for _ in range(n):
#     w, time = heapq.heappop(questions)
#     start_time = heapq.heappop(workers)
#     t = start_time + time
#     heapq.heappush(workers, t)

# total = max(workers)
# print(total)


# import heapq


# n, k = map(int, input().split())
# a = [-1 * x for x in list(map(int, input().split()))]
# heapq.heapify(a)
# total = 0
# for i in range(k):
#     discount = -1 * heapq.heappop(a)
#     if total + discount > total:
#         total += discount

# print(total)


# import heapq


# n, k = map(int, input().split())
# places = [0] * k
# heapq.heapify(places)
# total = 0
# for _ in range(n):
#     a, b = map(int, input().split())
#     if places[0] <= a:
#         heapq.heappop(places)
#         total += 1
#         heapq.heappush(places, b)

# print(total)


# import heapq


# n, m = map(int, input().split())

# notifications = []
# for _ in range(n):
#     idi, p, s = map(int, input().split())
#     heapq.heappush(notifications, (s, idi, p))

# for _ in range(m):
#     s, idi, p = heapq.heappop(notifications)
#     print(idi)
#     heapq.heappush(notifications, (s + p, idi, p))
