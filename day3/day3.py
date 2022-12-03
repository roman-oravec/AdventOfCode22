

def prior(c):
  n = ord(c)
  if n <= 90:
    return n - 38
  else:
    return n - 96

def badge(rucksacks):
  #print(rucksacks)
  b = [i for i in set(rucksacks[0]) if (i in rucksacks[1] and i in rucksacks[2])]
  #print(b)
  return prior(b[0])


with open('day3/input.txt', 'r') as f:
  data = f.read().split()

# 1
res = 0
for r in data:
  a = r[slice(0, len(r)//2)]
  b = r[slice(len(r)//2, len(r))]
  # print(r, a, b)
  for c in a:
    if c in b:
      # print(prior(c))
      # print("Common:", c)
      res += prior(c)
      break

print(res)

print("--------------")
# 2
n = 3 
res2 = sum([badge(data[i:i+n]) for i in range(0, len(data)+1-n, n)])
print(res2)


