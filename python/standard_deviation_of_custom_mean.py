





def standard_deviation(list_, value_): # value_ is custom mean of list_
    sum_squares = 0
    for x in range(0,len(list_)):
        sum_squares += (value_ - list_[x])**2
    return (sum_squares/(len(list_)-1))**.5




