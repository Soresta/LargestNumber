# Largest number:
# The program that finds the largest of 50 numbers entered from the keyboard.
# Klavyeden girilen 50 tane sayıdan en büyük olanı bulan program.

firstNum = int(input("Enter a number: "))
largest = firstNum
for i in range(9):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num

print(largest)
