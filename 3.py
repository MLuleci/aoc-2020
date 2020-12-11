with open('data/3.txt') as f:
    lines = f.read().split('\n')
    lines = lines[:-1]
    dys = [1, 1, 1, 1, 2]
    dxs = [1, 3, 5, 7, 1]
    prod = 1
    for i in range(len(dxs)):
        dx = dxs[i]
        dy = dys[i]
        x = dx
        y = dy
        count = 0
        while y < len(lines):
            if lines[y][x] == '#':
                count = count + 1
            y = y + dy
            x = (x + dx) % len(lines[0])
        prod = prod * count
    print(prod)
