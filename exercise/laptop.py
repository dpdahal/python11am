print("================Computer Bazar=========")
print("1. Dell(Rs:20000) 2.Toshiba(Rs:30000) 3.Mac(Rs:50000)")
option = int(input("Enter your option:"))
dell_price = 0
toshiba_price = 0
mac_price = 0
delivery_price = 0
plastic_price = 0
bag_price = 0
git_box_price = 0
location_price = 0
tax_amount = 0

if option == 1:
    quantity = int(input("Enter quantity:"))
    dell_price = quantity * 20000
elif option == 2:
    quantity = int(input("Enter quantity:"))
    toshiba_price = quantity * 30000
elif option == 3:
    quantity = int(input("Enter quantity:"))
    mac_price = quantity * 50000
else:
    print("Invalid option")
    exit()

print("1.Home(Rs:1000) 2. Pickup(Free)")
delivery_option = int(input("Enter delivery option:"))
if delivery_option == 1:
    delivery_price = 1000

print("1. Plastic(Rs:500) 2. Bag(Rs:1000) 3.Gift Box(Rs:5000) 4.None")
packing_option = int(input("Enter packing option:"))
if packing_option == 1:
    plastic_price = 500
elif packing_option == 2:
    bag_price = 1000
elif packing_option == 3:
    git_box_price = 5000

total = dell_price + toshiba_price + mac_price
print("1. Kathmandu(Rs:13% tax) 2. BTK (Rs:Free) 3. LTP(Rs Free)")
location_option = int(input("Enter location option:"))
if location_option == 1:
    tax_amount = total * 0.13

grand_total = total + delivery_price + plastic_price + bag_price + git_box_price + tax_amount
print("============= Bill===============")
print("Total:", total)
print("Tax:", tax_amount)
print("Grand Total:", grand_total)
