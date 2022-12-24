with open('input.txt') as txt:
    commands = txt.read().splitlines()

class Directory:
    def __init__(self, name, parent):
        self.dirname = name
        self.size = -1
        self.subs = []
        self.parent = parent

    def get_size(self):
        tot_size = 0
        for sub in self.subs:
            if isinstance(sub, Directory):
                if sub.size > 0:
                    tot_size += sub.size
                else:
                    return -1
            else:
                tot_size += int(sub[0])
        
        self.size = tot_size
        return tot_size

    def find_sub(self, subname):
        for sub in self.subs:
            if isinstance(sub, Directory) and sub.dirname == subname:
                return sub
        return None

top = Directory('/', None)
curdir = top
idx = 1
s = 0
sizes = []
while idx < len(commands):
    c = commands[idx]
    if c == '$ ls':
        idx += 1
        while idx < len(commands) and commands[idx][0] != '$':
            sub_c = commands[idx]
            if sub_c[0].isalpha():
                sub = Directory(sub_c.split()[1], curdir)
            else:
                sub = sub_c.split()

            curdir.subs.append(sub)
            idx += 1
        
        # try to calculate and assign the size of the directory
        dir_size = curdir.get_size()
        sizes.append(dir_size)
        if dir_size <= 100_000:
            s += dir_size
    
    # '$ cd ..' command
    elif c.split()[2] == '..':
        # assign the curdir to be the current parent
        curdir = curdir.parent
        # try to calculate and assign the size of the directory
        dir_size = curdir.get_size()
        sizes.append(dir_size)
        if dir_size <= 100_000:
            s += dir_size
        idx += 1
    # '$ cd dirname' command
    else:
        # find the chosen directory in the list of subs of the curdir and make it the new curdir
        curdir = curdir.find_sub(c.split()[2])
        idx += 1

# go up the file tree calculating file sizes
while curdir:
    if curdir.size < 0: 
        dir_size = curdir.get_size()
        sizes.append(dir_size)
        if dir_size <= 100_000:
            s += dir_size
    curdir = curdir.parent

print(s)

# part 2

surplus_space = top.size - 40_000_000
last_size = -1
for idx, size in enumerate(sorted(sizes, reverse=True)):
    if size < surplus_space:
        print(last_size)
        break
    last_size = size