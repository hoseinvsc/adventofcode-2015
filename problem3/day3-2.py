def move(direction, position):
    x, y = position
    if direction == '^':
        return (x, y + 1)
    elif direction == 'v':
        return (x, y - 1)
    elif direction == '>':
        return (x + 1, y)
    elif direction == '<':
        return (x - 1, y)

def count_houses(directions):
    santa_position = (0, 0)
    robo_position = (0, 0)
    visited_houses = {(0, 0)}

    current_turn = 'santa'

    for direction in directions:
        if current_turn == 'santa':
            santa_position = move(direction, santa_position)
            visited_houses.add(santa_position)
            current_turn = 'robo'
        else:
            robo_position = move(direction, robo_position)
            visited_houses.add(robo_position)
            current_turn = 'santa'

    return len(visited_houses)

with open("problem3/day3.txt", "r") as file:
    directions = file.read()

houses = count_houses(directions)
print("Houses with presents:", houses)
