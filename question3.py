#write a program to find the factorial of a number
num = int(input())
ans = 1
for i in range(num + 1):
    ans *= i
print(ans)