
# Load and normalize data
with open('day2/input.txt', 'r') as f:
    data = [[ord(y)-64 for y in x.split(' ')]
            for x in f.read().split('\n')]

for x in data:
    x[1] -= 23

# 1
score = 0
for g in data:
    score += (((g[1] - g[0])+1) % 3) * 3 + g[1]

print(score)


# 2
s = 0
for g in data:
    # game points
    s += (g[1] - 1) * 3
    # symbol used
    s += ((g[0] + g[1]) % 3) + 1

print(s)
