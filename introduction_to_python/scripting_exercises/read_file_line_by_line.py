lines = []
with open("text.txt") as f:
    for line in f:
        lines.append(line.strip())

print(lines)
