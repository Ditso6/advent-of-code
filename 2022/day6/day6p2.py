# read input
file = open("stream.txt", "r")

stream = file.readline().rstrip()

position = 0
for i in range(0, len(stream)-14, 1):
    if len(set(stream[i:i+14])) == 14:
        position = i+14
        break
    else:
        None

print(position)
