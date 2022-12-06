with open("input.txt") as f:
    datastream = f.read()

for char in range(4, len(datastream)):
    if len(set(datastream[char - 4 : char])) == 4:
        print(char)
        break
