def inc_cycle(cycle, reg, cycles):
  cycle += 1
  res = 0
  if cycle in cycles:
    res = cycle*reg
    #print(f"CYCLE {cycle}",res)
  return cycle, res


with open('day10/input.txt', 'r') as f:
  data = f.read().splitlines()


reg = 1
cycle = 1
signals = 0
cycles = [20,60,100,140,180,220]

for inst in data:
  if 'noop' in inst:
    cycle, res = inc_cycle(cycle, reg, cycles)
    signals += res
    continue
  else:
    x = int(inst.split()[1])
    cycle, res = inc_cycle(cycle, reg, cycles)
    signals += res
    reg += x
    cycle, res = inc_cycle(cycle, reg, cycles)
    signals += res

print(signals)