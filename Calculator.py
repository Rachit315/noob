
num1 = int(input("Enter your first No:"))
num2 = int(input("Enter your second No:"))

sign = (input("Enter Operation you want to perform:"))


if sign == "+":
   print(num1, "+", num2, "=",num1+num2)
   
elif sign == "-":
 print(num1, "-", num2, "=",num1-num2)

elif sign == "*":
 print(num1, "X", num2, "=",num1*num2)

elif sign == "//":
 print(num1, "/", num2, "=",num1//num2)



else:
 print('Error: Please a mathematical symbol')

