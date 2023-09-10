# https://adventofcode.com/2015/day/1
from day1_module import check_balance

file = open("problem1/day1.txt","r")
read_file= file.read()

print(check_balance(read_file))