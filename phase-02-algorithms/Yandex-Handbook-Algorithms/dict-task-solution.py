# dictionary = {}
# q = int(input())
# q_list = []
# for _ in range(q):
#     q_list.append(list(map(int, input().split())))

# result = []
# for i in q_list:
#     if i[0] == 1:
#         dictionary[i[1]] = i[2]

#     elif i[0] == 2:
#         result.append(dictionary.get(i[1], -1))

# for res in result:
#     print(res)


# n = int(input())
# a = list(map(int, input().split()))

# frequency = {}

# for x in a:
#     if x in frequency:
#         frequency[x] += 1
#     else:
#         frequency[x] = 1

# max_value = -1
# result = min(a)
# for f in frequency.keys():
#     if frequency[f] > max_value:
#         max_value = frequency[f]
#         result = f
#     elif frequency[f] == max_value:
#         result = min(result, f)

# print(result)


# from fractions import Fraction


# n = int(input())
# fracts = []
# frequency = {}
# for _ in range(n):
#     num, den = map(int, input().split())
#     fract = Fraction(num, den)
#     fracts.append(fract)
#     if fract in frequency:
#         frequency[fract] += 1
#     else:
#         frequency[fract] = 1

# result = Fraction(1, 100000)
# max_value = -1
# for f in frequency.keys():
#     if frequency[f] > max_value:
#         max_value = frequency[f]
#         result = f
#     elif frequency[f] == max_value:
#         result = min(result, f)

# print(result.numerator, result.denominator)


# n = int(input())
# a = sorted(list(map(int, input().split())))

# frequency = {}
# for f in a:
#     if f in frequency:
#         frequency[f] += 1
#     else:
#         frequency[f] = 1

# max_values = list(frequency.items())
# max_values.sort(key=lambda x: (-x[1], x[0]))
# result = sorted([x[0] for x in max_values[:3]])
# print(' '.join(map(str, result)))


# def pattern(word):
#     patterns = []
#     for i in range(len(word)):
#         patterns.append(word[:i] + '*' + word[i + 1:])

#     return patterns


# n = int(input())
# pattern_count = {}
# word_count = {}
# answer = 0

# for _ in range(n):
#     word = input()
#     patterns = pattern(word)
#     l = len(patterns)
#     new_pairs = 0
#     for pat in patterns:
#         new_pairs += pattern_count.get(pat, 0)
#     new_pairs -= word_count.get(word, 0) * l
#     answer += new_pairs
#     for pat in patterns:
#         if pat in pattern_count:
#             pattern_count[pat] += 1
#         else:
#             pattern_count[pat] = 1
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(answer)
