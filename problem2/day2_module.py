def calc_gift(dimention):
    a = dimention.split('x')
    l = int(a[0])
    w = int(a[1])
    h = int(a[2])

    s1 = l*w
    s2 = h*w
    s3 = l*h

    list = [s1,s2,s3]
    min_area = min(list)

    area = 2*l*w + 2*w*h + 2*h*l
    result = min_area + area
    return result


def calculator_rebbon(dimention):
    g = dimention.split('x')

    a = int(g[0])
    b = int(g[1])
    c = int(g[2])
    lst = [a,b,c]
    lst.sort()

    min1 = lst[0]
    min2 = lst[1]
    rebbon_lan = min1*2 + min2*2
    hajm = a * b * c
    result = hajm + rebbon_lan
    return result



