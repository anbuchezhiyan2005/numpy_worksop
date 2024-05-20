# find if the given number is a palindrome or not?
num = input()
if num == num[::-1]:
    print("palindrome")
else:
    print("Not palindrome")