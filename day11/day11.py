class Monke():
  def __init__(self, id, items, op, test, throw_to) -> None:
    self.id = id
    self.items = items
    self.op = op
    self.test = test
    self.throw_to = throw_to
    self.inspect_count = 0

  def inspect(self, old):
    res = eval(self.op) % BASE
    log(f"Monkey inspects item with level {old}")
    log(f"Multiplied to {res}")
    self.inspect_count += 1
    return res

  def do_test(self, x):
    return x % self.test == 0

  def monke_throw(self, i):
    if self.do_test(i):
      log(f"{i} is divisible by {self.test}")
      log(f"Throwing item with worry level {i} to monkey {self.throw_to[0]}")
      return i, self.throw_to[0]
    else:
      log(f"{i} is NOT divisible by {self.test}")
      log(f"Throwing item with worry level {i} to monkey {self.throw_to[1]}")
      return i, self.throw_to[1]

  def turn(self):
    throws = []
    for i in self.items:
      log(i)
      i = self.inspect(i)
      #i = i // 3
      log(f"Monke is bored, current level is {i}")
      what, who = self.monke_throw(i)
      throws.append((what,who))
      log(f"Monkey items: {self.items}, throws: {throws}")
    return throws


def load_monkes(data):
  monkes = []
  id = 0
  for d in data:
    m = d.splitlines()[1:]
    items = list(map(int, m[0].split(':')[1].strip().split(',')))
    op = m[1].split('=')[1].strip()
    test = int(m[2].split()[-1])
    throw_to = [int(m[3].split()[-1]), int(m[4].split()[-1])]
    monkes.append(Monke(id, items, op, test, throw_to))
    id += 1
  return monkes


def round(monkes):
  for m in monkes:
    log(f"Monkey {m.id}")
    throws = m.turn()
    for t in throws:
      monkes[t[1]].items.append(t[0])
    m.items = []
    log()

def log(s=''):
  if DEBUG:
    print(s)



with open('day11/input.txt', 'r') as f:
  data = f.read().split('\n\n')

DEBUG = False

monkes = load_monkes(data)
n = 10000
BASE = 1
for m in monkes:
  BASE *= m.test

for i in range(n):
  round(monkes)

counts = []
for m in monkes:
  counts.append(m.inspect_count)
  print(m.id, ': ', m.inspect_count)
counts.sort()
print(counts[-1] * counts[-2])



