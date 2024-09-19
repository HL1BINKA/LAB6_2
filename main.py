def average():
    A = list(map(int,input('Enter a list: ').split()))
    sum_of_neg=0
    count_of_neg=0
    print(A)
    for x in A:
        if x<0:
            sum_of_neg+=x
            count_of_neg+=1
    if count_of_neg>0:
        avr=sum_of_neg/count_of_neg
        print('Average is:', avr)
    else:
        print("No negative values")
        avr=0
    return avr
average()