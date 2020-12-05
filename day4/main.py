import os

# with open("input", 'r') as file:
#     data = file.read()
#     print(data)
#     splitted = data.split(os.linesep + os.linesep)

splitted = open('input').read().strip().split('\n\n')
   
reqs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def find_valid(splitted,reqs):
    valid = 0
    for passport in splitted:
        if all(req in passport for req in reqs):
            valid += 1
    return valid

print(find_valid(splitted,reqs))

