
# example:
#    1-3 a: abcde
#    1-3 b: cdefg
#    2-9 c: ccccccccc

# part 1
count = 0
with open('input', 'r') as f:
  for line in f:
    policy, password = line.rstrip().split(':')
    appear, letter = policy.split(' ')
    min, max = list(map(int, appear.split('-')))

    if password.count(letter) >= min and password.count(letter) <= max:
      count += 1

  print(count)

# part 2
count = 0
with open('input', 'r') as f:
  for line in f:
    policy, password = line.rstrip().split(':')
    appear, letter = policy.split(' ')
    pos1, pos2 = list(map(int, appear.split('-')))

    if password[pos1] == letter and password[pos2] != letter:
      # print(pos1, pos2, letter, password, password[pos1], password[pos2])
      count += 1

    if password[pos1] != letter and password[pos2] == letter:
      # print(pos1, pos2, letter, password, password[pos1], password[pos2])
      count += 1

  print(count)

