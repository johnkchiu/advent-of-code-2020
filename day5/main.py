
def find_row(ticket, min, max):
  # print(f"ticket: {ticket}, min: {min}, max: {max}")
  if ticket == '': return min

  if ticket[:1] == 'F':
    max = min + int((max - min) / 2)
  else:
    min = max - int((max - min) / 2)
  return find_row(ticket[1:], min, max)

def find_col(ticket, min, max):
  # print(f"ticket: {ticket}, min: {min}, max: {max}")
  if ticket == '': return min

  if ticket[:1] == 'L':
    max = min + int((max - min) / 2)
  else:
    min = max - int((max - min) / 2)
  return find_col(ticket[1:], min, max)


max = 0
seats = {}
with open('input', 'r') as file:
  for line in file:
    row = find_row(line.strip()[:7], 0, 127)
    col = find_col(line.strip()[-3:], 0, 7)
    seat = row * 8 + col
    if seat > max: max = seat
    seats[seat] = True
    print(f"ticket: {line.strip()}, row: {row}, col: {col}, seat: {seat}")

print(max)

for i in range(0, max):
  if i in seats:
    print('X ', end='')
  else:
    print(f"{i} ", end='')
  if i % 4 == 0:
    print(' ', end='')
  if i % 8 == 0:
    print('')

