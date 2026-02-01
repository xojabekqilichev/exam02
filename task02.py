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
    