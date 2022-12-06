with open("input.txt") as f:
    datastream = f.read()

for char in range(14, len(datastream)):
    if len(set(datastream[char - 14 : char])) == 14:
        print(char)
        break
