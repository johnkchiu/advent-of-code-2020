import re

# part 1
valid = 0
with open('input', 'r') as file:
  # read whole file and split
  for line in file.read().split('\n\n'):
    # remove trailing \n, join lines, split by ' ', and then split by ':'
    fields = dict(x.split(':') for x in line.strip().replace('\n', ' ').split(' '))

    if len(fields) == 8: valid += 1
    if len(fields) == 7 and all(key != 'cid' for key in fields.keys()): valid += 1

    print(f"Fields[{len(fields)}]: {fields}")

print(valid)

# part 2
def validate(fields):
  byr = 1920 <= int(fields['byr']) <= 2002
  iyr = 2010 <= int(fields['iyr']) <= 2020
  eyr = 2020 <= int(fields['eyr']) <= 2030
  if 'cm' in fields['hgt']:
    hgt = 150 <= int(fields['hgt'][:-2]) <= 193
  elif 'in' in fields['hgt']:
    hgt = 59 <= int(fields['hgt'][:-2]) <= 76
  else:
    hgt = False
  hcl = True if re.match('^#[a-f0-9]{6}$', fields['hcl']) else False
  ecl = True if re.match('amb|blu|brn|gry|grn|hzl|oth', fields['ecl']) else False
  pid = True if re.match('^[0-9]{9}$', fields['pid']) else False

  if (byr and iyr and eyr and hgt and hcl and ecl and pid) == False:
    print(byr, iyr, eyr, hgt, hcl, ecl, pid, fields)
  return (byr and iyr and eyr and hgt and hcl and ecl and pid)

valid = 0
with open('input', 'r') as file:
  # read whole file and split
  for line in file.read().split('\n\n'):
    # remove trailing \n, join lines, split by ' ', and then split by ':'
    fields = dict(x.split(':') for x in line.strip().replace('\n', ' ').split(' '))

    if len(fields) == 8 and validate(fields):
      valid += 1
    # else:
    #   print(f"Invalid Fields[{len(fields)}]: {fields}")


    if len(fields) == 7 and all(key != 'cid' for key in fields.keys()) and validate(fields):
      valid += 1
    # else:
    #   print(f"Invalid Fields[{len(fields)}]: {fields}")

print(valid)
