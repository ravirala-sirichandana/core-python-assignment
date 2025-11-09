prices = eval(input("Enter your cart_items  as {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500} : "))
def total_amount (prices):
    if len(prices)==0 :
        return 'YOUR CART IS EMPTY'
    else:
        total=sum(prices.values())
        if len(prices)>5:
            total *= 0.9
        return f'TOTAL PRICE OF YOUR ITEMS IS : {total}'
print(total_amount(prices))     