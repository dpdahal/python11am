print("================Location=============")
print("1. Kalanki 2. Buspark 3. Balaju ")
current = int(input("Enter your current: "))
price = 0
discount_price = 0
if current == 1:
    destination = int(input("Enter your destination: "))
    if destination == 2:
        student = input("Are you a student? (y/n): ")
        if student == "y":
            discount_price = 15 * 0.10
            price += 15 - discount_price
        else:
            price += 15
    elif destination == 3:
        price += 30
    elif current == destination:
        price += 75

print("Your price is: ", price)
print("Your discount price is: ", discount_price)
