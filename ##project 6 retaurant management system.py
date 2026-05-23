##project 6 retaurant  management system 

menu = {
    "Burger": 150,
    "Pizza": 250,
    "Pasta": 180,
    "Steak": 450,
    "Salad": 120,
    "Soup": 90,
    "Sushi": 320,
    "Ramen": 200,
}

orders = [
    {"customer": "Alice", "items": ["Burger", "Pizza"], "quantity": [2, 1]},
    {"customer": "Bob", "items": ["Steak", "Soup"], "quantity": [1, 2]},
    {"customer": "Charlie", "items": ["Sushi", "Salad"], "quantity": [3, 1]},
    {"customer": "Diana", "items": ["Ramen", "Burger"], "quantity": [2, 2]},
    {"customer": "Eve", "items": ["Pizza", "Pasta"], "quantity": [2, 1]},
    {"customer": "Frank", "items": ["Steak", "Sushi"], "quantity": [2, 1]},
    {"customer": "Grace", "items": ["Soup", "Salad"], "quantity": [3, 2]},
    {"customer": "Henry", "items": ["Ramen", "Pizza"], "quantity": [1, 2]},
]

for item, price in menu.items():
    print(item,price,"$")

#order >500
filtered = list(filter(lambda x: sum(menu[item] * qty
                                     for item, qty in zip(x["items"],x["quantity"]) )> 500,
                                     orders
                                     ))
#sum map orders 
result = list(map(
    lambda x:  (x["customer"],sum(menu[item] * qty
                                   for  item,  qty in zip(x["items"],x["quantity"]))),
                                   filtered
))

sorted_result = sorted(result,reverse=True)

best = max(result,key=lambda x: x[1])  #max
worst =  min(result,key=lambda x: x[1]) #min

total_order = list(map(lambda x: x[1],result))
print(sum(total_order),"$")

item_count = {}
for  order in orders:
    for item, qty   in zip(order["items"],order["quantity"]):
        if item  in item_count:
            item_count[item] += qty
        else:
            item_count[item] =   qty

best_menu = max(item_count,key=lambda x:  item_count[x])
print(best_menu,item_count[best_menu])
print("Beat customer",best[0],best[1],"$")
print("Worst customer",worst[0],worst[1],"$")