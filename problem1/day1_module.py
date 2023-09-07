def check_balance(file):
    balance = 0
    for char in file:
        if char == "(":
            balance = balance + 1
        elif char == ")":
            balance = balance - 1
    return balance


file = "(()"
print(check_balance(file))