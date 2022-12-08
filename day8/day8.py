import numpy as np


def score(arr):
    # print(arr)
    if len(arr) <= 1:
        #print("cant see shit")
        return 1
    s = 0
    my_tree = arr[0]
    for a in arr[1:]:
        s += 1
        if a >= my_tree:
            break
    #print("I see ", s)
    return s


def total_score(x, y, data):
    s = 1
    # print("DOWN")
    s *= score(data[x:, y])
    # print("RIGHT")
    s *= score(data[x][y:])
    # print("UP")
    s *= score(np.flip(data[:x+1, y]))
    # print("LEFT")
    s *= score(np.flip(data[x][:y+1]))
    return s


with open('day8/input.txt', 'r') as f:
    data = np.array([list(map(int, x)) for x in f.read().splitlines()])

res = 0
dim = len(data)
for x, y in np.ndindex(data[:dim, :dim].shape):
    e = data[x, y]
    if np.all(e > data[x+1:, y]) or np.all(e > data[x][y+1:]) \
            or np.all(e > data[:x, y]) or np.all(e > data[x][:y]):
        res += 1

# print(res)

# 2
m = 0
for x, y in np.ndindex(data.shape):
    s = total_score(x, y, data)
    m = max(m, s)

print(m)
