def calculate(num1: float, num2: float, operator: str) -> float:
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        if num2 == 0:
            print("Error")
        else:
            result = num1/num2
    else:
        print("Invalid opertor.")
    return round(result, 2)


operator = input('Operator:')
num = float(input('Num:'))
num2 = float(input('Num:'))
result = calculate(num1= num, num2=num2, operator=operator)
print(result)
