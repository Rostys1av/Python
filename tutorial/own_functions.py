#Functions with no parameters
# functions use input(parameters) and output(return)

# def no_parameter():
#     return  2 * 2
#
# #Call the no parameter function(use it)
# print(no_parameter())
# print("------------------")

#function with multipul parameters

def mul_param(num1,num2,num3):
    """
    Calculates 3 int mutiplied by themselves
    :param num1: int
    :param num2: int
    :param num3: int
    :return: Value of the three
    """
    return num1 + num2 + num3

#print(mul_param(2,2,2,))

#print("------------------")

#Reuse code

def prime_num(num):
    """
    Calculates the prime number
    :param num: int
    :return: True or False
    """
    count = 2
    while count < num -1:
        if num % count == 0:
            return False
        count = count + 1
    return True
print(prime_num(10))

'''
num = 10
count =2 
while 2 < 10 -1:
        if 20 % 2 == 0:
            return False
        count = count + 1
    return True
'''