import numpy as np

with open('day8/input.txt', 'r') as f:
    data = np.array([list(map(int, x)) for x in f.read().splitlines()])

res = 0
dim = len(data)
for x, y in np.ndindex(data[:dim, :dim].shape):
    e = data[x, y]
    if np.all(e > data[x+1:, y]) or np.all(e > data[x][y+1:]) \
            or np.all(e > data[:x, y]) or np.all(e > data[x][:y]):
        res += 1

print(res)
