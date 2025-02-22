num = int(input("enter the given number :"))

isPrime = True

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            isPrime = False
            break
print("the given number is prime",isPrime)