# task was to create a median function without using any inbuilt function.

import numpy

# Taking input of the numbers from CMD Terminal

number_array = list()
number = input("Enter the number of elements you want:")
print ('Enter numbers in array: ')
for i in range(int(number)):
    n = input("number :")
    number_array.append(int(n))
    number_array.sort()
print ('ARRAY: ',number_array)

#Creating a function for Median

def median():
    l = number_array
    num = len(l)
    l.sort()
    if num % 2 == 0:
        m = (l[int((num/2)-1)] + l[int((num/2))])/2
    else:
        m = l[int((num/2))]
    return m
print('Median of the above array is: ', median())
