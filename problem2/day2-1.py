from day2_module import calc_gift

file = open("problem2/day2.txt","r")

sum=0
for i in range(0,1000):
    line = file.readline()
    l2 = line.strip()
    result = calc_gift (l2)
    sum = result + sum
    print (i,l2,result,sum)