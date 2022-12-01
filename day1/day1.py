
with open('day1\input.txt', 'r') as f:
  # 1
  elf_loads = [sum([int(y) for y in x.split('\n') if len(y)]) for x in f.read().split('\n\n')]
  print(max(elf_loads))

  # 2
  elf_loads.sort(reverse=True)
  print(sum(elf_loads[:3]))
