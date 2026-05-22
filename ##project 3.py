#project 3 coffee shop

menu = {'latte':5,
        'americano':3,
        'cappuccino':5,
        'espresso':4,
        }

for item  in menu:
    print(item,menu[item]) #menu,price

cups = []
orders = []
while True:
    order = input("menu?(done = end order)")
    if order  == "done":
        break
    orders.append(order)
    amount = int(input("How many cups")) 
    cups.append(amount) #add to list cups

def calculate_total(cups, order):
    total = 0
    for i in range(len(cups)):
        total += cups[i] * menu[orders[i]]
        return total

def apply_discount(total, total_cups):
    if total_cups >= 3:
        return total * 0.9 # sale 10%
    else:
        return total
    
def print_bill(total):
    print(f"Total price: {total} $")

total = calculate_total(cups, orders)
total_cups = sum(cups)
final_price = apply_discount(total,total_cups)
print_bill(final_price)