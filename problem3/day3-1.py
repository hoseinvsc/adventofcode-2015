file = open("problem3/day3.txt","r")
input_puzzle = file.read()

x, y = 0, 0
visited_houses = {(x, y)}

for move in input_puzzle:
    if move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    elif move == '>':
        x += 1
    elif move == '<':
        x -= 1
    visited_houses.add((x, y))

print(len(visited_houses))