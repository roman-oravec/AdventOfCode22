import numpy as np
from collections import deque

DEBUG = True
row_dirs = [-1, 1, 0, 0]
col_dirs = [0, 0, 1, -1]


def log(s=''):
    if DEBUG:
        print(s)


def look_around(curr, data, visited, q):
    count = 0
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
        visited[nxt] = True
        q.append(nxt)
        count += 1
    return count


def bfs(data, start, end):
    nodes_left_in_layer = 1
    nodes_in_next_layer = 1
    move_count = 0
    fin = False
    # Helper queue
    q = []
    q.append(start)
    # Helper bool arr
    visited = np.zeros(data.shape, dtype=bool)

    visited[start] = True
    while len(q) > 0:
        log(f"Moves: {move_count}")
        curr = q.pop()
        log("Curr" + str(curr))
        if curr == end:
            fin = True
            break
        nodes_in_next_layer += look_around(curr, data, visited, q)
        log(f"After looking around {q}")
        nodes_left_in_layer -= 1
        log(f"Left in layer {nodes_left_in_layer}")
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if fin:
        return move_count
    return -1


if __name__ == "__main__":
    with open('day12/input2.txt', 'r') as f:
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

    print(bfs(data, start, end))
