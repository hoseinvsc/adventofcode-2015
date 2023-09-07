# https://adventofcode.com/2015/day/1
# my input must be read from input.txt 
file = open("problem1/d.txt","r")
read_file= file.read()

balance = 0
for char in read_file:
    if char == "(":
        balance = balance + 1
    elif char == ")":
        balance = balance - 1

print(balance)
