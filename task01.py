def calculate(num1: float, num2: float, operator: str) -> float:
    if operator not in ['+', '-', '*', '/']:
        return "Error: Noto'g'ri operator"
    if num2 == 0:
        return "Error: Nolga bo'lish mumkin emas"
    
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
        
    
    return round(float(result), 2)
