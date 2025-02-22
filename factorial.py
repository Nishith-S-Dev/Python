# factorial of the given number 

# problem statement is that find the factorial of the num using the while loop

number = int(input("enter the factorial of number "))
factorial = 1;
while number>0:
    factorial *=number
    number -=1
print("the factorial of the given number is :",factorial)