from pprint import pprint

with open('day5/input.txt', 'r') as f:
    data = f.read().split('\n\n')

crates = data[0]

moves = data[1].split('\n')
n = [int(x) for x in crates.split('\n')[-1].strip().split('  ')]
crates = crates.split('\n')[:-1]
cols = {}
for i in n:
    cols['col_%s' % i] = []

for row in range(len(crates) - 1, -1, -1):
    curr = crates[row]
    col_n = 1
    pos = 0
    while pos < len(curr):
        if curr[pos] == '[':
            cols['col_%s' % col_n].append(curr[pos+1])
        col_n += 1
        pos += 4
        continue
# 2 (#1 commit before)
moves = [[int(x) for x in y.split() if x.isdigit()] for y in moves]
for m in moves:
    src = cols['col_%s' % m[1]]
    dst = cols['col_%s' % m[2]]
    load = src[-m[0]:]
    # print(m)
    #print("LOAD", load)
    dst += load
    cols['col_%s' % m[1]] = cols['col_%s' % m[1]][:-m[0]]

for i in n:
    print(cols['col_%s' % i][-1], end='')
print()
