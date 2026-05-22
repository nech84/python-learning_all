#project2 price elec

price_per_unit = 4

unit = int(input("unit: "))

def calculate_price(unit):
    return unit * price_per_unit

def check_sale(unit):
    if unit > 100:
        return "sale 10%"
    else:
        return "no sale"
    
def print_bill(unit,price):
    print(f"used{unit}unit")
    print(f"total price {price} $")

price =  calculate_price(unit)
sale =  check_sale(unit)
print_bill(unit,price)
print(sale)

