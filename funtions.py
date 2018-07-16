# def helloWorld():
#     print("Hello")
#     print("this")
#     print("isn't")
#     print("Super")
#     print("Mario")
#     print("World")
#
# helloWorld()
#

#======Function Use======

# def numberLoop():
#     x =  0
#     while(x<3):
#         x +=1
#         print(x)
#
#
# x = 0
# while(x < 100):
#     x += 1
#     print(numberLoop())



#======Return Functions======
# def printKenn():
#     print("Kenn")
#
# def returnKenn():
#     print("return funtion")
#     return "Kenn"
# printKenn()
# returnKenn()

#=====Hello World======

# def helloWorld():
#     return "helloWorld"
# helloWorld()
#
# def arrayOfNames():
#     return ["Bob", "John", "Kenn", "Kevin"]
#
# print(arrayOfNames())

# def sumTwoNumbers(number1, number2):
#     return number1 + number2
#
# print(sumTwoNumbers(5,6))
# print(sumTwoNumbers(11,34))
# print(sumTwoNumbers(3,5))

# def sumTwoNumbers(name1, name2):
#     name1 = name1.upper()
#     name2 = name2.upper()
#     return (name1 + " " + name2)
#
# print(sumTwoNumbers("Kenn","Kevin"))


# def yourName():
#
#     return name
#
# name = input("What is your name?")
# print("Hello", yourName())

# def finalCount(yourNumber):
#
#     x = 0
#     while(x < yourNumber):
#         x += 1
#         print(x)
#
#
# yourNumber = int(input("Pick a number over 25?"))
# print(finalCount(yourNumber))


def inputCounter(num1):

    while(num1 <= num2):
        num1 += 1
        print(num1)



num1= int(input("What is your first number?"))
num2 = int(input("What is your second number?"))

print(inputCounter(num1))