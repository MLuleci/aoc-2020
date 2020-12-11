import re
with open('data/4.txt') as f:
    passports = f.read().split('\n\n')
    passports[-1] = passports[-1][:-1]
    ref = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
    count = 0
    for i in passports:
        pairs = {}
        for j in i.split('\n'):
            for k in j.split(' '):
                l = k.split(':');
                key = l[0]
                val = l[1]
                pairs[key] = val
        got = set(pairs.keys())
        if ref.issubset(got):
            if not re.match('^\d{4}$',pairs['byr']) or not int(pairs['byr']) in range(1920,2003):
                continue

            if not re.match('^\d{4}$',pairs['iyr']) or not int(pairs['iyr']) in range(2010,2021):
                continue

            if not re.match('^\d{4}$',pairs['eyr']) or not int(pairs['eyr']) in range(2020,2031):
                continue
            
            if not re.match('^\d+(in|cm)$',pairs['hgt']):
                continue
            unit = pairs['hgt'][-2:]
            n = int(pairs['hgt'][:-2])
            if unit == 'cm' and not n in range(150,194):
                continue
            if unit == 'in' and not n in range(59,77):
                continue
            
            if not re.match('^#[a-f0-9]{6}$',pairs['hcl']):
                continue
            
            if not re.match('^(amb|blu|brn|gry|grn|hzl|oth)$',pairs['ecl']):
                continue
            
            if not re.match('^\d{9}$',pairs['pid']):
                continue
            count = count + 1
    print(count)
