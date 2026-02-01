def calculate_cart(cart: dict) -> int:
    total = sum(map(lambda x: x['price']*x['quantity'], cart.values()))
    return total
cart = {
    'non': {'price': 3000, 'quantity': 2},
    'sut': {'price': 8000, 'quantity': 1},
    'olma': {'price': 5000, 'quantity': 5}
}

print(calculate_cart(cart))  # 37000