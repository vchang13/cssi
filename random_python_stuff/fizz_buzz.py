"""My implementation of fizzbuzz."""

x = input('Number: ')

def fizzbuzz(number):
    """Prints out fizzbuzz
    Prints out fizz if a number is divisible by 3, buzz if its divisible by 5
    and fizzbuzz if its divisible by both 3 and 5.

    """
    if number % 3 == 0 and number % 5 == 0:
         print('fizzbuzz')
    elif number % 5 == 0:
        print('buzz')
    elif number % 3 == 0:
        print('fizz')
    else:
        print(number)

for num in range(0, x+1):
    fizzbuzz(num)




# def i_take_all_the_args(arg1, arg2, arg3, arg4):
#     print(arg1)
#     print(arg2 + arg3 + arg4)
#
# i_take_all_the_args('hi', 1, 2 ,3)
# i_take_all_the_args('hi', 'a', 'b', 'c')
# #i_take_all_the_args('hi', 1, 'a', 3) #will show error since cannot add string and int together
# i_take_all_the_args(arg4=3, arg3=2, arg2=1, arg1='hi')
# #i_take_all_the_args(100, arg1='hai', arg3=2, arg2=1) #wont work
#
# def print_person(first, last_name, middle_name=None):
#     """docstring for the function that tells others what it does
#     prints out person's name
#
#     Args:
#         first: (str) Person's first name
#         last_name: (str) This person's last name.
#         middle_name: (str) optional, person's middle_nameself.
#     Returns:
#         (str) The string of the person's name.
#     """
#     middle_name = middle_name or '' #means that this is optional
#     print('{f} {m} {l}'.format(
#     f=first, m=middle_name, l=last_name))
#
# print_person('Mary', 'Grace', middle_name = 'Sue')

"""
As done by Anna

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
         print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')

while True: #run forever until i say stop
    human_input = input('Let me check your fizzbuzziness or say "stop": ')
    if human_input == 'stop':
        break
    fizzbuzz(human_input)

As done by Nonso (one line)

def fizzbuzz(number):
    print( "{f}{b}".format(f = "fizz" if number % 3 == 0 else "", b = "buzz" if number % 5 == 0 else""))

"""
