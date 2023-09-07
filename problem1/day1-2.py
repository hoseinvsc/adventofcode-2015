from day1_module import balance_founder

file = open("problem1/day1.txt","r")
read_file= file.read()

print(balance_founder(read_file))