file = open("problem1/day1.txt","r")
read_file= file.read()

balance = 0
counter = 0
for char in read_file:
    counter = counter+1
    print(char,counter,balance)

    if char == "(":
        balance = balance + 1
    elif char == ")":
        balance = balance - 1

    if balance == -1:
        print("*************")
        break

print(balance)
print(counter)