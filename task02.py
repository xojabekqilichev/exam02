def atm_operation(balance: int, action: str, amount: int) -> int:
    if action == 'withdraw':
        if balance < amount:
            print("ERROR")
        else:
            return balance - amount
    elif action == 'deposit':
        return balance + amount
    else:
        return balace
    def atm_operation(balance: int, action: str, amount: int):
    if amount < 0:
        return "Error: Summa manfiy bo'lishi mumkin emas"
    if action == "deposit":
        balance += amount
        return balance
    elif action == "withdraw":
        if amount > balance:
            return "Error: Mablag' yetarli emas"
        balance -= amount
        return balance
    else:
        return "Error: Noto'g'ri operatsiya turi"


print(atm_operation(100000, "deposit", 50000))  
print(atm_operation(100000, "withdraw", 20000)) 
print(atm_operation(100000, "withdraw", 150000))
print(atm_operation(100000, "deposit", -5000)) 