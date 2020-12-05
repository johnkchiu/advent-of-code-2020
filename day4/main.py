
from os import replace


valid = 0

# part 1
with open('input', 'r') as file:
  # read whole file and split
  for line in file.read().split('\n\n'):
    # remove trailing \n, join lines, split by ' ', and then split by ':'
    fields = [x.split(':') for x in line.strip().replace('\n', ' ').split(' ')]

    if len(fields) == 8: valid += 1
    if len(fields) == 7 and all(field[0] != 'cid' for field in fields): valid += 1

    print(f"Fields[{len(fields)}]: {fields}")

print(valid)
