def inc_cycle(cycle, reg):
  draw(reg, cycle)
  cycle += 1
  res = 0
  return cycle, res

def show_sprite(reg, cycle):
  print(f"CYCLE {cycle}")
  print("SPRITE POSITION:")
  for i in range(40):
    if i % 40 in range(reg - 1, reg + 2):  
      print('#', end='')  
    else:
      print('.', end='')
  print('\n-------------------------------------')

def draw(reg, cycle):
  #show_sprite(reg, cycle)
  if (cycle % 40) in range(reg-1, reg+2):
    print('#', end='')
  else:
    print('.', end='')

  if (cycle % 40)  == 0:
    print()

with open('day10/input2.txt', 'r') as f:
  data = f.read().splitlines()

reg = 1
cycle = 1
signals = 0

for inst in data:
  if 'noop' in inst:
    cycle, res = inc_cycle(cycle, reg)
    signals += res
    continue
  else:
    x = int(inst.split()[1])
    cycle, res = inc_cycle(cycle, reg)
    signals += res
    reg += x
    cycle, res = inc_cycle(cycle, reg)
    signals += res

print(cycle)
#print('\n',signals)