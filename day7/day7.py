
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


with open('day7/input.txt', 'r') as f:
    data = f.read().splitlines()

root = Dir('/', None)
cwd = root

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
        i += 1

# prt_dir(root)
print(total_size(root))
