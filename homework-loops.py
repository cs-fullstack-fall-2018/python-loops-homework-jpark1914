# #Exercise 1
#
# for x in range(-20,50):
#     print(x)
#
# #Exercise 2
#
# for x in range(0,21,2):
#     print(x)

#Exercise 3
#
# numbers = [34, 23, 546, 1]
# totalSum= 0
# for x in numbers:
#     totalSum += x
# print(totalSum)

#Exercise 4


# for x in range(0,100):
#     if(x%4 == 0):
#         print(x)
#

# Extra-ish Credit
originalPassword = input("What is your password?")
passwordToCheck = input("Confirm Password")


while( passwordToCheck != originalPassword or passwordToCheck == "q"):
    passwordToCheck = input( "What is your password? Or press 'q' to quit")

