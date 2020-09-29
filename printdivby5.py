def finddivby5(numlist) :
    print("given list is ", numlist)
    print("divisble by 5 nos are :")
    l=len(numlist)
    for x in range(l):
        if (numlist[x] % 5 == 0):
             print(numlist[x])
    # for x in numlist:
    #   if (x % == 0):
    #.      print(x)

givlist = [100,200,250,35,60,56,75,33,55] 
finddivby5(givlist)

   """ Given a list of numbers, Iterate it and print only those numbers which are divisible of 5 """
