import numpy as np
from collections import deque
import sys

DEBUG = False
row_dirs = [-1, 1, 0, 0]
col_dirs = [0, 0, 1, -1]

shortPath = sys.maxsize
path = 0
found = False
steps = []


def log(s=''):
    if DEBUG:
        print(s)


def visit(curr, data, visited, end):
    global shortPath, path, found
    log(f"Visiting position {curr[0]}, {curr[1]} with value {data[curr]}")
    if curr[0] == end[0] and curr[1] == end[1]:
        found = True
        shortPath = min(path, shortPath)
        return

    visited[curr] = True
    path += 1

    for i in range(4):
        nxt = (curr[0] + row_dirs[i], curr[1] + col_dirs[i])
        if nxt[0] < 0 or nxt[1] < 0:
            continue
        if nxt[0] >= data.shape[0] or nxt[1] >= data.shape[1]:
            continue
        if visited[nxt]:
            continue
        if data[nxt] > (data[curr] + 1):
            continue
        visit(nxt, data, visited, end)
    visited[curr] = False
    path -= 1
    log(visited)


if __name__ == "__main__":
    with open('day12/input.txt', 'r') as f:
        data = np.array([list(map(ord, x)) for x in f.read().splitlines()])

    # Find Start and End
    start = np.where(data == ord('S'))
    end = np.where(data == ord('E'))

    # Set elevation for S and E
    data[start] = ord('a')
    data[end] = ord('z')
    # Normalize to 0,1,2...
    data -= 97
    log(f"START {start}")
    log(f"END {end}")

    visit(start, data, np.zeros(data.shape, dtype=bool), end)
    print(shortPath)
