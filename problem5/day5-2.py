def twice(s):
    for i in range(len(s) - 1):
        # print (i)
        p = s[i]+s[i+1]
        if s.count(p) >= 2:
            # print (i)
            return True
    return False

def between(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False


with open("problem5/day5.txt", "r") as file:
    lines = file.readlines()
    nice_count = 0
    
    for line in lines:
        line = line.strip()
        s = line
        if twice(s) and between(s):
            nice_count += 1

print (nice_count)