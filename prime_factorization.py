from math import sqrt
while True:
    n  = int(raw_input("num: "))
    div = 2
    factors = []

    f = False
    while not f:
        if n % div == 0:
            n = n / div
            factors.append(str(div))
            div = 1
        if n == 1:

            f = True
            
        else:
            div += 1
            

    my_dict = {i:factors.count(i) for i in factors}
    print my_dict   
