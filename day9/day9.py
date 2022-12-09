import numpy as np


def move_tail(h,t, tail_history, tail):
  for i in range(len(h)):
    # Same pos or adjacent
    if abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1])  <= 1:
      #print("NOT MOVING")
      break
    # Same row or col
    if h[abs(i-1)] == t[abs(i-1)]:
      if h[i] > t[i]:
        #print(f"MOVING tail[{i}] + 1")
        t[i] += 1
      if h[i] < t[i]:
        #print(f"MOVING tail[{i}] + 1")
        t[i] -= 1
    else:
      if h[0] > t[0]:
        #print(f"MOVING tail[{i}] + 1")
        t[0] += 1
      if h[0] < t[0]:
        #print(f"MOVING tail[{i}] + 1")
        t[i] -= 1
      if h[1] > t[1]:
        #print(f"MOVING tail[{i}] + 1")
        t[1] += 1
      if h[1] < t[1]:
        #print(f"MOVING tail[{i}] + 1")
        t[1] -= 1
      break
  if tail:
    tail_history.add(tuple(t))
  ##print(tail_history)
  return t

def print_board(knots):
  return
  print('==================')
  for x in range(20):
    for y in range(20):
      try:
        idx = knots.index([x,y])
        print(idx, end='')
      except:
        print('.', end='') 
      # else:
      #   print('.', end='') 
    print()

def move(d, l, tail_history, knots):
  for i in range(l):
    if d == 'L':
      knots[0][1] -= 1
    if d == 'R':
      knots[0][1] += 1
    if d == 'U':
      knots[0][0] += 1
    if d == 'D':
      knots[0][0] -= 1

    for i in range(len(knots) - 1):
      tail = False
      if i+1 == 9:
        tail = True
      knots[i+1] = move_tail(knots[i],knots[i+1], tail_history, tail)
  print_board(knots)
  return

with open('day9/input.txt', 'r') as f:
  data = [x.split() for x in f.read().splitlines()]
  data = [[x[0], int(x[1])] for x in data]

n = 10
knots = [[0,0] for i in range(n)]

tail_history = set()
tail_history.add(tuple([0,0]))
for m in data:
  move(m[0], m[1], tail_history, knots)

print(len(tail_history))

