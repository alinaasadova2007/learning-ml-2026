# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add(self, index, data):
#         new_node = Node(data)
#         if index == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return

#         current = self.head
#         current_index = 0

#         while current is not None and current_index < index - 1:
#             current = current.next
#             current_index += 1

#         if current is None:
#             raise IndexError('Индекс вне диапазона списка')

#         new_node.next = current.next
#         current.next = new_node

#     def find(self, index):
#         current = self.head
#         current_index = 0

#         while current is not None and current_index < index - 1:
#             current = current.next
#             current_index += 1

#         if current is None:
#             raise IndexError('Индекс вне диапазона списка')

#         return current.data

#     def remove(self, index):
#         if self.head is None:
#             raise IndexError('Список пуст')

#         if index == 1:
#             self.head = self.head.next
#             return

#         current = self.head
#         for _ in range(index - 2):
#             if current.next is None:
#                 raise IndexError('Индекс вне диапазона списка')
#             current = current.next

#         if current.next is None:
#             raise IndexError('Индекс вне диапазона')

#         current.next = current.next.next


# my_list = LinkedList()
# q = int(input())
# result = []
# for _ in range(q):
#     action = list(map(int, input().split()))
#     if action[0] == 1:
#         my_list.add(action[1], action[2])
#     elif action[0] == 2:
#         result.append((my_list.find(action[1])))
#     elif action[0] == 3:
#         my_list.remove(action[1])

# for i in result:
#     print(i)

# n = int(input())
# a = list(map(int, input().split()))

# max_diff = float('-inf')
# min_diff = float('inf')
# max_index = 0
# min_index = 0
# min_pair = []
# max_pair = []

# for j in range(1, n):
#     diff = a[min_index] - a[j]
#     pair = [min_index, j]
#     if diff < min_diff:
#         min_diff = diff
#         min_pair = pair
#     if a[j] < a[min_index]:
#         min_index = j

#     diff = a[max_index] - a[j]
#     pair = [max_index, j]
#     if diff > max_diff:
#         max_diff = diff
#         max_pair = pair
#     if a[j] > a[max_index]:
#         max_index = j

# print(' '.join(map(str, [x + 1 for x in min_pair])))
# print(' '.join(map(str, [x + 1 for x in max_pair])))


# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# q_list = []
# for _ in range(q):
#     q_list.append(int(input()))

# index_dict = {}
# for i in range(n):
#     if a[i] not in index_dict:
#         index_dict[a[i]] = i + 1

# for p in q_list:
#     print(index_dict.get(p, -1))


# n = int(input())
# a = list(map(int, input().split()))
# min_value = float('inf')
# result = []
# for i in a:
#     if i < min_value:
#         min_value = i
#         result.append(i)
#     else:
#         result.append(int(min_value))

# print(' '.join(map(str, result)))

# n = int(input())
# a = list(map(int, input().split()))
# k = n
# result = [a[0]]
# for i in range(1, n-1):
#     value = a[i]
#     if a[i-1] > value and value < a[i + 1]:
#         k -= 1
#     else:
#         result.append(value)
# result.append(a[-1])

# print(k)
# print(' '.join(map(str, result)))


# n = int(input())
# a = list(map(int, input().split()))
# max_value = 0
# max_index = -1
# for i in range(n):
#     if a[i] >= max_value:
#         max_value = a[i]
#         max_index = i
# del a[max_index]

# print(' '.join(map(str, a)))
