# write a program to do airthmetical operation addition and division.

# addition
num1 = float(input("enter the first number for addition: "))
num2 = float(input("enter the second number for addition: "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")


# Division
num3 = float(input("Enter the diviend for division: "))
num4 = float(input("Enter the divisor for division: "))
if  num4 == 0:
    print("Error: Division By zero is not allowed.")
else:
    div_result = num3 / num4
    print(f"Division: {num3} / {num4} = {div_result}")
    