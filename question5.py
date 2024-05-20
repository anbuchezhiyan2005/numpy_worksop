#write a program to find if the given number is prime no or not
num = int(input())
if num % 2 == 0:
    print("Not prime Number")

else:
    flag = 0
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            flag = 1
    if flag == 1:
        print("Not prime number")
    else:
        print("Prime number")