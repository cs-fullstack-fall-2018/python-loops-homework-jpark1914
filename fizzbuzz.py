

yourNum = int(input("What is your number?"))
my_file = open("fizzbuzz.txt", "w+")

for num in range(0, yourNum):
    if(num%3 == 0 and num%5 == 0):
        my_file.write(str(num) + "\n")
        print(str(num),"FizzBuzz")

    elif(num%5 == 0):
        print(str(num), "Buzz")

    elif(num%3 == 0):
        print(str(num), "Fizz")
    else:
        print("meh")