def sumprev(z):
    y = range(z)
    for x in y:
        c=x+x-1
        if x == 0:
            print("the Answer is as follows")
        else:
            print ("the sum of Current Number and ",x,"the previous number ",x-1,"is", c)

sumprev(5)
