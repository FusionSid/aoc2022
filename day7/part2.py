with open("input.txt") as f:
    terminal_output = f.read().strip().split("\n")[1:]


class File:
    def __init__(self, file_data: str) -> None:
        _data = file_data.split(" ")

        self.size = int(_data[0])
        self.name = _data[1]

    def __repr__(self):
        return f"{self.name} ({self.size})"


class Directory:
    def __init__(self, name: str, parent) -> None:
        self.name = name
        self.parent = parent
        self.children: list[Directory | File] = []

    # for visualisation purposes
    def __repr__(self):
        return f"{self.name}: [{', '.join(repr(i) for i in self.children)}]"


def get_dir_size(_dir: Directory):
    total = 0
    for i in _dir.children:
        if isinstance(i, File):
            total += i.size
            continue
        total += get_dir_size(i)

    return total


def find_directories(_dir: Directory):
    global min_dirsize, options  # uhh globals bad code shh
    for child in _dir.children:
        if isinstance(child, Directory):
            dirsize = get_dir_size(child)
            if dirsize >= min_dirsize:
                options.append(dirsize)
            find_directories(child)


current = root = Directory("/", None)

for line in terminal_output:
    if line.startswith("$"):
        if line[2] == "c":
            dirname = line.split("cd ")[1]
            if dirname == "..":
                current = current.parent
            for _dir in current.children:
                if isinstance(_dir, Directory) and _dir.name == dirname:
                    current = _dir
        continue

    if line.startswith("d"):
        current.children.append(Directory(line.split(" ")[1], current))
        continue
    current.children.append(File(line))

min_dirsize = 30000000 - (70000000 - get_dir_size(root))
print("Minimum Directory Size Needed:", min_dirsize)

options = []  # shit code ngl
find_directories(root)
print(f"Answer:", min(options))
