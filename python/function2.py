# sum sabhi values ko sum karne ke liye

def sum_num(*number):
    total = sum(number)
    return total
result = sum_num(10,20,30,40,50)
print("Total sum is:-",result)

"""
output:

Total sum is:- 150
"""


# even , odd number niklne ke liye 

def odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"
rb = odd(8)
print(rb)

"""

output: 

8 is even
"""

# max sabse badi value nikalne ke liye

def find(number):
    max_num = max(number)
    return f"Maximum number is : {max_num}"
result = find([3,8,12,90,50])
print(result)
"""
output:

Maximum number is : 90

"""


# min list me se sabse chhoti value nikalne ke liye

def find(number):
    max_num = min(number)
    return f"Maximum number is : {max_num}"
result = find([3,8,12,90,50])
print(result)

"""
output

Maximum number is : 3
"""



#lis ko sorted karne ke liye

def find(number):
    max_num = sorted(number)
    return f"Maximum number is : {max_num}"
result = find([3,8,12,90,50])
print(result)

"""
output:

 number is : [3, 8, 12, 50, 90]

 """

 

# number*2 list ko 2 bar repeat karne ke liye 

def find(number):
    max_num = (number*2)
    return f"Maximum number is : {max_num}"
result = find([3,8,12,90,50])
print(result)

"""
output

 number is : [3, 8, 12, 90, 50, 3, 8, 12, 90, 50]
"""
