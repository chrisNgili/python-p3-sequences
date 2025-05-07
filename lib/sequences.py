#!/usr/bin/env python3

# def print_fibonacci(length):
#     calculated = []
#     if length == 0:
#         print(calculated)       
#     else:
#         a,b = 0, 1
#         while a <= length:
#             calculated.append(a)
#             a, b = b, a + b
#             print(calculated)
#     pass
# print(print_fibonacci(10))
# def print_fibonacci(length):
#     calculated = []
#     if length == 0:
#         print (calculated)
#     elif length == 1:
#         print([0])
#     elif length == 2 :
#         print([0,1])
#     else:
#         a,b = 0,1
#         for i in range(2,length):
#             calculated.append(a + b)
#             print(calculated)
#             a = b
#             b = calculated 
# print(print_fibonacci(10))

def print_fibonacci(length):
    calculated = []
    if length == 0:
        print(calculated)
    elif length == 1:
        print([0])
    elif length == 2 :
        print([0,1])    
    else:
        a,b = 0,1
        calculated.append(a)
        calculated.append(b)
        for i in range(2, length):
            sum = a + b
            a = b
            b = sum 
            calculated.append(sum)    
        print(calculated)
    pass        
print(print_fibonacci(10))