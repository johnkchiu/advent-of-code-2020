from itertools import combinations

lines = open('input','r').read().splitlines()
vals = list(map(int, lines))

# 2 combinations, sum, find 2020
combs = list(combinations(vals, 2))
sums = list(map(sum, combs))
for index, value in enumerate(sums):
  if value == 2020:
    print('Combination: {}.  Product: {}'.format(combs[index], combs[index][0] * combs[index][1]))


# 3 combinations, sum, find 2020
combs = list(combinations(vals, 3))
sums = list(map(sum, combs))
for index, value in enumerate(sums):
  if value == 2020:
    print('Combination: {}.  Product: {}'.format(combs[index], combs[index][0] * combs[index][1] * combs[index][2]))

