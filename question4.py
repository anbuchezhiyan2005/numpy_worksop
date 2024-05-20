#write a program to find the sum of digits of a given number'
num = input()
ans = 0
for i in num:
    ans += int(i)
print(ans)