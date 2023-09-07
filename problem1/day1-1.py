# https://adventofcode.com/2015/day/1

file = open("problem1/day1.txt","r")
read_file= file.read()

def check_balance(read_file):
    balance = 0
    for char in read_file:
        if char == "(":
            balance = balance + 1
        elif char == ")":
            balance = balance - 1
    return balance

print(check_balance(read_file))