
lines = open('input','r').read().splitlines()

def slope(right, down):
  x,y  = 0, 0
  count = 0
  for index, line in enumerate(lines):
    # skip if not inc by down
    if index%down != 0:
      print(line)
      continue

    # loop back around
    if (x > len(line)-1):
      x = x - len(line)

    # print(x, y)
    if line[x] == '#':
      count += 1
      print(line[:x] + 'X' + line[x + 1:])
    else:
      print(line[:x] + 'O' + line[x + 1:])

    x = x + right
    y = index

  return count

# part 1
print(slope(3,1))

# part 2
print(slope(1,1))
print(slope(3,1))
print(slope(5,1))
print(slope(7,1))
print(slope(1,2))

print(slope(1,1) * slope(3,1) * slope(5,1) * slope(7,1) * slope(1,2))
