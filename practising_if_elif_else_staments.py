a = [int(x) for x in input("Enter the value of x :").split()]
for i in a:
    if i>= 500 and i<=2050:
        print(i, " is in range")
    elif i==2007 or i==2020:
        print(i)
    else:
        print('empty')                        # [525  is in range, empty, 852  is in range, 2020  is in range, 562  is in range]


'''  errors handling practise session  in python'''

# print('python program')
# print('coding environment')
# try:
#     print('hello')                                             # SyntaxError
# try:
#     print('hello'+3)
# except:
#     print('you have not defined the name')
# print("Hello world!")
# print("Welcome!!")

''' We can keep only one final, else , try block in the code but, 
                                  we can keep multiple except blocks in it'''
# print('python program')                                        # python program
# print('coding environment')                                    # coding environment
# try:
#     print('hello')                                             # hello
#     print(a)
# except ZeroDivisionError:
#     print('you have not defined the name')
# except ValueError:
#     print("another method")
# except NameError:
#     print("I am a programmer")                                 # I am a programmer
# else:
#     print("name error")
# print("Hello world!")                                         # Hello world!
# print("Welcome!!")                                            # Welcome!!
