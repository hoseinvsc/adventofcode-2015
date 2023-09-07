#This is for part1
def check_balance(file):
    balance = 0
    for char in file:
        if char == "(":
            balance = balance + 1
        elif char == ")":
            balance = balance - 1
    return balance


#This is for part2
def balance_founder(file2):
    balance2 = 0
    counter = 0
    for char in file2:
        counter = counter+1
        print(char,counter,balance2)

        if char == "(":
            balance2 = balance2 + 1
        elif char == ")":
            balance2 = balance2 - 1

        if balance2 == -1:
            print("****************")
            return counter+1
            break