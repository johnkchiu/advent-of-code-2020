
valid = 0

with open('input', 'r') as file:
  has_fields, fields = {}, []

  for line in file:
    if line == '\n':
      # # init map
      # has_fields = { 'byr':False, 'iyr':False, 'eyr':False, 'hgt':False, 'hcl':False, 'ecl':False, 'pid':False, 'cid':False}
      # # update fields provided
      # for field in fields:
      #   has_fields[field[0]] = True
      # # check all provide fields
      # if all((val == True or key == 'cid') for key, val in has_fields.items()):
      #   # print(fields)
      #   valid += 1
      # else:
      #

      if len(fields) == 8: valid += 1
      if len(fields) == 7 and all(field[0] != 'cid' for field in fields): valid += 1

      print(f"Fields[{len(fields)}]: {fields}")

      fields = []
    else:
      fields = fields + [x.split(':') for x in line.strip().split(' ')]

print(valid)

