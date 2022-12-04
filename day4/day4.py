

with open('day4/input.txt', 'r') as f:
  data = [[tuple(int(z) for z in y.split('-')) for y in x.split(',')] for x in f.read().split('\n')]

#print(data[:5])

overlap = 0
overlap2 = 0
for d in data:
  lower = min(d[0][0], d[1][0])
  upper = max(d[0][1], d[1][1])
  # print(d)
  # print(f"Lower {lower} Upper {upper}")
  if (lower in d[0] and upper in d[0]) or (lower in d[1] and upper in d[1]):
    #print("OVERLAP:",d)
    overlap += 1
  if (d[0][0] <= d[1][0] and d[0][1] >= d[1][0]) or (d[1][0] <= d[0][0] and d[1][1] >= d[0][0]):
    print("OVERLAP:",d)
    overlap2 += 1
  #print('--------')
print(overlap)
print(overlap2)