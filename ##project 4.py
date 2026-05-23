##project 4
sales = [
    {"name": "Alice", "sales": 1200, "region": "North"},
    {"name": "Bob", "sales": 850, "region": "South"},
    {"name": "Charlie", "sales": 2100, "region": "North"},
    {"name": "Diana", "sales": 430, "region": "East"},
    {"name": "Eve", "sales": 1750, "region": "South"},
    {"name": "Frank", "sales": 980, "region": "West"},
    {"name": "Grace", "sales": 3200, "region": "North"},
    {"name": "Henry", "sales": 620, "region": "East"},
    {"name": "Iris", "sales": 2800, "region": "West"},
    {"name": "Jack", "sales": 1100, "region": "South"},
    {"name": "Karen", "sales": 450, "region": "East"},
    {"name": "Leo", "sales": 1900, "region": "North"},
    {"name": "Mia", "sales": 750, "region": "West"},
    {"name": "Noah", "sales": 2400, "region": "South"},
    {"name": "Olivia", "sales": 310, "region": "East"},
]

filtered = list(filter(lambda x  : x["sales"] > 1000,sales)) 

result = list(map(lambda x: (x["name"], x["sales"] * 35),filtered)) #tran to bath

sorted_result = sorted(result,reverse=True) #max to min

sales_only = list(map(lambda x:x[1],result))

print("Sorted",sorted_result)
print("total",sum(sales_only),"THB")
print("Max",max(sales_only),"THB") #max
print("Min",min(sales_only,),"THB")   #min