##project 5
orders = [
    {"customer": "Alice", "product": "Laptop", "price": 1200, "quantity": 2, "country": "Thailand"},
    {"customer": "Bob", "product": "Phone", "price": 800, "quantity": 1, "country": "Singapore"},
    {"customer": "Charlie", "product": "Tablet", "price": 450, "quantity": 3, "country": "Thailand"},
    {"customer": "Diana", "product": "Laptop", "price": 1200, "quantity": 1, "country": "Malaysia"},
    {"customer": "Eve", "product": "Phone", "price": 800, "quantity": 2, "country": "Singapore"},
    {"customer": "Frank", "product": "Watch", "price": 300, "quantity": 4, "country": "Thailand"},
    {"customer": "Grace", "product": "Laptop", "price": 1200, "quantity": 3, "country": "Malaysia"},
    {"customer": "Henry", "product": "Tablet", "price": 450, "quantity": 2, "country": "Singapore"},
]

total_price =list(filter(lambda x: x["price"] * x["quantity"]> 1000,orders))

result = list(map(lambda x: (x["customer"],x["price"] * x["quantity"]),total_price))

sorted_result = sorted(result,reverse=True)

orders_only = list(map(lambda x:x[1],result))

print(sum(orders_only),"$")
print("Max",max(orders_only),"$")
print("Min",min(orders_only),"$")