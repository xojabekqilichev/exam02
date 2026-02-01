def calculate_tax(salary: int) -> dict:
    result = {}
    if salary <= 5000000:
        tax_percent = 0
    elif salary <= 10000000:
        tax_percent = 12
    elif salary <= 20000000:
        tax_percent = 18
    else:
        tax_percent = 25
    tax_amount = salary * (tax_percent / 100)
    net_salary = salary - tax_amount 
    result['gross'] = salary         
    result['tax_percent'] = tax_percent 
    result['tax_amount'] = tax_amount   
    result['net'] = net_salary        
    return result
salary = int(input('Oylikni kiriting: '))
hisobot = calculate_tax(salary)

print(hisobot)