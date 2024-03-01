def calculation(x,y,operator):
  if operator == '+':
    total = x + y
    return total
  elif operator == '-':
    total = x-y
    return total
  elif operator == '*':
    total = x * y
    return total
  elif operator =='/':
    total = x / y
    return total
  

num1 = float(input("Please enter number: "))
num2 = float(input("Please enter number: "))

ops = ['+', '-', '*', '/']
while True:
operator = input("Enter the math symbol you would like to use")
if operator not in ops:
  print("Please selects math sysmbol only from '+, -, *, /'")
  continue
else:
  print("Calculating")
  break
calc = calculation(num1, num2, operator)

print(calc)