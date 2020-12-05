import re
passports = open('input').read().strip().split('\n\n')

fields = {
    'byr': lambda x: 2002 >= int(x) >= 1920,
    'iyr': lambda x: 2020 >= int(x) >= 2010,
    'eyr': lambda x: 2030 >= int(x) >= 2020,
    'hgt': lambda x: (x[-2:] == 'cm' and 193 >= int(x[:-2]) >= 150) or (x[-2:] == 'in' and 76 >= int(x[:-2]) >= 59),
    'hcl': lambda x: re.match('^#[a-f\d]{6}$', x) != None,
    'ecl': lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'],
    'pid': lambda x: len(x) == 9  and x.isdigit(),
}
p1 = p2 = 0
for passport in passports:
    parts = re.split('\s', passport)
    passport_dict = dict(part.split(':') for part in parts)
    if all(key in passport_dict for key in fields):
        p1 += 1
        if all(fields[key](passport_dict[key]) for key in fields):
            p2 += 1
print(p1, p2)