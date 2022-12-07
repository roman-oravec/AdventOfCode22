
class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def add_child(self, ch):
        self.children.append(Dir(ch.split()[1], self))

    def add_file(self, f):
        self.files.append(f.split())

    def get_size(self):
        return sum([int(x[0]) for x in self.files])


def prt_dir(d):
    if d.children == []:
        return
    print('DIR:', d.name, ':\n', end='\t')
    for c in d.children:
        print(c.name, end=', ')
    print()
    for c in d.children:
        prt_dir(c)


def total_size(d):
    subs = 0
    for s in d.children:
        subs += total_size(s)
    return subs + d.get_size()


def partOne(dirs):
    res = 0
    for d in dirs:
        ts = total_size(d)
        #print(d.name, ts)
        if ts <= 100000:
            res += ts
    return res


def partTwo(dirs, root):
    res = total_size(root)
    full = 70000000
    free = full - res
    needed = 30000000
    for d in dirs:
        ts = total_size(d)
        # print(ts)
        if (free + ts) > needed and ts < res:
            res = ts
    return res


with open('day7/input.txt', 'r') as f:
    data = f.read().splitlines()

root = Dir('/', None)
cwd = root

dirs = set()
dirs.add(root)
i = 1
while i < len(data):
    line = data[i]
    # print(line)
    if '$ ls' in line:
        i += 1
        line = data[i]
        while line[0] != '$':
            # File
            if line.split()[0].isnumeric():
                cwd.add_file(line)
            # Dir
            else:
                cwd.add_child(line)
            i += 1
            if i < len(data):
                line = data[i]
            else:
                break
    if '$ cd' in line:
        d = line.split()[-1]
        if d == '..':
            cwd = cwd.parent
        else:
            next = [x for x in cwd.children if x.name == d][0]
            cwd = next
        dirs.add(cwd)
        i += 1

# prt_dir(root)
# print(total_size(root))
print("Part 1:", partOne(dirs))
print("Part 2:", partTwo(dirs, root))
