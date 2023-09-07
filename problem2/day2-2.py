from day2_module import calculator_rebbon
file = open("problem2/day2.txt","r")

sum=0
for i in range(0,1000):
    line = file.readline()
    l2 = line.strip()
    result = calculator_rebbon(l2)
    sum = result + sum
    print (i,l2,result,sum)