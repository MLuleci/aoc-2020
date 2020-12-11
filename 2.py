f = open('data/2.txt')
lines = f.readlines()

count = 0
for x in lines:
    rule,pswd = x.split(':')
    minc,maxc = rule.split('-')
    ch = maxc[-1]
    maxc = int(maxc[0:-1])
    minc = int(minc)
    A = pswd[minc] == ch
    B = pswd[maxc] == ch
    if A ^ B:
        count = count + 1
print(count)
