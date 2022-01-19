def find_multiples():
    numSum = 0
    numList = []
    for num in range(0,1000):
        if num % 3 == 0 or num % 5 == 0:
            numSum += num
            numList.append(num)
    return numSum, numList

number_sum, number_list = find_multiples()
print("The sum of the {nlist} numbers is {nsum}".format(nlist=number_list.__len__(), nsum=number_sum))
           
