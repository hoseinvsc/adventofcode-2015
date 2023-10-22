# Create a 1000x1000 grid of lights, initialized to False (off)
grid = [[False] * 1000 for _ in range(1000)]

# Define the function to apply the instructions
def apply_instruction(instruction, grid):
    parts = instruction.split()
    action = parts[0]
    
    if action == "toggle":
        x1, y1, x2, y2 = map(int, parts[1].split(',')), map(int, parts[3].split(','))
    else:
        x1, y1, x2, y2 = map(int, parts[2].split(',')), map(int, parts[4].split(','))
    
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if action == "toggle":
                grid[x][y] = not grid[x][y]
            elif action == "on":
                grid[x][y] = True
            elif action == "off":
                grid[x][y] = False

file = open("problem6/day6.txt","r")
instructions = file.read()
for line in instructions.splitlines():
    apply_instruction(line, grid)

# Count the number of lights that are turned on
count = sum(row.count(True) for row in grid)
print(count)