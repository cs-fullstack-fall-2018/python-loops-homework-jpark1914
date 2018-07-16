# import os
# os system("clear")


my_file = open("fives.txt", "w+")

for num in range(0, 101):
    if (num % 5 == 0):
        my_file.write(str(num) + "\n")
    else:
        print("not divisible by 5: ", num)
