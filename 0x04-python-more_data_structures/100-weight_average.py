#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numerator = [i[0] * i[1] for i in my_list]
        denominator = [i[1] for i in my_list]
        return sum(numerator)/sum(denominator)
    else:
        return 0
